import pyttsx3 
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",120)
a=input("Enter a text what you want to be spoken:")

engine.say(a)
engine.runAndWait()

