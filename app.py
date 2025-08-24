import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Image Filters App",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
    .main .block-container {padding-top: 2rem;}
    .stRadio > label {font-weight: bold;}
    div.stButton > button {width: 100%;}
    .css-1v0mbdj.ebxwdo61 {border: none;}
    
 

    /* Sidebar background */
    [data-testid=stSidebar] {
        background: linear-gradient(180deg, #2196f3, #bbdefb) !important;
        padding: 0rem 0.8rem .5rem 0.8rem !important; /* reduce top padding */
    }

            
    /* Make all sidebar text neat */
    [data-testid=stSidebar] * {
        color: #0d1b2a !important;
        font-weight: 500;
    }

    /* Remove Streamlit default nav items/logo */
    [data-testid="stSidebarNav"],
    [data-testid="stSidebarNavItems"],
    [data-testid="stSidebarNavSeparator"],
    [data-testid="stSidebarUserContent"] img {
        display: none !important;
    }

    /* Radio buttons: equal size, white background */
    div[role='radiogroup'] label {
        background: white !important;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 10px;
        color: #2c3e50 !important;
        font-weight: 500;
        cursor: pointer;
        width: 100% !important;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        border: 1px solid #ddd;
        box-sizing: border-box;
    }

    /* Selected radio option */
    div[role='radiogroup'] label[data-selected="true"] {
        background: #2196f3 !important;
        color: white !important;
        font-weight: bold;
        border: 2px solid #1565c0;
    }

    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)



def main():
    # App Header with Logo
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("🖼️ Image Filters App")
        st.markdown("---")
    
    # Sidebar Configuration
    st.sidebar.image("https://img.icons8.com/color/96/000000/photography.png", width=100)
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"],key="fundamentals_file_uploader")
    # Page mapping with emojis
    pages = {
        "🏞️ Fundamentals": "P1Fundamentals",
        "📊 Histogram": "P2Histogram",
        "🎨 Filtering": "P3Filtering",
        "✂️ Edge Detection": "P4Edge_Detection",
        "📍 Feature Detection": "P5Feature_Detection",
        "🏠 Home": None
    }

    # Styled selection
    selection = st.sidebar.radio(
        "Choose a Filter Category",
        list(pages.keys()),
        index=len(pages) - 1
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.info(
        "This application demonstrates various "
        "image processing techniques using Python "
        "and OpenCV."
    )
    
    # Page Navigation
    if "🏞️ Fundamentals" in selection:
        from FilterPages import P1Fundamentals as fundamentals
        fundamentals.run(uploaded_file)
    elif "📊 Histogram" in selection:
        from FilterPages import P2Histogram as histogram
        histogram.run(uploaded_file)
    elif "🎨 Filtering" in selection:
        from FilterPages import P3Filtering as filtering
        filtering.run(uploaded_file)
    elif "✂️ Edge Detection" in selection:
        from FilterPages import P4Edge_Detection as edge_detection
        edge_detection.run(uploaded_file)
    elif "📍 Feature Detection" in selection:
        from FilterPages import P5Feature_Detection as features
        features.run(uploaded_file)
    else:
        # Home page content
        st.markdown("""
        ## Welcome to Image Filters App! 👋
        
        This application provides various image processing tools:
        
        - **🏞️ Fundamentals**: Basic image operations
        - **📊 Histogram**: Histogram analysis and equalization
        - **🎨 Filtering**: Spatial and frequency domain filters
        - **✂️ Edge Detection**: Various edge detection techniques
        - **📍 Feature Detection**: Feature detection algorithms
        
        ### Getting Started
        1. Select a category from the sidebar
        2. Upload an image
        3. Apply different filters and analyze results
        
        ### Need Help?
        Check the sidebar for navigation and additional information.
        """)

if __name__ == "__main__":
    main()
