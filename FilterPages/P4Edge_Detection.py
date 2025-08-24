import streamlit as st
import sys
from pathlib import Path

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from utils.io_utils import load_image, save_image
from utils.plot_utils import show_side_by_side
from filters import edge_detection
from filter_descriptions.edge_detection_desc import (
    sobel_filter_info, prewitt_filter_info, laplacian_filter_info, canny_filter_info,
)


def run(uploaded_file):
    st.title("✂️ Edge Detection")

    if uploaded_file:
        gray = load_image(uploaded_file, as_gray=True)

        option = st.selectbox(
            "Choose an Edge Detection Method",
            ["Sobel", "Prewitt", "Laplacian", "Canny"]
        )

        if option == "Sobel":
            edges = edge_detection.sobel_edge_detection(gray)
            show_side_by_side(gray, edges, caption1="Original", caption2="Sobel")
            sobel_filter_info()

        elif option == "Prewitt":
            edges = edge_detection.prewitt_edge_detection(gray)
            show_side_by_side(gray, edges, caption1="Original", caption2="Prewitt")
            prewitt_filter_info()

        elif option == "Laplacian":
            edges = edge_detection.laplacian_edge_detection(gray)
            show_side_by_side(gray, edges, caption1="Original", caption2="Laplacian")
            laplacian_filter_info()

        elif option == "Canny":
            edges = edge_detection.canny_edge_detection(gray)
            show_side_by_side(gray, edges, caption1="Original", caption2="Canny")
            canny_filter_info()

        save_option = st.checkbox("Save Result")
        if save_option:
            save_image(edges, "edges_output.png")
            st.success("✅ Image saved as edges_output.png")

    else:
        st.warning("Please upload an image to proceed.")
