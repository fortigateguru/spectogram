import streamlit as st
import cv2
import numpy as np
from PIL import Image

def detect_coins(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Morphological operations to close gaps in edges
    kernel = np.ones((5,5), np.uint8)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    
    # Detect circles
    circles = cv2.HoughCircles(closed, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                               param1=50, param2=30, minRadius=20, maxRadius=300)
    
    return circles

st.title("Improved Coin Counter App")
st.write("Upload an image to count the coins.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    circles = detect_coins(img_array)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        coin_count = len(circles)

        for (x, y, r) in circles:
            cv2.circle(img_array, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(img_array, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        cv2.putText(img_array, f"Coins: {coin_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        st.image(img_array, caption='Processed Image', use_column_width=True)
        st.write(f"Number of coins detected: {coin_count}")
    else:
        st.write("No coins detected. Try adjusting the parameters.")

# Add sliders for parameter tuning
st.sidebar.header("Parameter Tuning")
min_dist = st.sidebar.slider("Min Distance", 30, 100, 50)
param1 = st.sidebar.slider("Param1", 30, 100, 50)
param2 = st.sidebar.slider("Param2", 10, 100, 30)
min_radius = st.sidebar.slider("Min Radius", 10, 100, 20)
max_radius = st.sidebar.slider("Max Radius", 100, 500, 300)

# Update the HoughCircles parameters
if uploaded_file is not None:
    circles = cv2.HoughCircles(closed, cv2.HOUGH_GRADIENT, dp=1, minDist=min_dist,
                               param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    # ... (rest of the code to display results)
