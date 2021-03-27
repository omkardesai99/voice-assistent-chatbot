import speech_recognition as sr
import webbrowser
#import wikipedia
from time import strftime
import os
import sys
import re
import pyttsx3
from datetime import datetime
import smtplib, ssl

global day_time
n=datetime.now()
day_time=n.strftime('%H')

#interpret user voice response
engine=pyttsx3.init("sapi5")
rate=engine.getProperty("rate")
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',rate+1)
def microResponse(audiostring):
    engine.say(audiostring)
    engine.runAndWait()
def myCommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Say Somthing....')
        r.pause_threshold=0.5
        r.adjust_for_ambient_noise(source,duration=1)
        audiostring=r.listen(source)
    try:
        command=r.recognize_google(audiostring).lower()
        print('you said: '+command+ '\n')
    except sr.UnknownValueError:
        print('......')
        command=myCommand();
    return command

def assistance(command):
    global day_time
    "if statements for executing commands"
    if 'hello' in command:
        n=datetime.now()
        day_time=int(n.strftime('%H'))
        if day_time<12:
            microResponse('Hello User Good morning')
        elif 12<=day_time<18:
            microResponse('Hello User Good afternoon')
        else:
            microResponse('Hi user good evening')
    elif 'omkar' in command:
        microResponse('hello omkar how are you ....!')
        
    elif 'open google' in command:
        microResponse('opening google page')
        webbrowser.open('https://www.google.com/')
        
    elif 'open gmail' in command:
        microResponse('opening your gmail')
        webbrowser.open('https://mail.google.com/')
    
    elif 'send gmail' in command:
        microResponse('sending gmail')
        import os
        import smtplib, ssl
        mail = smtplib.SMTP('smtp.gmail.com', 587)#First it will initaite gmail SMTP 
        mail.ehlo()#then identify the server
        mail.starttls()#then encypting the session
        mail.login('#your email', 'your email password')
        mail.sendmail('your email','recipients email', 'try')
        mail.close()
        
    elif 'open youtube' in command:
        microResponse('opening youtube')
        webbrowser.open('https://www.youtube.com/')
        
    #terminate function
    elif 'shutdown' in command:
        microResponse('bye sir or mam Have a nice day!')
        
        sys.exit()
    return day_time
        
microResponse('this is omkar desais personal voice assistance how may i help u?')
microResponse('the time is' + day_time)
while True:
    assistance(myCommand())


