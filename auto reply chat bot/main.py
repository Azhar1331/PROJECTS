import pyautogui
import pyperclip
import time
from google import genai
import re # Required for the message checking function


"""
NOTE : THIS IS A PERSONAL PROJECT ADJUSTED ACCORDING TO SETUP CUSTOMIZE IT ACCORDING TO YOUR SETUP
LIKE POSITIONS AND ALL
"""
# --- Utility Function: Checks if the last message was sent by someone else ---
def is_last_message_from_other_person(chat_history: str, my_name: str = "Azhar") -> bool:
    lines = [line.strip() for line in chat_history.strip().split('\n') if line.strip()]

    if not lines:
        return False

    last_line = lines[-1]
    
    # Regex to check if the line starts with "Azhar" followed by a delimiter like :, -, or space
    pattern = re.compile(r"^\s*" + re.escape(my_name) + r"[:\-\s]+", re.IGNORECASE)
    
    if pattern.search(last_line):
        print(f"[Check] Last message was sent by {my_name}. Skipping reply.")
        return False
    else:
        print(f"[Check] Last message was NOT sent by {my_name}. Generating reply...")
        return True
# --- End of Utility Function ---


client = genai.Client(api_key="API KEY HERE")

pyautogui.click(464, 753)
time.sleep(1)

while True:
    # step-1 -CLicks on the Enter message section (Start chat by clicking the input field)

    #step-2 - Drag the mouse  from (444,118) to (1331 ,702) to select the text
    pyautogui.moveTo(522, 152)
    pyautogui.dragTo(966, 666 , duration=1.0 , button='left')

    #step-3 -copy the selected text to the keyboard:
    pyautogui.hotkey('ctrl','c')
    pyautogui.click(495, 179)
    time.sleep(1)

    #step4 - retrieve the text from  the clipboard and store it in a variable
    chat_history = pyperclip.paste()


    # --- CHECK IF AZHAR NEEDS TO REPLY BEFORE PROCEEDING ---
    if is_last_message_from_other_person(chat_history, my_name="Azhar"):
        
        # Define the persona prompt only if we need to reply
        persona_prompt = f"""
    You are an advanced AI assistant designed to **emulate the personality, style, and communication patterns** of the user named **Azhar**.

    ***
    [Azhar's Persona]
    ***
    **Name:** Azhar
    **Language/Tone:** Casual and friendly. Communicate primarily in **Hinglish** (a natural mix of Hindi and English) but be capable of replying fully in either language if the situation demands it.
    **Goal:** Analyze the provided chat history and the latest message to generate a relevant, human-like response *as if Azhar himself wrote it*.
    **Key Rules:**
    1.  **Do NOT** mention that you are an AI, a model, or an assistant.
    2.  **Maintain Context:** Use the style, vocabulary, and tone found in the chat history.
    3.  **Be Brief:** Keep responses short and to the point.
    4.  **Analyze and Respond:** The last part of the chat history contains the incoming message that Azhar needs to reply to. **Generate ONLY the reply text.**

    ***
    [Chat History]
    ***
    {chat_history}
    """
        
        # Generate the response
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            # The 'contents' argument must be a single list containing all messages (instructions + context).
            contents=[
                {"role": "user", "parts": [{"text": persona_prompt}]}
            ]
        )

        reply = response.text

        # step5 - Copy the generated AI response to the clipboard
        pyperclip.copy(reply)
        pyautogui.click(620, 711) 

        # step6 - Click the WhatsApp message input place (Your specified coordinates)
        # Co-ordinates: (620, 711)
        time.sleep(0.5) # Wait for the cursor to appear

        # step7 - Paste the response from the clipboard
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        # step8 - Press Enter to send the message
        pyautogui.press('enter')

        # Print the response to the terminal as well (for debugging)
        print("Response sent:", reply)

    else:
        print("Script finished. Azhar sent the last message.")


#615 744
#444 118 
#10
#1331
