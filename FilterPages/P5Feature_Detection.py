import streamlit as st
import sys
from pathlib import Path

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from utils.io_utils import load_image, save_image
from utils.plot_utils import show_side_by_side
from filters import features
from filter_descriptions.features_desc import (
    harris_corner_info, shi_tomasi_info, sift_info, fast_info, orb_info
)

def run(uploaded_file):
    st.title("✨ Feature Detection")

    if uploaded_file:
        image = load_image(uploaded_file)

        option = st.selectbox(
            "Choose a Feature Detection Method",
            ["Harris Corners", "Shi-Tomasi Corners", "SIFT", "FAST", "ORB"]
        )

        if option == "Harris Corners":
            result = features.harris_corners(image)
            show_side_by_side(image, result, caption1="Original", caption2="Harris Corners")
            harris_corner_info()

        elif option == "Shi-Tomasi Corners":
            result = features.shi_tomasi_corners(image)
            show_side_by_side(image, result, caption1="Original", caption2="Shi-Tomasi Corners")
            shi_tomasi_info()

        elif option == "SIFT":
            result = features.sift_features(image)
            show_side_by_side(image, result, caption1="Original", caption2="SIFT Features")
            sift_info()

        elif option == "FAST":
            result = features.fast_features(image)
            show_side_by_side(image, result, caption1="Original", caption2="FAST Features")
            fast_info()

        elif option == "ORB":
            result = features.orb_features(image)
            show_side_by_side(image, result, caption1="Original", caption2="ORB Features")
            orb_info()
            
        save_option = st.checkbox("Save Result")
        if save_option:
            save_image(result, "features_output.png")
            st.success("✅ Image saved as features_output.png")

    else:
        st.warning("Please upload an image to proceed.")
