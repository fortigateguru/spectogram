import streamlit as st
import cv2
import numpy as np
from PIL import Image

def apply_filter(image, filter_name):
    if filter_name == "Grayscale":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_name == "Blur":
        return cv2.GaussianBlur(image, (15, 15), 0)
    elif filter_name == "Edge Detection":
        return cv2.Canny(image, 100, 200)
    elif filter_name == "Sepia":
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        return cv2.transform(image, sepia_filter)
    return image

def main():
    st.title("Image Filter App")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = np.array(image)
        
        filter_name = st.selectbox(
            "Choose a filter",
            ("Original", "Grayscale", "Blur", "Edge Detection", "Sepia")
        )
        
        if filter_name != "Original":
            filtered_image = apply_filter(image, filter_name)
        else:
            filtered_image = image
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Image")
            st.image(image, channels="BGR")
        
        with col2:
            st.subheader(f"{filter_name} Filter")
            st.image(filtered_image, channels="BGR")

if __name__ == "__main__":
    main()
