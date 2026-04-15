#speech through text
'''
import pyttsx3
engine = pyttsx3.init()
def speech_thr_text(text):
    engine.say(text)
    engine.runAndWait()
speech_thr_text("Hey, I am your aasistant")
'''

'''
import pyttsx3
engine = pyttsx3.init()
def speak_text(text):
    engine.say(text)
user_text = input("Enter your message: ").lower()
name = "User"
if "my name is" in user_text:
    name = user_text.split("my name is") [-1].strip()
elif "name is" in user_text:
    name = user_text.split("name is") [-1].strip()
if user_text in ["hi", "hello", "hey"]:
    response = "Hello! How can I help you?"
elif "name" in user_text:
    response = f"Hello kunnu, how can I help you?"
else:
    response = "Sorry, I didn't understand that."
print(response)
speak_text(response)
engine.runAndWait()
'''


