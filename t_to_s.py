# it is a simple 5 lines of code to speech whatever you type as input.
#funwith python


# import the module required.
import pyttsx3
# initialising the model.
model = pyttsx3.init()

while True :                                                            # infinite loop
    speech = input("type anything to listen from me :")                 # taking input from user what to speak
    model.say(speech)
    model.runAndWait()
