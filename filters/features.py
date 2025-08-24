import cv2
import numpy as np


def harris_corners(image, block_size=2, ksize=3, k=0.04):
    """ Harris Corner Detection """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_f = np.float32(gray)

    harris = cv2.cornerHarris(gray_f, blockSize=block_size, ksize=ksize, k=k)
    harris = cv2.dilate(harris, None)  # enhance corners

    harris_img = image.copy()
    harris_img[harris > 0.01 * harris.max()] = [255, 0, 0]  # mark corners in red
    return harris_img


def shi_tomasi_corners(image, max_corners=100, quality_level=0.01, min_distance=10):
    """ Shi-Tomasi Corner Detection """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    shi_tomasi = cv2.goodFeaturesToTrack(
        gray, maxCorners=max_corners, qualityLevel=quality_level, minDistance=min_distance
    )
    shi_tomasi = shi_tomasi.astype(int)

    shi_img = image.copy()
    for pt in shi_tomasi:
        x, y = pt.ravel()
        cv2.circle(shi_img, (x, y), 5, (0, 255, 0), -1)
    return shi_img


def sift_features(image):
    """ SIFT Feature Detection """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    kp, des = sift.detectAndCompute(gray, None)

    sift_img = cv2.drawKeypoints(
        gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )
    return sift_img


def fast_features(image, threshold=30, nonmax_suppression=True):
    """ FAST Feature Detection """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fast = cv2.FastFeatureDetector_create(threshold=threshold, nonmaxSuppression=nonmax_suppression)
    kp = fast.detect(gray, None)

    fast_img = cv2.drawKeypoints(gray, kp, None, color=(255, 0, 0))
    return fast_img


def orb_features(image):
    """ ORB Feature Detection """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(gray, None)

    orb_img = cv2.drawKeypoints(gray, kp, None, color=(0, 255, 0), flags=0)
    return orb_img
