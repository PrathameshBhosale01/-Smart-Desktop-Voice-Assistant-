import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pyjokes
import pywhatkit as kit
import time
import requests
import random
import pyautogui
from bs4 import BeautifulSoup
import pyautogui
from plyer import notification
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, BOTH, SUNKEN
from PIL import Image, ImageTk
from threading import Thread


# Constants for custom styling
BG_COLOR = "#D2C6E2"
BUTTON_COLOR = "#F9F4F2"
BUTTON_FONT = ("Arial", 14, "bold")
BUTTON_FOREGROUND = "black"
HEADING_FONT = ("white", 24, "bold")
INSTRUCTION_FONT = ("Helvetica", 14)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


entry = None
stop_flag = False  # Define the stop_flag variable at the top of the script


def wish_time():
    global entry
    x = entry.get()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 6:
        speak('Good night! Sleep tight.')
    elif 6 <= hour < 12:
        speak('Good morning!')
    elif 12 <= hour < 18:
        speak('Good afternoon!')
    else:
        speak('Good evening!')
    speak(f"{x} How can I help you?")


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        speak("say something")
        recognizer.pause_threshold = 0.8
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for 1 second of ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        speak("recognizing")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def perform_task():
    global stop_flag
    while not stop_flag:
        query = take_command().lower()  # Converting user query into lower case
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation error (when the search term has multiple possible meanings)
                print(f"There are multiple meanings for '{query}'. Please be more specific.")
                speak(f"There are multiple meanings for '{query}'. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                # Handle page not found error (when the search term does not match any Wikipedia page)
                print(f"'{query}' does not match any Wikipedia page. Please try again.")
                speak(f"'{query}' does not match any Wikipedia page. Please try again.")
        elif 'play' in query:
            song = query.replace('play', "")
            speak("Playing " + song)
            kit.playonyt(song)
        elif "hello" in query:
            speak("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'search' in query:
            s = query.replace('search', '')
            kit.search(s)
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")
        elif 'open code' in query:
            code_path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location.replace(" ", "+"))
        elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
        elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
        # elif "ipl score" in query:
        #             from plyer import notification  #pip install plyer
        #             import requests #pip install requests
        #             from bs4 import BeautifulSoup #pip install bs4
        #             url = "https://www.cricbuzz.com/"
        #             page = requests.get(url)
        #             soup = BeautifulSoup(page.text,"html.parser")
        #             team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
        #             team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
        #             team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
        #             team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

        #             a = print(f"{team1} : {team1_score}")
        #             b = print(f"{team2} : {team2_score}")

        #             notification.notify(
        #                 title = "IPL SCORE :- ",
        #                 message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
        #                 timeout = 15
        #             )\
        elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                       webbrowser.open("https://www.youtube.com/watch?v=_ae2j9jZY_U&pp=ygUOY2hhcm1pbmcgc29uZ3M%3D")
        elif "news" in query:
                    from news import latestnews
                    latestnews()
        elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
        elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
        elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
        elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)
        elif "schedule my day" in query:
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = take_command().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
        elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
        elif "open" in query:
                    from dictapp import openappweb
                    openappweb(query)
        elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query)
        elif 'exit' in query:
            speak("thanks for giving your time")
            stop_voice_assistant()


def stop_voice_assistant():
    global stop_flag
    speak("Stopping the Voice Assistant.")
    stop_flag = True


def start_voice_assistant():
    global stop_flag
    wish_time()
    perform_task()
    stop_flag = False  # Reset the flag to False when starting the voice assistant


