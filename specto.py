import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import speech_recognition as sr
from transformers import pipeline
import numpy as np

# Title of the Streamlit app
st.title('Audio Analysis with MFCC and Sentiment Analysis')

# File uploader to upload an audio file
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])

if audio_file is not None:
    # Load the audio file
    y, sr = librosa.load(audio_file, sr=None)
    
    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    
    # Plot MFCC
    fig, ax = plt.subplots(figsize=(10, 6))
    img = librosa.display.specshow(mfccs, x_axis='time', ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    ax.set(title='MFCC')
    st.pyplot(fig)
    
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Convert audio to text
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        st.write("Transcribed Text:")
        st.write(text)
    except sr.UnknownValueError:
        st.write("Google Speech Recognition could not understand audio")
        text = ""
    except sr.RequestError as e:
        st.write(f"Could not request results from Google Speech Recognition service; {e}")
        text = ""
    
    # Perform sentiment analysis
    if text:
        sentiment_pipeline = pipeline('sentiment-analysis')
        result = sentiment_pipeline(text)
        sentiment_label = result[0]['label']
        sentiment_score = result[0]['score']
        
        st.write("Sentiment Analysis Result:")
        st.write(f"Sentiment: {sentiment_label}, Score: {sentiment_score}")

# Instructions
st.write("""
## Instructions
1. Upload an audio file in WAV, MP3, or OGG format.
2. The app will display the MFCC spectrogram of the audio.
3. The app will transcribe the audio to text using Google's Speech Recognition.
4. The app will perform sentiment analysis on the transcribed text and display the result.
""")
