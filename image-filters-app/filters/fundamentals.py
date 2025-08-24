import cv2
import numpy as np
def image_negation(gray_img: np.ndarray) -> np.ndarray:
    """Invert pixel values (Image Negation)."""
    return 255 - gray_img


def thresholding(gray_img: np.ndarray, thresh: int = 127) -> np.ndarray:
    """Simple Binary Thresholding."""
    _, binary_img = cv2.threshold(gray_img, thresh, 255, cv2.THRESH_BINARY)
    return binary_img


def gray_level_slicing(gray_img: np.ndarray, lower: int = 100, upper: int = 200) -> np.ndarray:
    """Highlight intensities between given lower & upper bounds."""
    sliced = np.where((gray_img > lower) & (gray_img < upper), 255, gray_img)
    return sliced.astype(np.uint8)


def bit_plane_slicing(gray_img: np.ndarray) -> list:
    """Generate 8 bit-planes of the image."""
    bit_planes = []
    for i in range(8):
        plane = np.bitwise_and(gray_img, 1 << i)
        bit_planes.append(plane)
    return bit_planes


def darken_image(gray_img: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    """
    Darken the image.
    alpha < 1 -> darkens image
    """
    return cv2.convertScaleAbs(gray_img, alpha=alpha, beta=0)


def lighten_image(gray_img: np.ndarray, alpha: float = 1.5, beta: int = 30) -> np.ndarray:
    """
    Lighten the image.
    alpha > 1 and positive beta -> brightens image
    """
    return cv2.convertScaleAbs(gray_img, alpha=alpha, beta=beta)