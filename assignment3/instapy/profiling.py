"""
Profiling (IN4110 only)
"""
import pstats
import cProfile
import line_profiler
import numpy
import instapy
from instapy import io 
import importlib 
from pstats import SortKey

def profile_with_cprofile(filter, image, ncalls=3): 
    """Profile filter(image) with line_profiler

    Statistics will be printed to stdout.

    Args:

        filter (callable): filter function
        image (ndarray): image to filter
        ncalls (int): number of repetitions to measure
    """
    profiler = cProfile.Profile()

    # run `filter(image)` in the profiler
    for i in range(ncalls):
        profiler.runcall(filter, image) 
    
    stats = pstats.Stats(profiler)
    
    # print the top 10 results, sorted by cumulative time
    # (check sort_stats and print_stats docstrings)
    stats.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(10)


def profile_with_line_profiler(filter, image, ncalls=3):
    """Profile filter(image) with line_profiler

    Statistics will be printed to stdout.

    Args:

        filter (callable): filter function
        image (ndarray): image to filter
        ncalls (int): number of repetitions to measure
    """
    # create the LineProfiler
    profiler = line_profiler.LineProfiler()

    # tell it to measure the function we are given
    profiler.add_function(filter) 

    # Measure filter(image)
    for i in range(ncalls):
        profiler.runcall(filter, image)

    # print statistics
    profiler.print_stats()


def run_profiles(profiler: str = "cprofile"):
    """Run profiles of every implementation

    Args:

        profiler (str): either 'line_profiler' or 'cprofile'
    """
    # Select which profile function to use
    module = importlib.import_module(f"instapy.profiling")

    if profiler == "line_profiler":
        filter_name = f"profile_with_{profiler}"
        profile_func = getattr(module, filter_name)
    elif profiler.lower() == "cprofile":
        profiler = "cprofile" 
        filter_name = f"profile_with_{profiler}"
        profile_func = getattr(module, filter_name)
    else:
        raise ValueError(f"{profiler=} must be 'line_profiler' or 'cprofile'")

    # construct a random 640x480 image
    image = io.random_image(width=640, height=480)

    filter_names = ["color2gray", "color2sepia"]
    implementations = ["python", "numpy", "numba", "cython"]
    for filter_name in filter_names:
        for implementation in implementations:
            print(f"Profiling {implementation} {filter_name} with {profiler}:")
            filter = instapy.get_filter(filter_name, implementation)  
            # call it once
            filter(image) 
            profile_func(filter, image) 


if __name__ == "__main__":
    print("Begin cProfile")
    run_profiles("cprofile")
    print("End cProfile")
    print("Begin line_profiler")
    run_profiles("line_profiler")
    print("End line_profiler")

