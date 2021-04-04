import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    houre = int(datetime.datetime.now().hour)
    if houre >= 0 and houre < 12:
        speak("Good Morning")
    elif houre >= 12 and houre < 18:
        speak("Good Afternoon")
    elif houre >= 18 and houre < 7.30:
        speak("Good Evening")
    else:
        speak("Good night")

    speak("Hi sir, How are you, my name is Davide I am assistance of pythonian Mezbah, how can help you")


def takeCommand():
    # It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-bd')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please..")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login('mezbahuddin800@gmail.com', 'password')
    server.sendmail('mezbahuddin800@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    # speak("I am good boy and i love python")
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open linkdin' in query:
            webbrowser.open("linkdin.com")
        elif 'open facebook' in query:
            webbrowser.open("fb.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open bing' in query:
            webbrowser.open("bing.com")
        elif 'open fiver' in query:
            webbrowser.open("fiver.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open wecaht' in query:
            webbrowser.open("wechat.com")


        elif 'play music' in query:
            # music_dir = 'D:\\Non Critical\\song\\Favorite Songs'
            music_dir = 'C:\\Users\\mezba\\Desktop\\New folder (3)'
            song = os.listdir(music_dir)
            print(song)
            # os.startfile(os.path.join(music_dir,song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\mezba\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\pycharm64.exe"
            os.startfile(pycharm)

        elif 'open to mezbah' in query:
            try:
                speak("what should i say")
                cintent = takeCommand()
                to = "mezbahuddin800Email@gmail.com"
                sendEmail(to, content)
                speak("Email has beeen send")
            except Exception as e:
                print(e)
                speak("sorry sir your Email is not send")


