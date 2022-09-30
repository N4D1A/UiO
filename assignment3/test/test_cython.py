from instapy.cython_filters import cython_color2gray, cython_color2sepia
import numpy as np 
import numpy.testing as nt
import random 


def test_color2gray(image, reference_gray):
    """Test whether the applied result of cython_color2gray 
    is the same as the reference gray image

    Args:
        image (np.array): 3D
        reference_gray (np.array) : 2D

    Returns:
        None

    check that the result has the right shape, type
    assert uniform values
    """
    # run color2gray
    gray_image = cython_color2gray(image)

    # check that the result has the right shape, type
    assert gray_image.shape == image.shape[:2]
    assert len(gray_image.shape) == 2
    assert gray_image.dtype == np.uint8
    assert isinstance(gray_image, np.ndarray) 

    # assert uniform values (you can comment out either (1) or (2))
    ## (1) verify some individual pixel samples
    sample_num = 100
    i_list = random.sample(range(0,image.shape[0]), sample_num) 
    j_list = random.sample(range(0,image.shape[1]), sample_num)     
    sepia_image_samples =[gray_image[i,j] for i, j in zip(i_list, j_list)]
    ref_sepia_image_samples =[reference_gray[i,j] for i, j in zip(i_list, j_list)]
    nt.assert_allclose(sepia_image_samples, ref_sepia_image_samples)

    ## (2) verify all pixels
    nt.assert_allclose(gray_image, reference_gray)


def test_color2sepia(image, reference_sepia):
    """Test whether the applied result of cython_color2sepia 
    is the same as the reference sepia image

    Args:
        image (np.array): 3D
        reference_sepia (np.array): 3D

    Returns:
        None

    check that the result has the right shape, type
    assert uniform values
    """
    # run color2sepia
    sepia_image = cython_color2sepia(image)
    
    # check that the result has the right shape, type
    assert sepia_image.shape == image.shape
    assert len(sepia_image.shape) == 3
    assert sepia_image.dtype == np.uint8
    assert isinstance(sepia_image, np.ndarray) 
    
    # assert uniform values (you can comment out either (1) or (2))
    ## (1) verify some individual pixel samples
    sample_num = 100
    i_list = random.sample(range(0,image.shape[0]), sample_num) 
    j_list = random.sample(range(0,image.shape[1]), sample_num)     
    sepia_image_samples =[sepia_image[i,j] for i, j in zip(i_list, j_list)]
    ref_sepia_image_samples =[reference_sepia[i,j] for i, j in zip(i_list, j_list)]
    nt.assert_allclose(sepia_image_samples, ref_sepia_image_samples)

    ## (2) verify all pixels
    nt.assert_allclose(sepia_image, reference_sepia)
