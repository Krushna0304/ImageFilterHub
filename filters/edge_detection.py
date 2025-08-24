import cv2
import numpy as np
def sobel_edge_detection(gray_image):
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_magnitude = np.uint8(np.clip(sobel_magnitude, 0, 255))

    return sobel_magnitude

def prewitt_edge_detection(gray_image):
    kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    
    prewitt_x = cv2.filter2D(gray_image, -1, kernel_x)
    prewitt_y = cv2.filter2D(gray_image, -1, kernel_y)
    prewitt_magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)
    prewitt_magnitude = np.uint8(np.clip(prewitt_magnitude, 0, 255))

    return prewitt_magnitude

def roberts_edge_detection(gray_image):
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    
    roberts_x = cv2.filter2D(gray_image, -1, kernel_x)
    roberts_y = cv2.filter2D(gray_image, -1, kernel_y)
    roberts_magnitude = np.sqrt(roberts_x**2 + roberts_y**2)
    roberts_magnitude = np.uint8(np.clip(roberts_magnitude, 0, 255))

    return roberts_magnitude

def laplacian_edge_detection(gray_image):
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    laplacian_magnitude = cv2.convertScaleAbs(laplacian)

    return laplacian_magnitude

def canny_edge_detection(gray_image, threshold1=100, threshold2=200):
    canny_edges = cv2.Canny(gray_image, threshold1, threshold2)

    return canny_edges