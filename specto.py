import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import io
import base64

# Function to load audio and compute MFCC
def compute_mfcc(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfccs, sr, y

# Function to create a downloadable report
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}">Download {filename}</a>'

# Streamlit UI
st.title("MFCC Spectrogram Generator and Report")

# File uploader
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file is not None:
    # Compute MFCC
    mfccs, sr, y = compute_mfcc(audio_file)
    
    # Plot MFCC
    fig, ax = plt.subplots()
    img = librosa.display.specshow(mfccs, sr=sr, x_axis='time', ax=ax)
    fig.colorbar(img, ax=ax)
    ax.set(title='MFCC')
    
    # Display plot in Streamlit
    st.pyplot(fig)

    # Create downloadable report
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.markdown(create_download_link(buf.getvalue(), "mfcc_spectrogram.png"), unsafe_allow_html=True)

    # Additional Analysis: Display waveform
    st.markdown("### Waveform")
    fig_waveform, ax_waveform = plt.subplots()
    librosa.display.waveshow(y, sr=sr, ax=ax_waveform)
    ax_waveform.set(title="Waveform")
    st.pyplot(fig_waveform)

    buf_waveform = io.BytesIO()
    fig_waveform.savefig(buf_waveform, format="png")
    st.markdown(create_download_link(buf_waveform.getvalue(), "waveform.png"), unsafe_allow_html=True)

    # Display a summary of the audio
    st.markdown("### Audio Summary")
    duration = librosa.get_duration(y=y, sr=sr)
    st.write(f"Duration: {duration:.2f} seconds")
    st.write(f"Sampling Rate: {sr} Hz")

    # Save the waveform and MFCC as downloadable report
    st.markdown("### Downloadable Report")
    report = f"Audio File: {audio_file.name}\n"
    report += f"Duration: {duration:.2f} seconds\n"
    report += f"Sampling Rate: {sr} Hz\n"

    report_buf = io.BytesIO()
    report_buf.write(report.encode('utf-8'))
    st.markdown(create_download_link(report_buf.getvalue(), "audio_report.txt"), unsafe_allow_html=True)
