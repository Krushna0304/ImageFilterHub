import streamlit as st

def sobel_filter_info():
    st.markdown(r"""
    ### 📌 Sobel Filter
    - **Concept:** Detects edges by computing gradient in **x** and **y** directions.  
    - **Kernels:**  
      $$
      G_x =
      \begin{bmatrix}
      -1 & 0 & +1 \\
      -2 & 0 & +2 \\
      -1 & 0 & +1
      \end{bmatrix}, \quad
      G_y =
      \begin{bmatrix}
      -1 & -2 & -1 \\
       0 &  0 &  0 \\
      +1 & +2 & +1
      \end{bmatrix}
      $$
    - **Gradient Magnitude:**  
      $$
      G = \sqrt{G_x^2 + G_y^2}
      $$
    - **Steps:**  
        1. Convolve image with $G_x$ and $G_y$.  
        2. Compute gradient magnitude and direction.  
    - **Usage:** Finds **horizontal & vertical edges**.
    """)

def prewitt_filter_info():
    st.markdown(r"""
    ### 📌 Prewitt Filter
    - **Concept:** Similar to Sobel but simpler approximation.  
    - **Kernels:**  
      $$
      G_x =
      \begin{bmatrix}
      -1 & 0 & +1 \\
      -1 & 0 & +1 \\
      -1 & 0 & +1
      \end{bmatrix}, \quad
      G_y =
      \begin{bmatrix}
      -1 & -1 & -1 \\
       0 &  0 &  0 \\
      +1 & +1 & +1
      \end{bmatrix}
      $$
    - **Gradient Magnitude:**  
      $$
      G = \sqrt{G_x^2 + G_y^2}
      $$
    - **Steps:**  
        1. Convolve with $G_x$, $G_y$.  
        2. Combine to detect edges.  
    - **Usage:** Edge detection with **less computation** than Sobel.
    """)

def roberts_filter_info():
    st.markdown(r"""
    ### 📌 Roberts Cross Operator
    - **Concept:** Detects **diagonal edges** using 2×2 kernels.  
    - **Kernels:**  
      $$
      G_x =
      \begin{bmatrix}
      +1 & 0 \\
       0 & -1
      \end{bmatrix}, \quad
      G_y =
      \begin{bmatrix}
       0 & +1 \\
      -1 &  0
      \end{bmatrix}
      $$
    - **Gradient Magnitude:**  
      $$
      G = \sqrt{G_x^2 + G_y^2}
      $$
    - **Steps:**  
        1. Apply $G_x$, $G_y$ filters.  
        2. Combine to get edge map.  
    - **Usage:** Useful for **fast edge detection** in low-resolution images.
    """)

def laplacian_filter_info():
    st.markdown(r"""
    ### 📌 Laplacian Filter
    - **Concept:** Uses **second derivative** to detect edges (all directions).  
    - **Kernel Example:**  
      $$
      \begin{bmatrix}
       0 & -1 &  0 \\
      -1 &  4 & -1 \\
       0 & -1 &  0
      \end{bmatrix}
      $$
    - **Formula:**  
      $$
      \nabla^2 f(x,y) = 
      \frac{\partial^2 f}{\partial x^2} +
      \frac{\partial^2 f}{\partial y^2}
      $$
    - **Steps:**  
        1. Convolve image with Laplacian kernel.  
        2. Detect **sharp intensity changes**.  
    - **Usage:** Captures **all edge directions** but sensitive to noise.
    """)

def canny_filter_info():
    st.markdown(r"""
    ### 📌 Canny Edge Detector
    - **Concept:** Multi-stage edge detection for **optimal results**.  
    - **Steps:**  
        1. Apply Gaussian filter (noise reduction).  
        2. Compute gradient using Sobel.  
        3. Non-maximum suppression (thin edges).  
        4. Double thresholding (strong & weak edges).  
        5. Edge tracking by hysteresis.  
    - **Formulas:**  
        - Gradient magnitude:  
        $$
        G = \sqrt{G_x^2 + G_y^2}
        $$
        - Gradient direction:  
        $$
        \theta = \tan^{-1}\left(\frac{G_y}{G_x}\right)
        $$
    - **Usage:** Most widely used for **robust edge detection**.
    """)
