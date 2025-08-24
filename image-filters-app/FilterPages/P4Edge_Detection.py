from pathlib import Path
import sys
import streamlit as st

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from utils.io_utils import load_image, save_image
from filters.edge_detection import sobel_edge_detection, prewitt_edge_detection, laplacian_edge_detection, canny_edge_detection

def run(uploaded_file):
    st.title("✂️ Edge Detection")

    st.write("Select an image to apply edge detection techniques.")


    if uploaded_file is not None:
        image = load_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        st.write("Choose an edge detection method:")
        method = st.selectbox("Select Method", ["Sobel", "Prewitt", "Laplacian", "Canny"])

        if st.button("Apply"):
            if method == "Sobel":
                edges = sobel_edge_detection(image)
            elif method == "Prewitt":
                edges = prewitt_edge_detection(image)
            elif method == "Laplacian":
                edges = laplacian_edge_detection(image)
            elif method == "Canny":
                edges = canny_edge_detection(image)

            st.image(edges, caption=f"{method} Edge Detection", use_column_width=True)
            save_option = st.checkbox("Save Result")
            if save_option:
                save_image(edges, "edges_output.png")
                st.success("Image saved as edges_output.png")
    else:
        st.warning("Please upload an image to proceed.")