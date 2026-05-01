# 🎯 AI Interview Analyzer

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=AI+Interview+Analyzer;Analyze+Your+Confidence+%F0%9F%92%AC;Improve+Your+Interview+Skills+%F0%9F%9A%80;Powered+by+AI+%F0%9F%A4%96" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/NLP-TextBlob-yellow?style=for-the-badge"/>
</p>

---

## 🚀 Overview

**AI Interview Analyzer** is a smart system that evaluates interview performance using **video, audio, and NLP analysis**.

It provides real-time insights into:
- Communication skills  
- Confidence level  
- Body language  
- Emotional behavior  

---

## ✨ Features

- 📹 Upload interview video  
- 🎤 Speech & sentiment analysis  
- 👁️ Eye contact tracking  
- 🧍 Body language detection  
- 😰 Anxiety estimation  
- 📊 AI-based scoring system  
- 🖥️ Interactive dashboard (Streamlit)

---

## 🧠 Tech Stack

| Category | Technology |
|--------|------------|
| Frontend | Streamlit |
| Video Processing | OpenCV |
| Audio Processing | MoviePy |
| NLP | TextBlob |
| ML | Scikit-learn |
| Data | NumPy, Pandas |

---

## 📂 Project Structure


ai-interview-analyzer/
│
├── app/
│ └── main.py
│
├── utils/
│ ├── audio_utils.py
│ ├── video_utils.py
│ ├── body_language.py
│ ├── scoring.py
│ ├── anxiety.py
│
├── data/
├── assets/
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone Repo
```bash
git clone https://github.com/shivamrajsr07/Interview_Analyser.git
cd ai-interview-analyzer
2️⃣ Setup Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
python -m textblob.download_corpora
▶️ Run App
streamlit run app/main.py

👉 Open in browser:
http://localhost:8501

🎥 Input Requirements
Format: .mp4
Duration: 1–2 minutes
Clear face + voice
📊 Output
👁️ Eye Contact Score
🗣 Sentiment Score
🧍 Body Language Score
😰 Anxiety Score
⭐ Final Performance Score
📸 Demo Preview
<p align="center"> <img src="https://user-images.githubusercontent.com/placeholder/demo.gif" width="700"/> </p>
💡 Future Enhancements
🎤 Whisper-based speech recognition
🤖 Deep learning emotion detection
☁️ Cloud deployment
📊 Advanced analytics
🎯 Use Cases
Interview preparation
Mock interview practice
Communication skill improvement
AI-based candidate evaluation
👨‍💻 Author

Shivam Raj

🔗 GitHub: https://github.com/shivamrajsr07
💼 LinkedIn: https://linkedin.com/in/impressiveboy
⭐ Show Some Love


