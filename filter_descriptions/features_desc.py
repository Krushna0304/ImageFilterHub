import streamlit as st  
def harris_corner_info():
    st.markdown(r"""
    ### 📌 Harris Corner Detector
    - **Concept:** Finds corners where intensity changes sharply in two directions.  
    - **Math:** Based on **structure tensor (M)**  

    $$
    M = \begin{bmatrix}
    I_x^2 & I_x I_y \\
    I_x I_y & I_y^2
    \end{bmatrix}
    $$

    - **Corner Response Function:**  

    $$
    R = \det(M) - k \cdot (\text{trace}(M))^2
    $$

    - **Steps:**  
        1. Compute image gradients.  
        2. Build matrix **M** from gradients.  
        3. Compute corner response function (R).  
        4. Threshold R → mark corners.  

    - **Usage:** Detects corners for object tracking & alignment.
    """)


def shi_tomasi_info():
    st.markdown(r"""
    ### 📌 Shi-Tomasi Corner Detector
    - **Concept:** Improvement of Harris → more stable & accurate.  
    - **Math:** Uses **minimum eigenvalue** ($\lambda_{min}$) of M instead of R.  

    $$
    \lambda_{min} = \min(\lambda_1, \lambda_2)
    $$

    - **Steps:**  
        1. Compute gradients.  
        2. Form matrix M.  
        3. Find minimum eigenvalue.  
        4. If $\lambda_{min}$ > threshold → corner.  

    - **Usage:** Basis of **Good Features to Track** (used in optical flow tracking).
    """)


def sift_info():
    st.markdown(r"""
    ### 📌 SIFT (Scale-Invariant Feature Transform)
    - **Concept:** Detects keypoints robust to **scale, rotation & illumination changes**.  

    - **Math:** Scale-space representation with Gaussian filter:  

    $$
    L(x,y,\sigma) = G(x,y,\sigma) * I(x,y)
    $$

    - **Difference of Gaussians (DoG):**  

    $$
    D(x,y,\sigma) = L(x,y,k\sigma) - L(x,y,\sigma)
    $$

    - **Steps:**  
        1. Build scale-space with Gaussian filters.  
        2. Detect extrema using DoG.  
        3. Localize keypoints.  
        4. Assign orientation.  
        5. Generate **128-D feature descriptor vector**.  

    - **Usage:** Object recognition, image stitching, tracking.  
    - **Note:** Originally patented, now open-source.
    """)


def fast_info():
    st.markdown(r"""
    ### 📌 FAST (Features from Accelerated Segment Test)
    - **Concept:** Very **fast corner detection** algorithm.  

    - **Math Rule:**  
    For each pixel $p$, consider 16 surrounding pixels.  
    If **N contiguous pixels** are brighter than $I_p + t$ or darker than $I_p - t$, → corner.  

    $$
    \text{Corner}(p) = 
    \begin{cases}
    1 & \text{if ≥ N contiguous pixels satisfy condition} \\
    0 & \text{otherwise}
    \end{cases}
    $$

    - **Steps:**  
        1. Check intensity of 16-circle neighbors.  
        2. Apply threshold condition.  
        3. Mark as corner if satisfied.  

    - **Advantages:** Extremely fast → real-time apps.  
    - **Limitations:** No scale/rotation invariance.  
    - **Usage:** Mobile vision, robotics.
    """)


def orb_info():
    st.markdown(r"""
    ### 📌 ORB (Oriented FAST and Rotated BRIEF)
    - **Concept:** Combines **FAST detector + BRIEF descriptor**, adds rotation invariance.  

    - **Math (Orientation):**  

    $$
    \theta = \arctan \left(\frac{m_{01}}{m_{10}}\right)
    $$

    where  
    $m_{pq} = \sum_x \sum_y x^p y^q I(x,y)$  

    - **Steps:**  
        1. Detect keypoints using FAST.  
        2. Compute orientation using image moments.  
        3. Extract **BRIEF binary descriptors**.  

    - **Advantages:**  
        - Fast, efficient, free alternative to SIFT/SURF.  
        - Robust to rotation, noise, and lighting changes.  
    - **Usage:** SLAM, AR, real-time object recognition.
    """)
