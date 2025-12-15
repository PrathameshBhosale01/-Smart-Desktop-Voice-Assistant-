# 🎙️ Smart Voice Assistant 

A web-based Smart Voice Assistant built with **Python Flask** backend and a modern, responsive **HTML/CSS/JavaScript** frontend. The assistant listens to voice commands, performs various actions like opening websites and fetching information, and responds using text-to-speech.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

</div>

> ⚠️ **Note:** This project runs **locally only** due to microphone and OS-level access requirements. It cannot be deployed to static hosting services like GitHub Pages or Netlify.

---

## ✨ Features

- 🎤 **Voice Recognition** - Captures and processes voice commands in real-time
- 🔊 **Text-to-Speech** - Natural voice responses using pyttsx3
- 🌐 **Website Control** - Open popular websites with voice commands
- 🔍 **Web Search** - Perform Google searches via voice
- ⏰ **Time Information** - Get current time on demand
- 😂 **Entertainment** - Tell jokes and fun facts
- 🌦️ **Weather Updates** - Fetch current weather information
- 📰 **News Access** - Get latest news headlines
- 🌍 **Translation** - Multi-language translation support
- 💻 **Modern UI** - Clean, responsive interface with Tailwind CSS
- 🎨 **Real-time Feedback** - Visual indicators for listening state

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core programming language |
| Flask | Web framework and REST API |
| Flask-CORS | Cross-origin resource sharing |
| SpeechRecognition | Voice input processing |
| pyttsx3 | Text-to-speech engine |
| PyAudio | Audio I/O handling |
| Wikipedia API | Knowledge queries |
| Requests | HTTP requests |
| BeautifulSoup4 | Web scraping |
| PyWhatKit | YouTube and search automation |
| PyAutoGUI | GUI automation |

### Frontend
| Technology | Purpose |
|------------|---------|
| HTML5 | Structure and semantics |
| Tailwind CSS | Modern utility-first styling |
| JavaScript (ES6+) | Client-side logic and Fetch API |

---

## 📂 Project Structure

```
smart-voice-assistant/
│
├── app.py              # Flask backend server
├── index.html          # Web UI frontend
├── Translator.py       # Translation functionality
├── news.py            # News fetching logic
├── dictapp.py         # App/website control
├── requirements.txt   # Python dependencies
├── README.md          # Documentation
└── .gitignore         # Git ignore rules
```

---

## 🚀 Installation & Setup

### Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- Working microphone (enabled in system settings)
- Internet connection
- Modern web browser (Chrome, Firefox, Edge)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/smart-voice-assistant.git
cd smart-voice-assistant
```

### Step 2: Install Python Dependencies

```bash
pip install flask flask-cors pyttsx3 SpeechRecognition wikipedia pyjokes pywhatkit requests beautifulsoup4 pyautogui pyaudio
```

**Or use requirements.txt:**

```bash
pip install -r requirements.txt
```

#### Troubleshooting PyAudio Installation

**Windows:**
If PyAudio installation fails, download the appropriate `.whl` file from [Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install:

```bash
pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux:**
```bash
sudo apt-get install python3-pyaudio
```

### Step 3: Start the Backend Server

```bash
python app.py
```

**Expected output:**
```
Voice Assistant Backend Starting...
 * Running on http://127.0.0.1:5000
Server running on http://localhost:5000
```

⚠️ **Keep this terminal window open.**

### Step 4: Start the Frontend Server

Open a **new terminal** in the project directory:

```bash
python -m http.server 5500
```

### Step 5: Access the Application

Open your browser and navigate to:
```
http://localhost:5500/index.html
```

---

## 🎙️ Usage Guide

### Getting Started

1. **Enter Your Name** - Type your name in the input field
2. **Click the Microphone** - Press the microphone button to start listening
3. **Speak Clearly** - Give your command in a clear voice
4. **Wait for Response** - The assistant will process and respond

### Voice Commands Examples

| Command | Action |
|---------|--------|
| `open youtube` | Opens YouTube in browser |
| `open google` | Opens Google search |
| `search python tutorials` | Searches Google for "python tutorials" |
| `what is the time` | Tells current time |
| `tell me a joke` | Shares a random joke |
| `weather` | Fetches weather information |
| `news` | Gets latest news headlines |
| `wikipedia artificial intelligence` | Searches Wikipedia |
| `translate hello to spanish` | Translates text |

### Tips for Best Results

- Speak in a quiet environment
- Use clear, concise commands
- Wait for the "listening" indicator before speaking
- Avoid background noise

---

## ⚠️ Important Limitations

### Why This Can't Be Hosted Online

This project requires:
- **Microphone Access** - Browser security restrictions prevent direct microphone access on static hosting
- **Local System APIs** - Uses OS-level speech synthesis and audio libraries
- **PyAudio Dependencies** - Requires native audio drivers not available in web hosting
- **Process Control** - Opens applications and controls browser tabs locally

### Deployment Options

✅ **Can be used for:**
- Local development and testing
- Portfolio demonstrations via screen recording
- Live demos on your local machine
- Personal use projects

❌ **Cannot be deployed to:**
- GitHub Pages
- Netlify
- Vercel
- Heroku (without significant modifications)

---

## 📸 Screenshots

<img width="1206" height="920" alt="image" src="https://github.com/user-attachments/assets/944e3fee-9f69-4c8b-b373-45011c97f07c" />


## 🧠 Learning Outcomes

Working on this project helped me develop skills in:

- **Backend Development** - Building REST APIs with Flask
- **Frontend Integration** - Connecting JavaScript to Python backend
- **Audio Processing** - Handling speech recognition and synthesis
- **Asynchronous Programming** - Managing concurrent operations with threading
- **API Integration** - Working with external APIs (Wikipedia, Weather, News)
- **Error Handling** - Debugging system-level dependencies
- **UI/UX Design** - Creating responsive, user-friendly interfaces
- **Web Technologies** - Understanding CORS, HTTP requests, and browser APIs

---

## 🔧 Troubleshooting

### Common Issues

**Problem:** Microphone not working
- **Solution:** Check system permissions and microphone settings

**Problem:** "Module not found" error
- **Solution:** Ensure all dependencies are installed: `pip install -r requirements.txt`

**Problem:** Port already in use
- **Solution:** Change port in `app.py` (5000) or frontend server (5500)

**Problem:** CORS errors
- **Solution:** Verify Flask-CORS is installed and configured correctly

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Future Enhancements

- [ ] Add support for more voice commands
- [ ] Implement conversation history
- [ ] Add multi-language support
- [ ] Create custom wake word detection
- [ ] Implement calendar integration
- [ ] Add email sending functionality
- [ ] Create mobile responsive design improvements
- [ ] Add dark/light theme toggle

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Prathamesh Bhosale**  
Computer Science & Engineering Student

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github)](https://github.com/PrathameshBhosale01)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/prathamesh--bhosale/)

---

## 🙏 Acknowledgments

- Flask documentation and community
- SpeechRecognition library contributors
- Tailwind CSS team
- All open-source libraries used in this project

---

<div align="center">

**Made with ❤️ by Prathamesh**

⭐ Star this repo if you found it helpful!

</div>
