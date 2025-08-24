# Image Filters App

This project is a Streamlit application designed for image processing and filtering. It provides a user-friendly interface to apply various image processing techniques, including fundamental operations, histogram processing, filtering, edge detection, and feature detection.

## Project Structure

```
image-filters-app/
├── app.py                         # Main Streamlit app entry point
├── requirements.txt               # Python dependencies (streamlit, opencv, numpy, etc.)
├── README.md                      # Project documentation
│
├── assets/                        # Store sample/test images
│   └── sample.jpg
│
├── utils/                         # Helper functions
│   ├── __init__.py
│   ├── io_utils.py               # Image loading, saving, conversion functions
│   ├── plot_utils.py             # Histogram plotting, visualization helpers
│
├── filters/                       # Organized by categories
│   ├── __init__.py
│   ├── fundamentals.py           # Negation, Thresholding, Gray-level slicing, etc.
│   ├── histogram.py              # Histogram processing & equalization
│   ├── filtering.py              # Mean, Gaussian, Median, Bilateral, etc.
│   ├── edge_detection.py         # Sobel, Prewitt, Roberts, Laplacian, Canny
│   ├── features.py               # Harris, Shi-Tomasi, SIFT, FAST, ORB
│
├── FilterPages/                         # Streamlit multipage support
│   ├── P1Fundamentals.py
│   ├── P2Histogram.py
│   ├── P3Filtering.py
│   ├── P4Edge_Detection.py
│   ├── P5Feature_Detection.py
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone P1
   cd image-filters-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run app.py
```

Once the application is running, you can navigate through the various pages to explore different image processing techniques.

## Features

- **Fundamentals**: Apply basic image processing techniques such as negation, thresholding, and gray-level slicing.
- **Histogram Processing**: Visualize and manipulate image histograms.
- **Filtering**: Use various filtering techniques including mean, Gaussian, median, and bilateral filtering.
- **Edge Detection**: Detect edges in images using methods like Sobel, Prewitt, Roberts, Laplacian, and Canny.
- **Feature Detection**: Identify features in images using techniques such as Harris, Shi-Tomasi, SIFT, FAST, and ORB.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.