import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Coin Counter App")
st.write("Upload an image to count the coins.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # Use morphological operations to enhance the edges
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(blurred, cv2.MORPH_CLOSE, kernel)

    # Detect circles using HoughCircles
    circles = cv2.HoughCircles(morph, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                               param1=100, param2=30, minRadius=20, maxRadius=100)

    coin_count = 0
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        coin_count = len(circles)

        for (x, y, r) in circles:
            cv2.circle(img_array, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(img_array, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    cv2.putText(img_array, f"Coins: {coin_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    st.image(img_array, caption='Processed Image', use_column_width=True)
    st.write(f"Number of coins detected: {coin_count}")
