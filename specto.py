import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, ClientSettings

# Custom AudioProcessor to handle audio streaming
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.sr = 16000  # Sampling rate
        self.chunk_size = 1024  # Number of samples per chunk
        self.audio_buffer = []

    def recv(self, frame):
        audio_frame = frame.to_ndarray()
        self.audio_buffer.extend(audio_frame)

        if len(self.audio_buffer) >= self.sr:
            y = np.array(self.audio_buffer[:self.sr])
            self.audio_buffer = self.audio_buffer[self.sr:]

            mfccs = librosa.feature.mfcc(y=y, sr=self.sr, n_mfcc=13)
            fig, ax = plt.subplots()
            img = librosa.display.specshow(mfccs, sr=self.sr, x_axis='time', ax=ax)
            fig.colorbar(img, ax=ax)
            ax.set(title='Real-time MFCC')

            st.pyplot(fig)

        return frame

# Streamlit UI
st.title("Real-time MFCC Spectrogram Generator")

st.markdown("""
This application captures audio from your microphone and displays the MFCC spectrogram in real-time.
""")

# WebRTC settings
webrtc_streamer(
    key="audio",
    mode=ClientSettings.Mode.AUDIO_ONLY,
    audio_processor_factory=AudioProcessor,
    client_settings=ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"audio": True, "video": False},
    ),
)
