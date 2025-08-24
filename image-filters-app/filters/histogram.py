# filters/histogram.py
import cv2
import numpy as np


def compute_histogram(gray_img: np.ndarray, bins: int = 256, range_vals: tuple = (0, 256)) -> np.ndarray:
    """
    Compute histogram of a grayscale image.
    
    Returns: histogram array
    """
    hist = cv2.calcHist([gray_img], [0], None, [bins], range_vals)
    return hist


def histogram_equalization(gray_img: np.ndarray) -> np.ndarray:
    """
    Perform global Histogram Equalization.
    Improves contrast by redistributing pixel intensities.
    """
    return cv2.equalizeHist(gray_img)


def clahe_equalization(gray_img: np.ndarray, clip_limit: float = 2.0, tile_grid_size: tuple = (8, 8)) -> np.ndarray:
    """
    Perform CLAHE (Contrast Limited Adaptive Histogram Equalization).
    Enhances local contrast.
    """
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    return clahe.apply(gray_img)
