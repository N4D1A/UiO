"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""

import time
import instapy
from instapy import io 
from typing import Callable
import numpy as np
from pathlib import Path 


assignment_dir = Path(__file__).absolute().parent.parent 


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    times = []
    
    for _ in range(calls):
        start_time = time.time()
        filter_function(*arguments)
        times.append(time.time()-start_time)

    return np.mean(times)


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """
    # open a txt.file 
    f = open("timing-report.txt","w+")

    # load the image
    image = io.read_image(assignment_dir.joinpath(filename))
    # print the image name, width, height
    print(f"Timing performed using: {filename} (width * height: {image.shape[1]} * {image.shape[0]})")

    # write data into the file
    f.write(f"Timing performed using: {filename} (width * height: {image.shape[1]} * {image.shape[0]})\n")

    # iterate through the filters
    filter_names = ["color2gray", "color2sepia"]
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = instapy.get_filter(filter=filter_name)  
        # time the reference implementation
        reference_time = time_one(reference_filter, image, calls=calls)
        print(
           f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})" 
        )

        # write data into the file
        f.write(f"\nReference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})\n")

        # iterate through the implementations
        implementations = ["numpy", "numba", "cython"] 
        for implementation in implementations:
            filter = instapy.get_filter(filter=filter_name, implementation=implementation) 

            # call it once
            filter(image) # to separate the first calling time in numba implementation 

            # time the filter
            filter_time = time_one(filter, image, calls=calls)
            # compare the reference time to the optimized time
            speedup = reference_time/filter_time
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )

            # write data into the file
            f.write(f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)\n")

    # close the file instance       
    f.close()

if __name__ == "__main__":
    
    make_reports()
