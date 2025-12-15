# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pyttsx3
# import datetime
# import speech_recognition as sr
# import wikipedia
# import os
# import webbrowser
# import pyjokes
# import pywhatkit as kit
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend communication

# # Initialize text-to-speech engine
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# def speak(audio):
#     """Convert text to speech"""
#     engine.say(audio)
#     engine.runAndWait()

# def take_command():
#     """Listen to user's voice and convert to text"""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.pause_threshold = 0.8
#         recognizer.adjust_for_ambient_noise(source, duration=0.5)
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             print("Recognizing...")
#             query = recognizer.recognize_google(audio, language='en-in')
#             print(f"You said: {query}")
#             return query
#         except sr.WaitTimeoutError:
#             print("Listening timeout")
#             return "None"
#         except Exception as e:
#             print(f"Error: {e}")
#             return "None"

# def process_command(query):
#     """Process the voice command and return response"""
#     query = query.lower()
#     response = ""

#     try:
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             response = f"According to Wikipedia: {results}"
#             speak(response)
            
#         elif 'play' in query:
#             song = query.replace('play', "")
#             response = f"Playing {song} on YouTube"
#             speak(response)
#             kit.playonyt(song)
            
#         elif "hello" in query:
#             response = "Hello! How are you?"
#             speak(response)
            
#         elif "how are you" in query:
#             response = "I'm perfect, thank you for asking!"
#             speak(response)
            
#         elif "thank you" in query:
#             response = "You're welcome!"
#             speak(response)
            
#         elif 'open youtube' in query:
#             response = "Opening YouTube"
#             speak(response)
#             webbrowser.open("https://www.youtube.com/")
            
#         elif 'open google' in query:
#             response = "Opening Google"
#             speak(response)
#             webbrowser.open("https://www.google.com/")
            
#         elif 'open facebook' in query:
#             response = "Opening Facebook"
#             speak(response)
#             webbrowser.open("https://www.facebook.com/")
            
#         elif 'open instagram' in query:
#             response = "Opening Instagram"
#             speak(response)
#             webbrowser.open("https://www.instagram.com/")
            
#         elif 'search' in query:
#             s = query.replace('search', '')
#             response = f"Searching for {s}"
#             speak(response)
#             kit.search(s)
            
#         elif 'the time' in query or 'time' in query:
#             str_time = datetime.datetime.now().strftime("%H:%M:%S")
#             response = f"The time is {str_time}"
#             speak(response)
            
#         elif 'joke' in query:
#             joke = pyjokes.get_joke()
#             response = joke
#             speak(joke)
            
#         elif "where is" in query:
#             location = query.replace("where is", "").strip()
#             response = f"Locating {location} on Google Maps"
#             speak(response)
#             webbrowser.open("https://www.google.nl/maps/place/" + location.replace(" ", "+"))
            
#         elif "weather" in query:
#             search = "temperature in delhi"
#             url = f"https://www.google.com/search?q={search}"
#             r = requests.get(url)
#             data = BeautifulSoup(r.text, "html.parser")
#             temp = data.find("div", class_="BNeawe").text
#             response = f"Current {search} is {temp}"
#             speak(response)
            
#         elif "news" in query:
#             response = "Opening latest news"
#             speak(response)
#             webbrowser.open("https://news.google.com/")
            
#         elif "screenshot" in query:
#             import pyautogui
#             im = pyautogui.screenshot()
#             im.save("ss.jpg")
#             response = "Screenshot saved as ss.jpg"
#             speak(response)
            
#         elif "remember that" in query:
#             rememberMessage = query.replace("remember that", "")
#             speak("You told me to remember that " + rememberMessage)
#             remember = open("Remember.txt", "a")
#             remember.write(rememberMessage + "\n")
#             remember.close()
#             response = f"I'll remember that: {rememberMessage}"
            
#         elif "what do you remember" in query:
#             try:
#                 remember = open("Remember.txt", "r")
#                 content = remember.read()
#                 remember.close()
#                 response = "You told me to remember: " + content
#                 speak(response)
#             except FileNotFoundError:
#                 response = "You haven't asked me to remember anything yet."
#                 speak(response)
            
#         elif 'exit' in query or 'stop' in query:
#             response = "Thanks for using the assistant. Goodbye!"
#             speak(response)
            
#         else:
#             response = "I didn't understand that command. Please try again."
#             speak(response)
            
#     except Exception as e:
#         response = f"Error processing command: {str(e)}"
#         print(response)
    
#     return response

# # API Routes

# @app.route('/api/status', methods=['GET'])
# def status():
#     """Check if backend is running"""
#     return jsonify({
#         'status': 'active',
#         'message': 'Backend is running successfully',
#         'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     })

# @app.route('/api/listen', methods=['POST'])
# def listen():
#     """Listen to voice command and process it"""
#     data = request.json
#     userName = data.get('userName', 'User')
    
