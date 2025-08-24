from pathlib import Path
import sys
import streamlit as st
import cv2
import numpy as np

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
from filters.features import harris_corners, shi_tomasi_corners, sift_features, fast_features, orb_features

def run(uploaded_file):
    st.title("Feature Detection Techniques")

    st.write("This page demonstrates various feature detection techniques.")

    if uploaded_file is not None:
        # Read the image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        st.image(image, channels="BGR", caption="Uploaded Image", use_column_width=True)

        # Feature Detection Options
        st.subheader("Select Feature Detection Method")
        method = st.selectbox("Choose a method:", ["Harris Corners", "Shi-Tomasi Corners", "SIFT", "FAST", "ORB"])

        if st.button("Detect Features"):
            if method == "Harris Corners":
                corners = harris_corners(image)
                st.image(corners, channels="BGR", caption="Harris Corners", use_column_width=True)
            elif method == "Shi-Tomasi Corners":
                corners = shi_tomasi_corners(image)
                st.image(corners, channels="BGR", caption="Shi-Tomasi Corners", use_column_width=True)
            elif method == "SIFT":
                keypoints = sift_features(image)
                st.image(keypoints, channels="BGR", caption="SIFT Features", use_column_width=True)
            elif method == "FAST":
                keypoints = fast_features(image)
                st.image(keypoints, channels="BGR", caption="FAST Features", use_column_width=True)
            elif method == "ORB":
                keypoints = orb_features(image)
                st.image(keypoints, channels="BGR", caption="ORB Features", use_column_width=True)
        else:
            st.warning("Please upload an image to proceed.")