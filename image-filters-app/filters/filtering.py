

import cv2
import numpy as np


def mean_filter(gray_img: np.ndarray, ksize: int = 5) -> np.ndarray:
    """Apply Mean / Box filter with given kernel size."""
    return cv2.blur(gray_img, (ksize, ksize))


def gaussian_filter(gray_img: np.ndarray, ksize: int = 5, sigma: float = 0) -> np.ndarray:
    """Apply Gaussian filter."""
    return cv2.GaussianBlur(gray_img, (ksize, ksize), sigma)


def median_filter(gray_img: np.ndarray, ksize: int = 5) -> np.ndarray:
    """Apply Median filter (good for salt & pepper noise)."""
    return cv2.medianBlur(gray_img, ksize)


def bilateral_filter(gray_img: np.ndarray, d: int = 9, sigma_color: int = 75, sigma_space: int = 75) -> np.ndarray:
    """Apply Bilateral filter (edge-preserving smoothing)."""
    return cv2.bilateralFilter(gray_img, d, sigma_color, sigma_space)


def high_pass_filter(gray_img: np.ndarray) -> np.ndarray:
    """Apply High-Pass sharpening filter using kernel convolution."""
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(gray_img, -1, kernel)


def low_pass_filter(gray_img: np.ndarray, ksize: int = 15) -> np.ndarray:
    """Apply Low-Pass filter (blurring with strong Gaussian)."""
    return cv2.GaussianBlur(gray_img, (ksize, ksize), 0)


def high_boost_filter(gray_img: np.ndarray, A: float = 1.5, ksize: int = 5) -> np.ndarray:
    """
    Apply High-Boost filter.
    A > 1 enhances sharpness while retaining low-frequency info.
    """
    low_pass = cv2.GaussianBlur(gray_img, (ksize, ksize), 0)
    high_boost = cv2.addWeighted(gray_img, A, low_pass, (1 - A), 0)
    return high_boost
