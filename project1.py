import os
import pyttsx3
import pyautogui
import wikipedia
import datetime
import speech_recognition as sr
import webbrowser
import random
import sys
import subprocess

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("jai sevalal. ma taro assistant. aja kai help kare saakuchu?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception as e:
        print("Sorry, I couldn't understand. Please say that again.")
        speak("Sorry, I couldn't understand. Please say that again.")
        return "None"
    return command.lower()

def open_application(app_name):
    try:
        if 'notepad' in app_name:
            os.system('notepad')
        elif 'chrome' in app_name:
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        elif 'explorer' in app_name:
            os.system('explorer')
        elif 'calculator' in app_name:
            os.system('calc')
        elif 'command prompt' in app_name:
            os.system('cmd')
        else:
            speak("Application not configured. Please try another one.")
    except Exception as e:
        speak("Failed to open the application.")

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
    except Exception as e:
        speak("Could not find information on Wikipedia.")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    speak("Screenshot taken and saved.")

def open_website(url):
    try:
        webbrowser.open(url)
        speak(f"Opening {url}")
    except Exception as e:
        speak("Failed to open the website.")

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    joke = random.choice(jokes)
    speak(joke)

def shutdown_system():
    speak("Shutting down the system. Goodbye!")
    os.system('shutdown /s /t 1')

def restart_system():
    speak("Restarting the system. Please wait.")
    os.system('shutdown /r /t 1')

def lock_system():
    speak("Locking the system.")
    os.system('rundll32.exe user32.dll,LockWorkStation')

def empty_recycle_bin():
    speak("Emptying the Recycle Bin.")
    subprocess.call(['powershell', '-command', 'Clear-RecycleBin', '-Force'])

def play_music():
    music_dir = 'C:\\Users\\Public\\Music'
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music.")
    else:
        speak("No music files found.")

def main():
    wish_user()
    while True:
        command = take_command()
        
        if 'open' in command:
            app = command.replace('open ', '')
            open_application(app)
        elif 'wikipedia' in command:
            query = command.replace('wikipedia ', '')
            search_wikipedia(query)
        elif 'screenshot' in command:
            take_screenshot()
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {current_time}")
        elif 'website' in command:
            url = command.replace('website ', '')
            open_website(url)
        elif 'joke' in command:
            tell_joke()
        elif 'shutdown' in command:
            shutdown_system()
        elif 'restart' in command:
            restart_system()
        elif 'lock' in command:
            lock_system()
        elif 'empty recycle bin' in command:
            empty_recycle_bin()
        elif 'play music' in command:
            play_music()
        elif 'exit' in command:
            speak("Goodbye!")
            sys.exit()
        else:
            speak("I didn't understand that. Please try again.")

if __name__ == '__main__':
    main()
    while True:
        query = wakeUpCommands().lower()
        if "wake up" in query:
            wishing()
            speak("Yes Boss, what can I do for you?")
            while True:
                query = commands().lower()

                if "wikipedia" in query:
                    speak("Searching Wikipedia...")
                    try:
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=1)
                        speak("According to Wikipedia:")
                        print(results)
                        speak(results)
                    except:
                        speak("No results found, sir.")

                elif "open youtube" in query:
                    speak("Opening YouTube")
                    pywhatkit.playonyt('music')

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif "mute" in query:
                    speak("Muting, Sir.")
                    break

                elif 'exit program' in query:
                    speak("Goodbye, Sir.")
                    quit()

                elif "open google" in query:
                    speak("Opening Google Chrome")
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    while True:
                        chromeQuery = commands().lower()
                        if "search" in chromeQuery:
                            searchQuery = chromeQuery.replace("search", "")
                            pyautogui.write(searchQuery)
                            pyautogui.press('enter')
                            speak('Searching...')
                        elif 'close chrome' in chromeQuery:
                            pyautogui.hotkey('ctrl', 'w')
                            speak("Closing Google Chrome")
                            break

                elif "screenshot" in query:
                    speak("Taking a screenshot...")
                    pyautogui.screenshot('screenshot.png')
                    speak("Screenshot saved!")

                elif "joke" in query:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)

                elif "play song" in query:
                    speak("Playing a song for you.")
                    songs = os.listdir(r'C:\Users\vrath\Music')
                    os.startfile(os.path.join(r'C:\Users\vrath\Music', songs[0]))

                elif "pause" in query:
                    pyautogui.press('space')
                    speak("Paused.")

                elif "open notepad" in query:
                    speak("Opening Notepad")
                    os.startfile("C:\\Windows\\System32\\notepad.exe")
                    while True:
                        notepadQuery = commands().lower()
                        if "type" in notepadQuery:
                            speak("What should I type?")
                            writeInNotepad = commands()
                            pyautogui.write(writeInNotepad)
                        elif "save" in notepadQuery:
                            pyautogui.hotkey('ctrl', 's')
                            speak("Saving the file.")
                        elif "close" in notepadQuery:
                            pyautogui.hotkey('alt', 'f4')
                            speak("Closing Notepad.")
                            break

                elif "info about" in query:
                    infoQuery = query.replace('info about', '')
                    speak("Getting information...")
                    try:
                        resInfo = pywhatkit.info(infoQuery, lines=2)
                        print(resInfo)
                        speak(resInfo)
                    except:
                        speak("Couldn't find information.")

                elif "exit" in query:
                    speak("Goodbye, Boss!")
                    quit()

