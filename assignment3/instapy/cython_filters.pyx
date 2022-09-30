"""Cython implementation of filter functions"""

import numpy as np
cimport numpy as np

cpdef np.ndarray[np.uint8_t, ndim=2] cython_color2gray(np.ndarray[np.uint8_t, ndim=3] image):
    """Convert rgb pixel array to grayscale
    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    cdef np.ndarray[np.uint8_t, ndim=2] gray_image 

    gray_image = (image @ [0.21, 0.72, 0.07]).astype(np.uint8) 
    
    return gray_image


cpdef np.ndarray[np.uint8_t, ndim=3] cython_color2sepia(np.ndarray[np.uint8_t, ndim=3] image):
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    cdef np.ndarray[np.uint8_t, ndim=3] sepia_image

    cdef np.ndarray[double, ndim=2] sepia_matrix
    sepia_matrix = np.array([
                    [ 0.393, 0.769, 0.189],
                    [ 0.349, 0.686, 0.168],
                    [ 0.272, 0.534, 0.131]])

    sepia_image = np.empty_like(image, dtype=np.uint8) 
    sepia_image = np.vectorize(min)(255,(image @ sepia_matrix.T)).astype(np.uint8) 

    return sepia_image
