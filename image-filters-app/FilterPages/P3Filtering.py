import streamlit as st
import sys
from pathlib import Path

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
from filters import filtering
from utils.io_utils import load_image



def run(uploaded_file):
    st.title("🎨 Basic Image Filtering")
   
    if uploaded_file:
        gray = load_image(uploaded_file, as_gray=True)
        option = st.selectbox(
            "Choose a filter",
            ["Mean Filter", "Gaussian Filter", "Median Filter", 
            "Bilateral Filter", "High-Pass Filter", 
            "Low-Pass Filter", "High-Boost Filter"]
        )
        spacer, col1, col2, _ = st.columns([1, 3, 3, .5])
        if option == "Mean Filter":
            result = filtering.mean_filter(gray, ksize=5)
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(gray, caption="Original", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(result, caption="Mean Filter", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)

        elif option == "Gaussian Filter":
            result = filtering.gaussian_filter(gray, ksize=5)
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(gray, caption="Original", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(result, caption="Gaussian Filter", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)

        elif option == "Median Filter":
            result = filtering.median_filter(gray, ksize=5)
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(gray, caption="Original", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(result, caption="Median Filter", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)

        elif option == "Bilateral Filter":
            result = filtering.bilateral_filter(gray, d=9, sigma_color=75, sigma_space=75)
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(gray, caption="Original", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(result, caption="Bilateral Filter", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)

        elif option == "High-Pass Filter":
            result = filtering.high_pass_filter(gray)
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(gray, caption="Original", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(result, caption="High-Pass Filter", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)

        elif option == "Low-Pass Filter":
            result = filtering.low_pass_filter(gray, ksize=15)
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(gray, caption="Original", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(result, caption="Low-Pass Filter", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)

        elif option == "High-Boost Filter":
            result = filtering.high_boost_filter(gray, A=1.5, ksize=5)
            with col1:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(gray, caption="Original", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(result, caption="High-Boost Filter", channels="GRAY", width=250)
                st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("Please upload an image to proceed.")

