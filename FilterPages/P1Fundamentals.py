import streamlit as st
import sys
from pathlib import Path

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from filters import fundamentals
from utils.io_utils import load_image
from utils.plot_utils import show_side_by_side
from utils.plot_utils import show_multiple_images
from filter_descriptions.fundamentals_desc import (
    image_negation_info, thresholding_info, gray_level_slicing_info,
    bit_plane_slicing_info, dark_light_info
)   

def run(uploaded_file):
    st.title("🏞️ Fundamentals & Point Processing")

    if uploaded_file:
        gray = load_image(uploaded_file, as_gray=True)

        option = st.selectbox(
            "Choose an operation",
            ["Image Negation", "Thresholding", "Gray Level Slicing", 
             "Bit-Plane Slicing", "Darken", "Lighten"]
        )

        if option == "Image Negation":
            result = fundamentals.image_negation(gray)
            show_side_by_side(gray, result, caption1="Original", caption2="Negative", channels="GRAY",width=250)
            image_negation_info()

        elif option == "Thresholding":
            result = fundamentals.thresholding(gray, thresh=127)
            show_side_by_side(gray, result, caption1="Original", caption2="Thresholded", channels="GRAY",width=250)
            thresholding_info()

        elif option == "Gray Level Slicing":
            result = fundamentals.gray_level_slicing(gray, 100, 200)
            show_side_by_side(gray, result, caption1="Original", caption2="Gray Level Slicing", channels="GRAY",width=250)
            gray_level_slicing_info()


        elif option == "Bit-Plane Slicing":
            bit_planes = fundamentals.bit_plane_slicing(gray)
            show_multiple_images(*bit_planes, captions=[f"Plane {i}" for i in range(8)], channels="GRAY", width=200, max_cols=4)
            bit_plane_slicing_info()

        elif option == "Darken":
            result = fundamentals.darken_image(gray, alpha=0.5)
            show_side_by_side(gray, result, caption1="Original", caption2="Darkened", channels="GRAY",width=250)
            dark_light_info()

        elif option == "Lighten":
            result = fundamentals.lighten_image(gray, alpha=1.5, beta=30)
            show_side_by_side(gray, result, caption1="Original", caption2="Lightened", channels="GRAY",width=250)
            dark_light_info()
    else:
        st.warning("Please upload an image to proceed.")

if __name__ == "__main__":
    run()
