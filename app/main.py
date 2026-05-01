import streamlit as st
import os
import sys

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.video_utils import analyze_eye_contact
from utils.audio_utils import analyze_speech
from utils.body_language import analyze_body_language
from utils.anxiety import analyze_anxiety
from utils.scoring import final_score

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Page config
st.set_page_config(page_title="AI Interview Analyzer", layout="centered")

st.title("🎯 AI Interview Analyzer")
st.write("Upload your interview video and get AI-based feedback")

# Upload video
uploaded_file = st.file_uploader("Upload Video", type=["mp4"])

if uploaded_file is not None:
    video_path = os.path.join("data", uploaded_file.name)

    # Save file
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.video(video_path)

    if st.button("Analyze Interview"):
        with st.spinner("Analyzing... Please wait"):

            # 🔥 Run all analysis modules
            eye = analyze_eye_contact(video_path)
            sentiment = analyze_speech(video_path)
            body = analyze_body_language(video_path)
            anxiety = analyze_anxiety(video_path)

            # 🔥 Final score calculation
            score = final_score(eye, sentiment, body, anxiety)

        st.success("Analysis Complete ✅")

        # 📊 Display metrics (5 columns now)
        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("👀 Eye Contact", f"{eye}%")
        col2.metric("🗣 Sentiment", f"{sentiment}")
        col3.metric("🧍 Body Language", f"{body}%")
        col4.metric("😰 Anxiety", f"{anxiety}%")
        col5.metric("⭐ Final Score", f"{score}%")

        # 🎯 Feedback
        st.subheader("📌 Performance Feedback")

        if score > 80 and anxiety < 30:
            st.success("🔥 Excellent! Confident and calm performance.")
        elif score > 60:
            st.warning("⚠️ Good, but reduce anxiety and improve posture.")
        else:
            st.error("❌ Needs improvement. Work on confidence and reduce nervousness.")

        # 📊 Breakdown
        st.subheader("📊 Score Breakdown")

        st.progress(int(eye))
        st.write("Eye Contact")

        st.progress(int((sentiment + 100) / 2))
        st.write("Sentiment")

        st.progress(int(body))
        st.write("Body Language")

        st.progress(int(anxiety))
        st.write("Anxiety")