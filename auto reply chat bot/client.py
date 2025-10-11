from google import genai

# NOTE: For security, never hardcode your API key. Use environment variables instead.
client = genai.Client(api_key="<API_KEY_HERE>")

# Assuming chat_history contains the history text you want the model to analyze

response = client.models.generate_content(
    model="gemini-2.5-flash",
    # FIX: The 'contents' argument must be a single list containing all messages (including system).
    contents=[
        # System Instruction (Role: user is used for system instructions in some multi-turn formats)
        {"role": "user", "parts": [{"text": "You are a person named azhar who speaks hindi as well as english. You analyze the following chat history and talk like him: "}]},
        
        # User Prompt (The core question)
        {"role": "user", "parts": [{"text": "Explain how AI works in a few words"}]}
    ]
)
print(response.text)




