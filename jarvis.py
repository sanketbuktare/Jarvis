import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

master = "Saanket"
print("Initializing jarvis..")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + master)
    elif hour>=18 and hour<20:
        speak("Good Evening" + master)
    #else:
        speak("Good Night" + master)
    speak("I am jarvis. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again please")
        speak("Say that again please")
        query = takeCommand()
    
    return query

#main program
speak("initializing jarvis...")
wishMe()
while True:

    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        #webbrowser.open("youtube.com")
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "youtube.com"
        webbrowser.get(chrome_path).open(url)

    elif 'open linkedin' in query:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "linkedin.com"
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "google.com"
        webbrowser.get(chrome_path).open(url)

    elif 'email' in query:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "mail.google.com"
        webbrowser.get(chrome_path).open(url)

    elif 'music' in query:
        songs_dir = "C:\\Users\\ADMIN\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{strTime}")
        speak(f"{master} the time is {strTime}")

    elif 'shutdown' in query:
        break
    
speak(f"Okay {master} I am glad I could be of some help. Bye bye take care")
