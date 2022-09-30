# Instapy

A python package to turn an image into a gray image or a sepia image

## Description

This package provides a gray filter that converts an image to grayscale and a sepia filter that converts an image to a sepia tone. You can also test filters by different implementations, all with the same result.

- Filters: gray, sepia
- Implementations: Python, NumPy, Numba, Cython
- Image resizing (optional)
- Saving the result to a file (optional)
- Runtime measurement (optional)

## Installation
1. Download the package.
2. Install from the unzipped package using:
```bash
python -m pip install .
```

## Usage
### 1. Command-line interface

Pass arguments to the instapy filter functions using command-line interface:
```bash
# option 1
python3 -m instapy <arguments>
# or option 2
instapy <arguments>
```
#### Arguments
```bash
positional arguments:
  file                  filename to apply filter to

options:
  -h, --help            show this help message and exit
  -o , --out            output filename with selected filter applied
  -g, --gray            select gray filter (flag)
  -se, --sepia          select sepia filter (flag)
  -i {python,numba,numpy,cython}, 
  --implementation {python,numba,numpy,cython}
                        select implementation (default: python)
  -sc, --scale          select scale factor to resize (1 - original size, type: float)
  -r, --runtime         check average time over N runs for selected filter (type: int)
  -k, --k               set sepia effect from 0-1 (0-100 percent). valid only with numpy implementation. (type: float)
                        
```
#### Examples of use
```bash
instapy "./rain.jpg" -se -o "./output.jpg"
# apply the sepia filter with python implementation to "rain.jpg" and save the result to "output.jpg"

```
```bash
python -m instapy "./rain.jpg" -se -sc 0.8 -i numpy -k 0.5
# apply the sepia filter with numpy implementation to "rain.jpg"
# with sepia filter effect to 0.5 (50%) and resize the image to 0.8 of its original size

```
### 2. Import modules in other python files

#### Modules

- python_filters

`python_color2gray(image: np.array) -> np.array`

`python_color2sepia(image: np.array)`

- numpy_filters

`numpy_color2gray(image: np.array) -> np.array`

`numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array`

- numba_filters

`numba_color2gray(image: np.array) -> np.array`

`numba_color2sepia(image: np.array) -> np.array`

- cython_filters

`np.ndarray[np.uint8_t, ndim=2] cython_color2gray(np.ndarray[np.uint8_t, ndim=3] image)`

`np.ndarray[np.uint8_t, ndim=3] cython_color2sepia(np.ndarray[np.uint8_t, ndim=3] image)`

- io

`read_image(filename: str) -> np.array`

`write_image(array: np.array, filename: str) -> None`

`random_image(width: int = 320, height: int = 180) -> np.array`

`display(array: np.array)`

#### Examples of use
```python
from instapy.python_filters import python_color2gray, python_color2sepia
from instapy import io

filename="./test/rain.jpg"
image = io.read_image(filename) # load image (= numpy.asarray(Image.open(filename))) 
filtered_image = python_color2gray(image)
io.display(filtered_image) # display image (= Image.fromarray(filtered_image).show())
```
```python
from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from instapy import io

filename="./test/rain.jpg"
image = io.read_image(filename) # load image (= numpy.asarray(Image.open(filename))) 
filtered_image = numpy_color2sepia(image, k=0.5) # set sepia effect to 0.5 (50%)
io.write_image(filtered_image, outfilename) # save image (= Image.fromarray(filtered_image).save(outfilename))
```
