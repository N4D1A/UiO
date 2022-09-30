"""pure Python implementation of image filters"""
import numpy as np
from instapy import io 


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty(shape=image.shape[:2], dtype=np.uint8) 
    # iterate through the pixels, and apply the grayscale transform
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            gray_image[i,j] = image[i,j][0]*0.21+image[i,j][1]*0.72+image[i,j][2]*0.07
            
    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image, dtype=np.uint8) # shape: 3d
    
    # Iterate through the pixels
    # applying the sepia matrix
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            sepia_image[i,j][0] = min(255, image[i][j][0]*0.393+image[i][j][1]*0.769+image[i][j][2]*0.189)
            sepia_image[i,j][1] = min(255, image[i][j][0]*0.349+image[i][j][1]*0.686+image[i][j][2]*0.168)
            sepia_image[i,j][2] = min(255, image[i][j][0]*0.272+image[i][j][1]*0.534+image[i][j][2]*0.131)
    
    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image