#     # Greet user first time
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour < 6:
#         greeting = 'Good night! Sleep tight.'
#     elif 6 <= hour < 12:
#         greeting = 'Good morning!'
#     elif 12 <= hour < 18:
#         greeting = 'Good afternoon!'
#     else:
#         greeting = 'Good evening!'
    
#     speak(f"{greeting} {userName}. How can I help you?")
    
#     # Listen to command
#     query = take_command()
    
#     if query == "None":
#         return jsonify({
#             'transcript': 'No speech detected',
#             'response': 'I could not hear anything. Please try again.'
#         })
    
#     # Process command
#     response = process_command(query)
    
#     return jsonify({
#         'transcript': query,
#         'response': response,
#         'timestamp': datetime.datetime.now().strftime("%H:%M:%S")
#     })

# @app.route('/api/command', methods=['POST'])
# def command():
#     """Process a text command (from quick buttons)"""
#     data = request.json
#     query = data.get('command', '')
#     userName = data.get('userName', 'User')
    
#     if not query:
#         return jsonify({
#             'response': 'No command provided'
#         })
    
#     # Process command
#     response = process_command(query)
    
#     return jsonify({
#         'command': query,
#         'response': response,
#         'timestamp': datetime.datetime.now().strftime("%H:%M:%S")
#     })

# @app.route('/api/greet', methods=['POST'])
# def greet():
#     """Greet the user"""
#     data = request.json
#     userName = data.get('userName', 'User')
    
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour < 6:
#         greeting = 'Good night! Sleep tight.'
#     elif 6 <= hour < 12:
#         greeting = 'Good morning!'
#     elif 12 <= hour < 18:
#         greeting = 'Good afternoon!'
#     else:
#         greeting = 'Good evening!'
    
#     message = f"{greeting} {userName}. How can I help you?"
#     speak(message)
    
#     return jsonify({
#         'greeting': message,
#         'timestamp': datetime.datetime.now().strftime("%H:%M:%S")
#     })

# @app.route('/api/text-to-speech', methods=['POST'])
# def text_to_speech():
#     """Convert text to speech"""
#     data = request.json
#     text = data.get('text', '')
    
#     if not text:
#         return jsonify({
#             'error': 'No text provided'
#         }), 400
    
#     speak(text)
    
#     return jsonify({
#         'message': 'Speech completed',
#         'text': text
#     })

# # Root route
# @app.route('/')
# def home():
#     """Home route"""
#     return jsonify({
#         'message': 'Voice Assistant API is running!',
#         'endpoints': {
#             '/api/status': 'GET - Check backend status',
#             '/api/listen': 'POST - Listen and process voice command',
#             '/api/command': 'POST - Process text command',
#             '/api/greet': 'POST - Greet the user',
#             '/api/text-to-speech': 'POST - Convert text to speech'
#         }
#     })

# if __name__ == '__main__':
#     print("=" * 60)
#     print("🚀 Voice Assistant Backend Starting...")
#     print("=" * 60)
#     print("✅ Server running on http://localhost:5000")
#     print("✅ Open index.html in your browser to use the UI")
#     print("=" * 60)
#     print("\n📡 Available Endpoints:")
#     print("   GET  /api/status          - Check backend status")
#     print("   POST /api/listen          - Voice command")
#     print("   POST /api/command         - Text command")
#     print("   POST /api/greet           - Greet user")
#     print("   POST /api/text-to-speech  - Text to speech")
#     print("=" * 60)
#     print("\n🎤 Ready to receive commands!\n")
#     app.run(debug=True, port=5000, host='0.0.0.0')
from flask import Flask, request, jsonify
from flask_cors import CORS
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pyjokes
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup
import threading  # ✅ Added for thread-safe text-to-speech

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# ✅ Create a lock to prevent "run loop already started" error
tts_lock = threading.Lock()

def speak(audio):
    def run_tts():
        with tts_lock:
            try:
                engine.say(audio)
                engine.runAndWait()
            except RuntimeError:
                pass

    threading.Thread(target=run_tts, daemon=True).start()

