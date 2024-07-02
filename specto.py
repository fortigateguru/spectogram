import streamlit as st
import cv2
import numpy as np
from PIL import Image

def apply_filter(image, filter_name):
    # Convert PIL Image to numpy array
    image_np = np.array(image)
    
    # Convert RGB to BGR (OpenCV uses BGR)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    if filter_name == "Grayscale":
        filtered = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    elif filter_name == "Blur":
        filtered = cv2.GaussianBlur(image_bgr, (15, 15), 0)
    elif filter_name == "Edge Detection":
        filtered = cv2.Canny(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY), 100, 200)
    elif filter_name == "Sepia":
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        filtered = cv2.transform(image_bgr, sepia_filter)
    else:
        filtered = image_bgr
    
    # Convert back to RGB for displaying
    if len(filtered.shape) == 2:  # If grayscale
        return cv2.cvtColor(filtered, cv2.COLOR_GRAY2RGB)
    else:
        return cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB)

def main():
    st.title("Image Filter App")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        filter_name = st.selectbox(
            "Choose a filter",
            ("Original", "Grayscale", "Blur", "Edge Detection", "Sepia")
        )
        
        filtered_image = apply_filter(image, filter_name)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)
        
        with col2:
            st.subheader(f"{filter_name} Filter")
            st.image(filtered_image, use_column_width=True)

if __name__ == "__main__":
    main()
