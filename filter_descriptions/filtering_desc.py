import streamlit as st

def mean_filter_info():
    st.markdown(r"""
    ### 📌 Mean / Box Filter
    - **Concept:** Each pixel is replaced by the average of its neighborhood.  
    - **Kernel:** Uniform, usually 3×3, 5×5, or 7×7.  
    - **Formula:**  
      $$
      g(x,y) = \frac{1}{mn} \sum_{i=-a}^{a}\sum_{j=-b}^{b} f(x+i,y+j)
      $$
    - **Steps:**  
        1. Choose kernel size (odd, e.g., 3×3).  
        2. Slide kernel across the image.  
        3. Replace center pixel with neighborhood mean.  
    - **Usage:** Basic smoothing, reduces random noise but blurs edges.
    """)

def gaussian_filter_info():
    st.markdown(r"""
    ### 📌 Gaussian Filter
    - **Concept:** Weighted average based on Gaussian distribution.  
    - **Kernel:** Defined by standard deviation (σ).  
    - **Formula:**  
      $$
      G(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}
      $$
    - **Steps:**  
        1. Define kernel size & σ.  
        2. Compute Gaussian weights.  
        3. Convolve with the image.  
    - **Usage:** Smooths while preserving edges better than mean filter.
    """)

def median_filter_info():
    st.markdown(r"""
    ### 📌 Median Filter
    - **Concept:** Replaces each pixel with the **median** of its neighborhood.  
    - **Kernel Size:** 3×3, 5×5 (odd).  
    - **Steps:**  
        1. Take neighborhood values.  
        2. Sort them.  
        3. Replace center with the median.  
    - **Usage:** Excellent for removing **salt & pepper noise**.
    """)

def bilateral_filter_info():
    st.markdown(r"""
    ### 📌 Bilateral Filter
    - **Concept:** Combines spatial + intensity similarity → smooths while preserving edges.  
    - **Formula:**  
      $$
      I_{filtered}(x) = \frac{1}{W_p} \sum_{x_i} I(x_i)\, f_r(\|I(x_i)-I(x)\|)\, f_s(\|x_i-x\|)
      $$
      - $f_s$: spatial Gaussian (distance)  
      - $f_r$: range Gaussian (intensity)  
    - **Steps:**  
        1. Choose spatial σ (neighborhood size).  
        2. Choose range σ (intensity sensitivity).  
        3. Apply weighted averaging.  
    - **Usage:** Noise reduction **without blurring edges**.
    """)

def high_pass_filter_info():
    st.markdown(r"""
    ### 📌 High-Pass Filter (Sharpening)
    - **Concept:** Enhances fine details and edges by highlighting high frequencies.  
    - **Kernel Example (3×3 Laplacian):**  
      $$
      \begin{bmatrix}
      -1 & -1 & -1 \\
      -1 & 8  & -1 \\
      -1 & -1 & -1
      \end{bmatrix}
      $$
    - **Steps:**  
        1. Convolve image with high-pass kernel.  
        2. Enhance edges and details.  
    - **Usage:** Edge detection, sharpening details.
    """)

def low_pass_filter_info():
    st.markdown(r"""
    ### 📌 Low-Pass Filter (Blurring)
    - **Concept:** Suppresses high frequencies → smoothens image.  
    - **Kernel Example (3×3 Mean):**  
      $$
      \frac{1}{9}
      \begin{bmatrix}
      1 & 1 & 1 \\
      1 & 1 & 1 \\
      1 & 1 & 1
      \end{bmatrix}
      $$
    - **Steps:**  
        1. Convolve with low-pass kernel.  
        2. Output appears blurred.  
    - **Usage:** Noise removal, background smoothing.
    """)
def high_boost_filter_info():
    st.markdown(r"""
    ### 🔹 High-Boost Filtering
    - **Purpose:** Enhances fine details and edges while retaining low-frequency components.  
      It is an extension of the high-pass filter, where part of the original image is added back.  

    - **Formula:**  
      $$
      g(x,y) = A \cdot f(x,y) - f_{LP}(x,y)
      $$
      where:  
      - $f(x,y)$ = Original image  
      - $f_{LP}(x,y)$ = Low-pass (blurred) version  
      - $A \geq 1$ = Amplification factor  

    - **Cases:**  
        - $A = 1$ → Pure high-pass filtering.  
        - $A > 1$ → High-boost filtering (edges + original details preserved).  

    - **Steps:**  
        1. Apply a Low-Pass Filter (Gaussian/Box) → Get smoothed version.  
        2. Subtract smoothed image from original → Extract high-frequency details.  
        3. Multiply original by $A$ and add high-frequency details back.  

    - **Kernel Example (for A = 1.5):**  
      $$
      \begin{bmatrix}
      0 & -1 & 0 \\
      -1 & 5 & -1 \\
      0 & -1 & 0
      \end{bmatrix}
      $$

    - **Applications:**  
        - Image sharpening.  
        - Enhancing medical/scientific images (fine details).  
        - Improving clarity in low-contrast images.  
    """)

