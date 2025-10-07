import speech_recognition as sr
import webbrowser 
import pyttsx3 
import music_lib 
from openai import OpenAI



recognizer = sr.Recognizer()
engine = pyttsx3.init()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    # The API key must be an OpenRouter key, not an OpenAI key.
    api_key="<OPEN_AI_API_KEY_HERE>",
)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def processCommand(c):
         if "open google" in c.lower():
              webbrowser.open("https://google.com")
         elif "open youtube" in c.lower():
              webbrowser.open("https://youtube.com")
         elif "open github" in c.lower():
              webbrowser.open("https://github.com/CodeWithHarry/The-Ultimate-Python-Course/blob/main/Mega%20Project%201%20-%20Jarvis/main.py")
         elif c.lower().startswith("play"):
              song = c.lower().split(" ")[1]
              link = music_lib.music[song]
              webbrowser.open(link)
              
         else:
             completion = client.chat.completions.create(
              # --- FIX: Uncomment and provide real values for these headers ---
              # These are required by OpenRouter for proper usage tracking/ranking.
              extra_headers={
                  "HTTP-Referer": "https://www.your-site-url.com", # REQUIRED: Use your website's domain or a placeholder.
                  "X-Title": "My Mega Project Assistant",# OPTIONAL: Use a descriptive name for your project.
              },
              # extra_body={}, # Removed as it's not needed here
              model="deepseek/deepseek-chat-v3.1:free",
              messages=[
                  {"role":"system", "content" : "You are a virtual assistant named jarvis that is skilled in general tasks like Alexa who gives short responses"},
                  {"role": "user", "content": command}
              ],
              # ADDED: max_tokens as a keyword argument
              max_tokens=100 
          )
             if "speak" in command:
               speak((completion.choices[0].message.content))
             else:
               print((completion.choices[0].message.content))
                    
             
             
            
         # --- Main loop remains the same ---
    
if __name__ == "__main__":
         print("Initialising Jarvis......") # Uncomment this line when ready
    
         while True:
              r = sr.Recognizer()
              try:
                       with sr.Microphone() as source:
                            print("Listening.....")
                            audio = r.listen(source)
                       print("Recognizing.....") 
                       word = r.recognize_google(audio)

                       if "jarvis" in word.lower():
                            print("Yeah")
                            with sr.Microphone() as source:
                                
                                while True:
                                     print("Jarvis Active.....")
                                     print("active_listening")
                                     audio = r.listen(source)
                                     print("Recognizing")
                                     command = r.recognize_google(audio) 
                                     
                                     if "exit" in command:
                                         break
                                     
                                     processCommand(command)
                                     
                                if "exit" in command:
                                    break

                                    
                                    
              except Exception as e:
                       print(e)