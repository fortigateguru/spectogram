import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import io

# Set the title of the app
st.title("MFCC Spectrogram Viewer")

# Upload audio file
uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3"])

# Process and display MFCC if a file is uploaded
if uploaded_file is not None:
    # Load the audio file
    y, sr = librosa.load(uploaded_file, sr=None)
    
    # Calculate MFCC
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    
    # Plot MFCC
    fig, ax = plt.subplots()
    img = librosa.display.specshow(mfccs, x_axis='time', ax=ax)
    ax.set(title='MFCC')
    fig.colorbar(img, ax=ax)
    
    # Display the plot
    st.pyplot(fig)
    
    # Display the MFCCs as a dataframe
    st.write("MFCCs:", mfccs)

# Footer information
st.markdown("Developed by [Your Name]")
