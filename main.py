import pyttsx3
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Diwakar")
    while(True):
      x = input("Enter what you want me to speak  ")
      if x=='q':
         break
      engine = pyttsx3.init()
      engine.say(x)
      engine.runAndWait()
