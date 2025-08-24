import streamlit as st

def image_histogram_info():
    st.markdown(r"""
    ### 📌 Image Histogram
    - **Concept:** A histogram shows the frequency distribution of pixel intensities in an image.  
    - **Definition:** For a grayscale image with intensity levels \(0,1,2,...,L-1\), the histogram is:  
      $$
      h(r_k) = n_k
      $$
      where \(r_k\) = kth intensity level, \(n_k\) = number of pixels with intensity \(r_k\).  
    - **Steps:**  
        1. Count how many pixels fall into each intensity value.  
        2. Plot intensity (x-axis) vs frequency (y-axis).  
    - **Usage:** Analyze image brightness, contrast, and dynamic range.  
    """)

def histogram_equalization_info():
    st.markdown(r"""
    ### 📌 Histogram Equalization (Global Contrast Enhancement)
    - **Concept:** Redistributes pixel intensities to span the entire range → improves global contrast.  
    - **Formula:**  
      $$
      s_k = T(r_k) = \sum_{j=0}^{k} \frac{n_j}{N}
      $$
      where \(N\) = total pixels, \(n_j\) = count of intensity \(j\).  
    - **Steps:**  
        1. Compute histogram of input image.  
        2. Compute **Cumulative Distribution Function (CDF)**.  
        3. Map old pixel values to new intensity values using CDF.  
        4. Generate enhanced image.  
    - **Usage:** Enhances low-contrast images (e.g., medical scans, satellite images).  
    - **Limitation:** May over-enhance noise, doesn’t handle local contrast well.  
    """)

def clahe_info():
    st.markdown(r"""
    ### 📌 Adaptive Histogram Equalization (CLAHE – Contrast Limited AHE)
    - **Concept:** Improves on Histogram Equalization by applying it **locally** on image tiles, preventing over-contrast.  
    - **Steps:**  
        1. Divide image into small tiles (e.g., 8×8).  
        2. Apply histogram equalization on each tile.  
        3. Clip histogram (limit contrast) → avoids noise amplification.  
        4. Interpolate tile boundaries to smooth transitions.  
    - **Usage:** Enhances **local contrast** in images with varying lighting (e.g., medical X-rays, natural images).  
    - **Advantages:** Prevents noise amplification, better for non-uniform illumination.  
    """)
