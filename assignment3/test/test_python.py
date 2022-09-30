from instapy.python_filters import python_color2gray, python_color2sepia
import numpy as np 
import numpy.testing as nt
import random 


def test_color2gray(image):
    """Test whether the applied result of python_color2gray 
    is the same as the expected gray scale image

    Args:
        image (np.array): 3D

    Returns:
        None

    check that the result has the right shape, type
    assert uniform values
    """
    # run color2gray
    gray_image = python_color2gray(image)

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
    gray_image_samples =[gray_image[i,j] for i, j in zip(i_list, j_list)]
    new_gray_image_samples = np.asarray([
                            image[i,j][0]*0.21+image[i,j][1]*0.72+image[i,j][2]*0.07 
                            for i, j in zip(i_list, j_list)]).astype(np.uint8)
    nt.assert_allclose(gray_image_samples, new_gray_image_samples)

    ## (2) verify all pixels
    new_gray_image = np.empty(shape=image.shape[:2], dtype=np.uint8) 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            new_gray_image[i,j] = image[i,j][0]*0.21+image[i,j][1]*0.72+image[i,j][2]*0.07
    nt.assert_allclose(gray_image, new_gray_image)
    

def test_color2sepia(image):
    """Test whether the applied result of python_color2sepia
    is the same as the expected sepia tone image

    Args:
        image (np.array): 3D

    Returns:
        None

    check that the result has the right shape, type
    assert uniform values
    """
    # run color2sepia
    sepia_image = python_color2sepia(image)
    
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
    new_sepia_image_samples = np.asarray([
                            np.asarray([
                            min(255, image[i][j][0]*0.393+image[i][j][1]*0.769+image[i][j][2]*0.189),
                            min(255, image[i][j][0]*0.349+image[i][j][1]*0.686+image[i][j][2]*0.168),
                            min(255, image[i][j][0]*0.272+image[i][j][1]*0.534+image[i][j][2]*0.131)
                            ])
                            for i, j in zip(i_list, j_list)]).astype(np.uint8)
    nt.assert_allclose(sepia_image_samples, new_sepia_image_samples)

    ## (2) verify all pixels
    new_sepia_image = np.empty_like(image, dtype=np.uint8) # shape: 3d   
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            new_sepia_image[i,j][0] = min(255, image[i][j][0]*0.393+image[i][j][1]*0.769+image[i][j][2]*0.189)
            new_sepia_image[i,j][1] = min(255, image[i][j][0]*0.349+image[i][j][1]*0.686+image[i][j][2]*0.168)
            new_sepia_image[i,j][2] = min(255, image[i][j][0]*0.272+image[i][j][1]*0.534+image[i][j][2]*0.131)
    nt.assert_allclose(sepia_image, new_sepia_image)
