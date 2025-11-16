import yfinance as yf 
import pandas as pd
import numpy as np
from datetime import date

class SMABacktester:
    def __init__(self, ticker, start_date, end_date, short_window, long_window, initial_capital=100000.0):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.short_window = short_window
        self.long_window = long_window
        self.initial_capital = initial_capital
        self.data = self._download_data()
        self._generate_signals()

    def _download_data(self):
        print(f"Downloading data for {self.ticker}...")
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        if data.empty:
            raise ValueError(f"No data downloaded for {self.ticker}")
        return data

    def _generate_signals(self):
        self.data['SMA_Short'] = self.data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        self.data['SMA_Long'] = self.data['Close'].rolling(window=self.long_window, min_periods=1).mean()

        self.data['Signal'] = 0.0

        self.data.loc[self.data.index[self.short_window:], 'Signal'] = np.where(
            self.data['SMA_Short'][self.short_window:] > self.data['SMA_Long'][self.short_window:], 
            1.0, 
            0.0
        )
        
        self.data['Position'] = self.data['Signal'].diff()

    def run_backtest(self):
        self.data['Returns'] = self.data['Close'].pct_change()
        
        self.data['Strategy_Returns'] = self.data['Returns'] * self.data['Signal'].shift(1)
        
        self.data['Cumulative_Strategy_Returns'] = \
            (1 + self.data['Strategy_Returns']).cumprod() * self.initial_capital
            
        self.data['Cumulative_Benchmark_Returns'] = \
            (1 + self.data['Returns']).cumprod() * self.initial_capital

        return self.data[['Cumulative_Strategy_Returns', 'Cumulative_Benchmark_Returns']]

    def calculate_metrics(self):
        returns = self.data['Strategy_Returns'].dropna()
        
        annualized_return = returns.mean() * 252 

        annualized_volatility = returns.std() * np.sqrt(252)

        sharpe_ratio = annualized_return / annualized_volatility

        cum_returns = self.data['Cumulative_Strategy_Returns'] / self.initial_capital
        peak = cum_returns.expanding(min_periods=1).max()
        drawdown = (cum_returns - peak) / peak
        max_drawdown = drawdown.min()
        
        return {
            "Annualized Return": f"{annualized_return * 100:.2f}%",
            "Annualized Volatility": f"{annualized_volatility * 100:.2f}%",
            "Sharpe Ratio": f"{sharpe_ratio:.2f}",
            "Max Drawdown": f"{max_drawdown * 100:.2f}%"
        }

if __name__ == '__main__':
    TICKER = input("""Enter The Company Stock Name {
    "Apple Inc.": "AAPL",
    "Microsoft Corp.": "MSFT",
    "Alphabet Inc. (Google)": "GOOGL",
    "Amazon.com Inc.": "AMZN",
    "Tesla, Inc.": "TSLA",
    "Johnson & Johnson": "JNJ",
    "JPMorgan Chase & Co.": "JPM",
    "Exxon Mobil Corp.": "XOM",
    "The Coca-Cola Company": "KO",
    "Walmart Inc.": "WMT",
    "Meta Platforms Inc. (Facebook)": "META",
    "Berkshire Hathaway Inc.": "BRK-B",
    "S&P 500 ETF": "SPY",
    "Nasdaq 100 ETF": "QQQ"
} :  """)
    
    START = "2019-01-01"
    END = date.today().strftime('%Y-%m-%d')
    SHORT_SMA = 50
    LONG_SMA = 200

    backtester = SMABacktester(
        ticker=TICKER, 
        start_date=START, 
        end_date=END, 
        short_window=SHORT_SMA, 
        long_window=LONG_SMA
    )

    results = backtester.run_backtest()

    metrics = backtester.calculate_metrics()

    print("\n" + "="*50)
    print(f"📈 Backtest Results for {TICKER} (SMA {SHORT_SMA}/{LONG_SMA})")
    print("="*50)
    
    print("\n--- Performance Metrics ---")
    for key, value in metrics.items():
        print(f"{key:<25}: {value}")

    print("\n--- Final Capital Comparison ---")
    final_strategy_capital = results['Cumulative_Strategy_Returns'].iloc[-1]
    final_benchmark_capital = results['Cumulative_Benchmark_Returns'].iloc[-1]

    print(f"Starting Capital: ${backtester.initial_capital:,.2f}")
    print(f"Final Strategy Capital: ${final_strategy_capital:,.2f}")
    print(f"Final Buy & Hold Capital: ${final_benchmark_capital:,.2f}")

    print("\n--- Example Data Tail (Last 5 Days) ---")
    print(backtester.data[['Close', 'SMA_Short', 'SMA_Long', 'Signal', 'Position', 'Strategy_Returns']].tail())

    try:
        import matplotlib.pyplot as plt
        results.plot(title=f'{TICKER} SMA Crossover Strategy Performance')
        plt.xlabel("Date")
        plt.ylabel("Capital ($)")
        plt.show()
    except ImportError:
        print("\nInstall matplotlib (`pip install matplotlib`) to see the performance chart.")