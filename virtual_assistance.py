import smtplib
import webbrowser
import os
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # get details of current voice
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    # speak(f"Sir, the time is {strTime}")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak(f"Good Morning! {strTime} hour")
    elif 12 <= hour <= 18:
        speak(f"Good Afternoon! {strTime} hour")
    elif 18 <= hour <= 20:
        speak(f"Good Evening! {strTime} hour")
    else:
        speak(f"Good Night! {strTime} hour")
    speak("I am Jarvis, How may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nazirahammed98@gmail.com', 'nazir@786')
    server.sendmail('abibi2257@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # speak("Nasima is a Good Girl")  # Without this command, speech will not be audible to us.
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif "open youtube" in query:
            chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromedir).open("youtube.com")
            # webbrowser.open("youtube.com")
        elif "open google" in query:
            chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromedir).open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = "E:\\"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[7]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nazirahammed98@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
