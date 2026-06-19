import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit

def speak(text):
    print(f"Assistant: {text}")
    # Re-initialize pyttsx3 each time so it doesn’t hang
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't understand that. Please say again.")
        return "none"
    return query.lower()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning ruhina!")
    elif hour < 18:
        speak("Good afternoon ruhina!")
    else:
        speak("Good evening ruhina!")
    speak("I am your voice assistant. How can I help you?")

def main():
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("Sorry, I couldn’t find anything on Wikipedia.")

        elif 'open youtube' in query:
            speak("Opening YouTube now.")
            webbrowser.open("https://www.youtube.com")
            break
        elif 'open google' in query:
            speak("Opening Google now.")
            webbrowser.open("https://www.google.com")
            break
        elif 'time' in query:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_str}")
            break
        elif 'date' in query:
            date_str = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today is {date_str}")
            break
        elif 'play' in query:
            song = query.replace("play", "")
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
            break
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye ruhina, have a nice day!")
            break

        

if __name__ == "__main__":
    main()