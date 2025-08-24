import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

def display_image(image, title='Image'):
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_comparison(original, processed, original_title='Original Image', processed_title='Processed Image'):
    plt.figure(figsize=(15, 7))
    
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title(original_title)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(processed, cmap='gray')
    plt.title(processed_title)
    plt.axis('off')
    
    plt.show()

def plot_histogram(image, hist, title="Histogram", width=8, height=4):
    """
    Display an image and its histogram side by side in Streamlit.
    
    Args:
        image: The input grayscale image.
        hist: Histogram array of the image.
        title: Title for the histogram plot.
        width: Width of the histogram figure in inches.
        height: Height of the histogram figure in inches.
    """
    # Show the image
    st.image(image, caption="Original Image", channels="GRAY", width=250)
    
    # Plot histogram
    fig, ax = plt.subplots(figsize=(width, height))
    ax.plot(hist.flatten(), color='black')
    ax.set_title(title)
    ax.set_xlabel("Pixel Intensity")
    ax.set_ylabel("Frequency")
    ax.grid(True)
    
    st.pyplot(fig)

def show_side_by_side(original, result, caption1="Original", caption2="Result", channels="GRAY", width=250):
    spacer, col1, col2, _ = st.columns([1, 3, 3, .5])
    with col1:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(original, caption=caption1, channels=channels, width=width)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(result, caption=caption2, channels=channels, width=width)
        st.markdown("</div>", unsafe_allow_html=True)

def show_multiple_images(*images, captions=None, channels="RGB", width=200, max_cols=4, spacer_width=0.1):
    """
    Display multiple images side by side in Streamlit with a left spacer.
    
    Parameters:
        *images: variable number of images (numpy arrays or PIL Images)
        captions: list of captions for each image (default None)
        channels: 'RGB' or 'GRAY'
        width: width of each image in pixels
        max_cols: max number of columns in a row (wraps if more)
        spacer_width: fraction of space for the left spacer (0-1)
    """
    if captions is None:
        captions = [""] * len(images)

    for i in range(0, len(images), max_cols):
        n_cols = min(max_cols, len(images) - i)
        # Add one extra column for left spacer
        cols = st.columns([spacer_width] + [1]*n_cols)
        for col, img, cap in zip(cols[1:], images[i:i+max_cols], captions[i:i+max_cols]):
            with col:
                st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                st.image(img, caption=cap, channels=channels, width=width)
                st.markdown("</div>", unsafe_allow_html=True)
