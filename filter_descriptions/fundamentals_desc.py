import streamlit as st
def image_negation_info():
    st.markdown(r"""
    ### 📌 Image Negation
    - **Concept:** Inverts pixel values, useful for X-rays & medical imaging.  
    - **Formula:**  
      $$
      s = L - 1 - r
      $$
      where \(L\) = number of gray levels, \(r\) = input pixel, \(s\) = output pixel.  
    - **Steps:**  
        1. For each pixel, subtract intensity from maximum (e.g., 255 in 8-bit images).  
        2. Replace pixel with result.  
    - **Usage:** Highlight details in dark regions.  
    """)

def thresholding_info():
    st.markdown(r"""
    ### 📌 Thresholding
    - **Concept:** Converts grayscale image into binary based on a threshold.  
    - **Formula:**  
      $$
      s = 
      \begin{cases} 
      1 & \text{if } r \geq T \\ 
      0 & \text{if } r < T 
      \end{cases}
      $$
      where \(T\) = threshold.  
    - **Steps:**  
        1. Select threshold \(T\).  
        2. Assign pixels above \(T\) to white, below \(T\) to black.  
    - **Usage:** Simple segmentation (e.g., document scanning).  
    """)

def gray_level_slicing_info():
    st.markdown(r"""
    ### 📌 Gray Level Slicing
    - **Concept:** Highlights specific intensity ranges in an image.  
    - **Formula:**  
      Enhances pixels in range \([r_1, r_2]\) while suppressing others.  
    - **Steps:**  
        1. Choose intensity range \([r_1, r_2]\).  
        2. Enhance pixels inside the range.  
        3. Dim or leave unchanged pixels outside range.  
    - **Usage:** Highlight tissues in medical images or specific features.  
    """)

def bit_plane_slicing_info():
    st.markdown(r"""
    ### 📌 Bit-Plane Slicing
    - **Concept:** Decomposes image into binary bit-planes (1–8 for 8-bit images).  
    - **Formula:**  
      $$
      I(x,y) = \sum_{k=0}^{7} b_k(x,y) \cdot 2^k
      $$
      where \(b_k\) = kth bit-plane.  
    - **Steps:**  
        1. Extract each bit-plane separately.  
        2. Reconstruct image by combining planes.  
    - **Usage:** Data compression, watermarking, feature analysis.  
    """)

def dark_light_info():
    st.markdown(r"""
    ### 📌 Darkening & Lightening
    - **Concept:** Adjusts brightness by scaling pixel values.  
    - **Formula:**  
      $$
      s = \alpha r + \beta
      $$
      where \(\alpha\) = contrast factor, \(\beta\) = brightness shift.  
    - **Steps:**  
        1. Multiply pixel values by factor \(\alpha\).  
        2. Add bias \(\beta\) for shifting.  
    - **Usage:** Enhance underexposed or overexposed images.  
    """)
