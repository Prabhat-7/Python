import winsound
import time
import pyttsx3 
engine=pyttsx3.init()
engine.setProperty('rate',120)
frequency = 1700
  # Set Frequency To 2500 Hertz
duration=1000
while True:
    time.sleep(5)
    winsound.Beep(frequency, duration)

    engine.say("Drink water..")
    engine.runAndWait()
