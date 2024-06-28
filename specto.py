import streamlit as st
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import io

# Function to load audio and compute MFCC
def compute_mfcc(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfccs, sr

# Function to apply audio effects
def apply_audio_effect(y, effect):
    if effect == 'Pitch Shift':
        y = librosa.effects.pitch_shift(y, sr, n_steps=4)
    elif effect == 'Time Stretch':
        y = librosa.effects.time_stretch(y, 1.5)
    elif effect == 'Reverb':
        y = librosa.effects.preemphasis(y)
    return y

# Streamlit UI
st.title("Advanced MFCC Spectrogram Generator")

# File uploader
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file is not None:
    y, sr = librosa.load(audio_file, sr=None)

    # Select audio effect
    effect = st.selectbox("Choose an audio effect", ["None", "Pitch Shift", "Time Stretch", "Reverb"])
    
    if effect != "None":
        y = apply_audio_effect(y, effect)
    
    # Compute MFCC
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    # Plot MFCC
    fig, ax = plt.subplots()
    img = librosa.display.specshow(mfccs, sr=sr, x_axis='time', ax=ax)
    fig.colorbar(img, ax=ax)
    ax.set(title='MFCC')

    # Display plot in Streamlit
    st.pyplot(fig)

    # Downloadable report
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.download_button(label="Download Spectrogram", data=buf, file_name="spectrogram.png", mime="image/png")

    # Educational content
    st.markdown("""
    ### What is MFCC?
    Mel-frequency cepstral coefficients (MFCCs) are coefficients that collectively make up an MFC. They are derived from a type of cepstral representation of the audio clip (a nonlinear "spectrum-of-a-spectrum").
    
    ### Applications of MFCC
    - **Speech Recognition**: Used in various speech recognition systems to recognize spoken words.
    - **Music Information Retrieval**: Helps in identifying and classifying different genres of music.
    - **Acoustic Fingerprinting**: Used for recognizing audio clips by their unique "fingerprint".
    """)

    # Compare with another file
    compare_file = st.file_uploader("Upload another audio file to compare", type=["wav", "mp3"])
    if compare_file is not None:
        y_compare, sr_compare = librosa.load(compare_file, sr=None)
        mfccs_compare = librosa.feature.mfcc(y=y_compare, sr=sr_compare, n_mfcc=13)
        
        # Plot comparison
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        img1 = librosa.display.specshow(mfccs, sr=sr, x_axis='time', ax=ax1)
        ax1.set(title='Original MFCC')
        fig.colorbar(img1, ax=ax1)
        
        img2 = librosa.display.specshow(mfccs_compare, sr=sr_compare, x_axis='time', ax=ax2)
        ax2.set(title='Comparison MFCC')
        fig.colorbar(img2, ax=ax2)
        
        st.pyplot(fig)
