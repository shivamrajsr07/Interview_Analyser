from moviepy.editor import VideoFileClip
from textblob import TextBlob
import os

def analyze_speech(video_path):
    try:
        clip = VideoFileClip(video_path)
        audio_path = "temp_audio.wav"

        clip.audio.write_audiofile(audio_path, verbose=False, logger=None)

        # Simple placeholder text (no API dependency)
        text = "I am confident and excited about this opportunity"

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if os.path.exists(audio_path):
            os.remove(audio_path)

        return round(sentiment * 100, 2)

    except:
        return 0