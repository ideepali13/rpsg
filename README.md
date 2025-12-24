# ✊✋✌️ Rock Paper Scissors – Hand Gesture Game (OpenCV)

A real-time Rock–Paper–Scissors game built using Python and Computer Vision, where the player interacts with the system using hand gestures detected via webcam.

This project uses OpenCV and MediaPipe to recognize hand landmarks, classify gestures, and simulate gameplay against a computer opponent.

---

## 🔍 Project Overview

This project transforms the classic Rock–Paper–Scissors game into a gesture-controlled computer vision application.  
The player shows a hand gesture in front of the camera, which is detected and interpreted automatically to determine the game outcome.

The project demonstrates:
- Real-time computer vision
- Hand landmark detection
- Gesture recognition logic
- Interactive Python application design

---

## ✨ Key Features

- Live webcam input processing  
- Hand landmark detection using MediaPipe  
- Gesture recognition for Rock, Paper, and Scissors  
- Computer-generated opponent moves  
- Real-time result display (Win / Lose / Draw)  
- Smooth and responsive gameplay  

---

## 🧰 Tech Stack

- Python  
- OpenCV  
- MediaPipe  
- NumPy  
- Random module  

---

## 📁 Project Structure

rock-paper-scissors-opencv/
│
├── main.py
├── requirements.txt
├── README.md
└── demo/

---

## ⚙️ Setup & Installation

### Step 1: Clone the Repository
git clone https://github.com/your-username/rock-paper-scissors-opencv.git  
cd rock-paper-scissors-opencv

### Step 2: Install Dependencies
pip install -r requirements.txt

### Step 3: Run the Application
python main.py

Note: Ensure your webcam is connected and permissions are enabled.

---

## ✋ Gesture Classification Logic

Gesture     | Fingers Detected
------------|------------------
Rock        | 0 fingers
Paper       | 5 fingers
Scissors    | 2 fingers

---

## 🔄 Working Principle

1. Webcam captures continuous video frames  
2. MediaPipe identifies hand landmarks  
3. Finger-count logic classifies the gesture  
4. Computer randomly selects its move  
5. Game rules determine the winner  
6. Result is displayed instantly on screen  

---

## 🚀 Learning Outcomes

- Understanding real-time computer vision pipelines  
- Implementing gesture recognition systems  
- Applying OpenCV with MediaPipe  
- Building interactive AI-based applications  
- Strengthening Python problem-solving skills  

---

## 🛠️ Future Enhancements

- Countdown timer before move capture  
- Scoreboard with win/loss tracking  
- Improved UI and animations  
- Multiplayer or AI difficulty modes  
- Conversion to executable (.exe)  

---

## 📸 Demo

Demo video or screenshots can be added here.

---

## 👩‍💻 Author

Deepali Chaturvedi  
Computer Science Student  
Interests: Computer Vision, AI, Python Development

---

## 📄 License

This project is open-source and available for educational and personal use.
