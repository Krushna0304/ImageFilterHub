import streamlit as st
import sys
from pathlib import Path

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from filters import histogram
from utils.io_utils import load_image
from utils.plot_utils import show_side_by_side, plot_histogram

def run(uploaded_file):
    st.title("📊 Histogram Processing")
   
    if uploaded_file:
        gray = load_image(uploaded_file, as_gray=True)

        option = st.selectbox(
            "Choose an operation",
            ["Image Histogram", "Histogram Equalization", "CLAHE"]
        )

        if option == "Image Histogram":
            hist = histogram.compute_histogram(gray)
            plot_histogram(gray, hist, title="Image Histogram", width=10, height=5)


        elif option == "Histogram Equalization":
            eq_img = histogram.histogram_equalization(gray)
            show_side_by_side(gray, eq_img, caption1="Original", caption2="Equalized")

        elif option == "CLAHE":
            clahe_img = histogram.clahe_equalization(gray, clip_limit=2.0, tile_grid_size=(8, 8))
            show_side_by_side(gray, clahe_img, caption1="Original", caption2="CLAHE")
    else:
        st.warning("Please upload an image to proceed.")
