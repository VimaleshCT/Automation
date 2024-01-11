import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning my Dear Friend")
    elif 12 <= hour < 16:
        speak("Good Afternoon my Dear Friend")
    else:
        speak("Good Evening my Dear Friend")
    speak("Let me know how can I help you, what are you looking for?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you Vimal....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"My dear friend you said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Vimal say that again please....")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pranovvimal30@gmail.com', 'Pranov@26')
    server.sendmail('pranovvimal30@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'open notepad' in query:
            npath = "C:\\Windows32\\notepad.exe"
            os.startfile(npath)

        elif 'open paint' in query:
            npath = "C:\\windows\\system32\\mspaint.exe"
            os.startfile(npath)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open github' in query:
            webbrowser.open('github.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"My dear Friend, the time is {strTime}")

        elif 'open linkedin' in query:
            webbrowser.open('www.linkedin.com')

        elif 'email to other friend' in query:
            try:
                speak("what should I send?")
                content = takecommand()
                to = "ctvimal05@gmail.com"
                sendEmail(to, content)
                speak("Your email has been sent successfully!!")

            except Exception as e:
                print(e)
                speak("My dear friend... I am unable to send the email..please address the error")