def take_command():
    """Listen to user's voice and convert to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.8
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timeout")
            return "None"
        except Exception as e:
            print(f"Error: {e}")
            return "None"

def process_command(query):
    """Process the voice command and return response"""
    query = query.lower()
    response = ""

    try:
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            response = f"According to Wikipedia: {results}"
            speak(response)
            
        elif 'play' in query:
            song = query.replace('play', "")
            response = f"Playing {song} on YouTube"
            speak(response)
            kit.playonyt(song)
            
        elif "hello" in query:
            response = "Hello! How are you?"
            speak(response)
            
        elif "how are you" in query:
            response = "I'm perfect, thank you for asking!"
            speak(response)
            
        elif "thank you" in query:
            response = "You're welcome!"
            speak(response)
            
        elif 'open youtube' in query:
            response = "Opening YouTube"
            speak(response)
            webbrowser.open("https://www.youtube.com/")
            
        elif 'open google' in query:
            response = "Opening Google"
            speak(response)
            webbrowser.open("https://www.google.com/")
            
        elif 'open facebook' in query:
            response = "Opening Facebook"
            speak(response)
            webbrowser.open("https://www.facebook.com/")
            
        elif 'open instagram' in query:
            response = "Opening Instagram"
            speak(response)
            webbrowser.open("https://www.instagram.com/")
            
        elif 'search' in query:
            s = query.replace('search', '')
            response = f"Searching for {s}"
            speak(response)
            kit.search(s)
            
        elif 'the time' in query or 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The time is {str_time}"
            speak(response)
            
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            response = joke
            speak(joke)
            
        elif "where is" in query:
            location = query.replace("where is", "").strip()
            response = f"Locating {location} on Google Maps"
            speak(response)
            webbrowser.open("https://www.google.nl/maps/place/" + location.replace(" ", "+"))
            
        elif "weather" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            response = f"Current {search} is {temp}"
            speak(response)
            
        elif "news" in query:
            response = "Opening latest news"
            speak(response)
            webbrowser.open("https://news.google.com/")
            
        elif "screenshot" in query:
            import pyautogui
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            response = "Screenshot saved as ss.jpg"
            speak(response)
            
        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "")
            speak("You told me to remember that " + rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage + "\n")
            remember.close()
            response = f"I'll remember that: {rememberMessage}"
            
        elif "what do you remember" in query:
            try:
                remember = open("Remember.txt", "r")
                content = remember.read()
                remember.close()
                response = "You told me to remember: " + content
                speak(response)
            except FileNotFoundError:
                response = "You haven't asked me to remember anything yet."
                speak(response)
            
        elif 'exit' in query or 'stop' in query:
            response = "Thanks for using the assistant. Goodbye!"
            speak(response)
            
        else:
            response = "I didn't understand that command. Please try again."
            speak(response)
            
    except Exception as e:
        response = f"Error processing command: {str(e)}"
        print(response)
    
    return response


# ================= API Routes =================

@app.route('/api/status', methods=['GET'])
def status():
    """Check if backend is running"""
    return jsonify({
        'status': 'active',
        'message': 'Backend is running successfully',
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/listen', methods=['POST'])
def listen():
    """Listen to voice command and process it"""
    data = request.json
    userName = data.get('userName', 'User')
    
    # Greet user
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 6:
        greeting = 'Good night! Sleep tight.'
    elif 6 <= hour < 12:
        greeting = 'Good morning!'
    elif 12 <= hour < 18:
        greeting = 'Good afternoon!'
    else:
        greeting = 'Good evening!'
    
    speak(f"{greeting} {userName}. How can I help you?")
    
    query = take_command()
    
    if query == "None":
        return jsonify({
            'transcript': 'No speech detected',
            'response': 'I could not hear anything. Please try again.'
        })
    
    response = process_command(query)
    
    return jsonify({
        'transcript': query,
        'response': response,
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S")
    })

@app.route('/api/command', methods=['POST'])
def command():
    """Process a text command"""
    data = request.json
    query = data.get('command', '')
    userName = data.get('userName', 'User')
    
    if not query:
        return jsonify({'response': 'No command provided'})
    
    response = process_command(query)
    
    return jsonify({
        'command': query,
        'response': response,
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S")
    })

@app.route('/api/greet', methods=['POST'])
def greet():
    """Greet the user"""
    data = request.json
    userName = data.get('userName', 'User')
    
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 6:
        greeting = 'Good night! Sleep tight.'
    elif 6 <= hour < 12:
        greeting = 'Good morning!'
    elif 12 <= hour < 18:
        greeting = 'Good afternoon!'
    else:
        greeting = 'Good evening!'
    
    message = f"{greeting} {userName}. How can I help you?"
    speak(message)
    
    return jsonify({
        'greeting': message,
        'timestamp': datetime.datetime.now().strftime("%H:%M:%S")
    })

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    """Convert text to speech"""
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    speak(text)
    
    return jsonify({
        'message': 'Speech completed',
        'text': text
    })

@app.route('/')
def home():
    """Home route"""
    return jsonify({
        'message': 'Voice Assistant API is running!',
        'endpoints': {
            '/api/status': 'GET - Check backend status',
            '/api/listen': 'POST - Listen and process voice command',
            '/api/command': 'POST - Process text command',
            '/api/greet': 'POST - Greet the user',
            '/api/text-to-speech': 'POST - Convert text to speech'
        }
    })

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Voice Assistant Backend Starting...")
    print("=" * 60)
    print("✅ Server running on http://localhost:5000")
    print("✅ Open index.html in your browser to use the UI")
    print("=" * 60)
    print("\n📡 Available Endpoints:")
    print("   GET  /api/status          - Check backend status")
    print("   POST /api/listen          - Voice command")
    print("   POST /api/command         - Text command")
    print("   POST /api/greet           - Greet user")
    print("   POST /api/text-to-speech  - Text to speech")
    print("=" * 60)
    print("\n🎤 Ready to receive commands!\n")
    app.run(debug=True, port=5000, host='0.0.0.0')
