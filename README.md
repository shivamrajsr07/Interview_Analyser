🚀 AI Interview Analyzer

An AI-powered system that evaluates interview performance using video, audio, and NLP analysis.

📌 Project Overview

The AI Interview Analyzer helps candidates improve their interview skills by analyzing:

🎤 Speech & confidence

🙂 Facial expressions

👁️ Eye contact

💬 Sentiment of answers

It provides a complete performance score and feedback dashboard.

🎯 Key Features

📹 Upload interview video (1–2 mins)

🎤 Extract and analyze speech

🙂 Detect facial expressions

👁️ Eye contact tracking using OpenCV

💬 Sentiment analysis using NLP

📊 Performance scoring system

🖥️ Interactive UI using Streamlit

🧠 Tech Stack
Category	Technology
Frontend	Streamlit
Video Processing	OpenCV
Audio Processing	MoviePy
NLP	TextBlob
Data Processing	NumPy, Pandas
Visualization	Matplotlib
📂 Project Structure
ai-interview-analyzer/
│
├── app/
│   └── main.py
│
├── utils/
│   ├── audio_utils.py
│   ├── video_utils.py
│
├── data/
├── assets/
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/shivamrajsr07/ai-interview-analyzer.git
cd ai-interview-analyzer
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install --upgrade pip
pip install streamlit opencv-python moviepy imageio-ffmpeg numpy pandas matplotlib scikit-learn textblob librosa soundfile
python -m textblob.download_corpora
▶️ Run the Application
python -m streamlit run app/main.py

👉 Open in browser:

http://localhost:8501
🎥 Input Requirements

Duration: 1–2 minutes

Format: .mp4

Content: Interview answer (e.g., “Tell me about yourself”)

Clear face + audio required

📊 Output

The system provides:

✅ Confidence Score

🙂 Emotion Analysis

👁️ Eye Contact Score

💬 Sentiment Score

📈 Final Performance Score

💡 Future Enhancements

🎤 Speech-to-text using Whisper AI

😐 Advanced emotion detection (Deep Learning)

🌍 Cloud deployment

📊 Advanced analytics dashboard

🏆 Use Case

Students preparing for placements

Mock interview practice

Communication skill evaluation

👨‍💻 Author

Shivam Raj
GitHub: https://github.com/shivamrajsr07