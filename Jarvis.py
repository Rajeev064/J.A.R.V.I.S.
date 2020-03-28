import pyttsx3  #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import smtplib
'''
  from tkinter import *
  # create the canvas, size in pixels
  canvas = Canvas(width = 500, height = 300, bg = 'black')
  # pack the canvas into a frame/form
  canvas.pack(expand = YES, fill = BOTH)
  # load the .gif image file
  # put in your own gif file here, may need to add full path
  # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
  gif1 = PhotoImage(file = 'tenor.gif')
  # put gif image on canvas
  # pic's upper left corner (NW) on the canvas is at x=50 y=10
  canvas.create_image(50, 10, image = gif1, anchor = NW)
  # run it ...
  mainloop()
'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
   
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...") 
        #speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rajeevdemoprojects@gmail.com', 'RajeevDemoProjects@012')
    server.sendmail('rajeevdemoprojects@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            content = takeCommand()
            query = query.replace("wikipedia", content)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'exit' in query:
            speak("Bye sir. Have a nice day")
            raise SystemExit

        elif 'date and time' in query:
            #strTime = datetime.datetime.now().strftime("%H:%M:%S")
            strTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            speak(f"Sir, the date and time is {strTime}")

        elif 'restart the pc' in query:
            os.system("shutdown /r /t 1")

        elif 'Shutdown the pc' in query:
            os.system("shutdown /s /t 1")

        elif 'how is the weather' in query:
            import temp
            speak('''Enter city name''')
            city = takeCommand()
            temp.temp_check(city)
            
        elif 'play music' in query:
            import music
            speak('''Enter file name''')
            musicf1 = takeCommand()
            musicf = musicf1 + '''.mp3'''
            music.play_music(musicf)
         
        elif 'hello' in query:
            speak("Hello Sir")

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rs3167196@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")    

    

