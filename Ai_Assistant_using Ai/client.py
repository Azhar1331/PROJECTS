import openai
from openai import OpenAI
import os

# --- Client Initialization ---
# The client is correctly initialized to point to the OpenRouter base URL.
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    # The API key must be an OpenRouter key, not an OpenAI key.
    api_key="<API_KEY_HERE>",
)

# --- Chat Completion Call ---
completion = client.chat.completions.create(
    # --- FIX: Uncomment and provide real values for these headers ---
    # These are required by OpenRouter for proper usage tracking/ranking.
    extra_headers={
        "HTTP-Referer": "https://www.your-site-url.com", # REQUIRED: Use your website's domain or a placeholder.
        "X-Title": "My Mega Project Assistant",          # OPTIONAL: Use a descriptive name for your project.
    },
    # extra_body={}, # Removed as it's not needed here
    model="deepseek/deepseek-chat-v3.1:free",
    messages=[
        {"role": "user", "content": "What is the meaning of life?"}
    ]
)

print(completion.choices[0].message.content)
