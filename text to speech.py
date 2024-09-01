import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get text input from the user
text = input("Enter the text you want to convert to speech: ")

# Use text-to-speech to say the input text
engine.say(text)
engine.runAndWait()