def main():
    # Create the main GUI window
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("500x700")
    root.configure(bg=BG_COLOR)

    def on_button_click():
        global stop_flag
        if not stop_flag:
            stop_flag = False  # Reset the flag to False when starting the voice assistant
            Thread(target=start_voice_assistant).start()
        else:
            stop_voice_assistant()

    # Load and set the background image
    background_image = Image.open(
        "wallpaperflare.com_wallpaper.jpg")  # Replace "path/to/your/background_image.jpg" with the actual image file path
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = ttk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    f1 = ttk.Frame(root)
    f1.pack(pady=100)  # Add some padding to the frame to center it vertically

    image2 = Image.open("p.jpg")  # Replace "path_to_image2.jpg" with the actual path to your image
    resized_image = image2.resize((120, 120))
    p2 = ImageTk.PhotoImage(resized_image)
    l2 = ttk.Label(f1, image=p2, relief=SUNKEN)
    l2.pack(side="top", fill="both")

    # Heading
    heading_label = ttk.Label(root, text="Voice Assistant", font=HEADING_FONT, background=BG_COLOR)
    heading_label.pack(pady=20)

    global entry
    f1 = ttk.Frame(root)
    f1.pack()
    l1 = ttk.Label(f1, text="Enter Your Name", font=INSTRUCTION_FONT, background=BG_COLOR)
    l1.pack(side=LEFT, fill=BOTH)
    entry = ttk.Entry(f1, width=30)
    entry.pack(pady=10)

    # Instruction
    instruction_label = ttk.Label(root, text="Click the button below to start the Voice Assistant.",
                                  font=INSTRUCTION_FONT, background=BG_COLOR)
    instruction_label.pack(pady=10)

    # Create and place a button on the GUI
    button = ttk.Button(root, text="Start Voice Assistant", command=on_button_click,
                        style="VoiceAssistant.TButton")
    button.pack(pady=20)

    # Style the button
    style = ttk.Style(root)
    style.configure("VoiceAssistant.TButton", font=BUTTON_FONT, background=BUTTON_COLOR, foreground=BUTTON_FOREGROUND)

    # Run the GUI main loop
    root.mainloop()


if __name__ == "__main__":
    main()


#     Great mindset! Enhancing your Smart Desktop Assistant can turn it from a basic automation tool into a more powerful and impressive project â€” especially for showcasing on your resume, GitHub, or interviews.

# ðŸ”§ Ways to Make Your Assistant More Advanced
# âœ… 1. NLP Integration (Natural Language Processing)
# What to Add: Understand user intent more smartly (e.g., "Can you open Google?" vs. "Launch Google").

# How: Use libraries like:

# transformers (e.g., BERT, GPT)

# spaCy or nltk for intent classification

# Outcome: More natural conversation and flexibility in user input.

# âœ… 2. Use GPT (LLMs) for Chat or Summarization
# What to Add: Integrate OpenAI or Gemini APIs to allow:

# Answering general questions

# Summarizing content

# Writing emails or messages

# Outcome: Assistant feels intelligent and conversational.

# âœ… 3. Email and Calendar Integration
# What to Add: Gmail/Outlook + Google Calendar support

# Features:

# Send emails by voice

# Read inbox summary

# Remind about meetings/events

# How: Use smtplib, Google API (google-api-python-client)

# âœ… 4. Voice Wake Word (Hotword Detection)
# What to Add: Say â€œJarvisâ€ or â€œSmartBotâ€ to activate it.

# How: Use libraries like snowboy (deprecated), porcupine, or build a simple VAD with webrtcvad.

# âœ… 5. GUI Enhancements
# What to Add:

# Animated assistant avatar

# Task summary list (To-Do) in the UI

# Dark/light theme toggle

# How: Use tkinter or switch to PyQt5 / PySide2 for more advanced GUI design.

# âœ… 6. Add System Monitoring Features
# What to Add: System stats like CPU, RAM, battery, and disk usage

# How: Use psutil

# Bonus: Speak alerts if system usage is high

# âœ… 7. Note-Taking + Daily Journal
# What to Add: A voice-to-text note recorder

# Save Format: Save daily notes to .txt or even .md files

# Bonus: Use gTTS for reverse (reading notes aloud)

# âœ… 8. Add Webcam Surveillance or Object Detection
# What to Add: Basic security mode to record motion

# How: Use cv2 (OpenCV)

# Bonus: Integrate face recognition for login or greeting

# âœ… 9. Weather + News in GUI
# Create a card-style interface for:

# Live Weather

# News Headlines

# YouTube Trends

# Auto-refresh every hour using after() loop in tkinter.

# âœ… 10. Dockerize It or Create an Executable
# Why: Makes your project deployable and portable

# Use:

# pyinstaller to make a .exe

# Docker to containerize your assistant

# ðŸ§  Extra Suggestions
# Category	Idea
# Personalization	Use userâ€™s name, birthday reminders
# Scheduler	Daily reminders using schedule or APScheduler
# Language	Add multi-language support using googletrans
# Security	Add voice-based password protection
# API Integration	ChatGPT, Google Maps, Spotify, Twitter, etc.

# ðŸ“¦ Example of an Advanced Feature List
# You can label your assistant as:

# "An intelligent desktop assistant with GUI, voice control, NLP, web scraping, system monitoring, and real-time reminders."

