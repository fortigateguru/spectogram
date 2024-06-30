import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

st.title("MFCC Spectrogram Viewer")

uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3"])

if uploaded_file is not None:
    try:
        y, sr = librosa.load(uploaded_file, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        fig, ax = plt.subplots()
        img = librosa.display.specshow(mfccs, x_axis='time', ax=ax)
        ax.set(title='MFCC')
        fig.colorbar(img, ax=ax)
        st.pyplot(fig)
        st.write("MFCCs:", mfccs)
    except Exception as e:
        st.error(f"Error processing the audio file: {e}")

st.markdown("Developed by [Your Name]")
