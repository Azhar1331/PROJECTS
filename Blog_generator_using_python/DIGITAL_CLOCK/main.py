import datetime as DT
import time as T

try:
    class DigitalClock:

        def update_time(self):
            now = DT.datetime.now()
            self.hour = now.hour
            self.minute = now.minute
            self.second = now.second
            self.time_string = f"{self.hour:02} : {self.minute:02} : {self.second:02}"


    my_clock = DigitalClock()

    while True:
        my_clock.update_time()
        print(my_clock.time_string, end='\r')
        T.sleep(1)

except Exception as e:
    print(e)