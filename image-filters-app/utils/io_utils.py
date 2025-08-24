import cv2
import numpy as np

def load_image(uploaded_file, as_gray=False):
    """Load an image from the specified file path."""
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    flag = cv2.IMREAD_GRAYSCALE if as_gray else cv2.IMREAD_COLOR
    img = cv2.imdecode(file_bytes, flag)
    return img

def save_image(image, save_path):
    """Save an image to the specified file path."""
    success = cv2.imwrite(save_path, image)
    if not success:
        raise IOError(f"Failed to save image at {save_path}")

def convert_to_grayscale(image):
    """Convert a color image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)