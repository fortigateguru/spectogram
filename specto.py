import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sine Wave Generator")

# Sliders for wave parameters
amplitude = st.slider("Amplitude", 0.1, 2.0, 1.0, 0.1)
frequency = st.slider("Frequency", 0.1, 5.0, 1.0, 0.1)
phase = st.slider("Phase (radians)", 0.0, 2*np.pi, 0.0, 0.1)

# Generate x values
x = np.linspace(0, 2*np.pi, 1000)

# Generate y values (sine wave)
y = amplitude * np.sin(frequency * x + phase)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y)
ax.set_title(f"Sine Wave: A={amplitude}, f={frequency}, φ={phase:.2f}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)

# Set y-axis limits based on amplitude
ax.set_ylim(-2, 2)

# Display the plot in Streamlit
st.pyplot(fig)

# Display the equation
st.latex(f"y = {amplitude:.1f} \sin({frequency:.1f}x + {phase:.2f})")

# Optional: Display raw data
if st.checkbox("Show raw data"):
    st.write(pd.DataFrame({"x": x, "y": y}))
