"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from instapy import io
from instapy.timing import time_one 

def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: float = 1,
    calls: int = None,
    k: float = None 
) -> None:

    """Run the selected filter"""
    # load the image from a file
    image =Image.open(file)

    # Resize image, if needed
    if scale != 1:
        image = image.resize((int(image.width*scale), int(image.height*scale)))
        image = np.asarray(image)
    else:
        image = np.asarray(image)
    
    # Apply the filter
    selected_filter = instapy.get_filter(filter=filter, implementation=implementation)


    if k!=None:
        filtered = selected_filter(image, k)
    else:    
        filtered = selected_filter(image) 
    
    # Save the file
    if out_file: 
        io.write_image(filtered, out_file)
    
    # Not asked to save, display it instead
    else:
        io.display(filtered)

    # Runtime tracking 
    if calls:
        runtime = time_one(selected_filter, image, calls=calls)
        print(f"Average time over {calls} runs for {implementation}_{filter}: {runtime:.3}s")


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="filename to apply filter to")
    
    # Add required arguments
    parser.add_argument("-o", "--out", help="output filename with selected filter applied") 
    parser.add_argument("-g", "--gray", help="select gray filter (flag)", action='store_true') 
    parser.add_argument("-se", "--sepia", help="select sepia filter (flag)", action='store_true') 
    parser.add_argument("-i", "--implementation", choices=['python', 'numpy', 'numba', 'cython'], help="select implementation (default: python)", default='python')
    parser.add_argument("-sc", "--scale", help="select scale factor to resize (1 - original size, type: float)", type=float, default=1) 
    parser.add_argument("-r", "--runtime", help="check average time over N runs for selected filter (type: int)", type=int) 
    parser.add_argument("-k", "--k", help="set sepia effect from 0-1 (0-100 percent). valid only with numpy implementation. (type: float)", type=float) 

    # parse arguments and call run_filter
    args = parser.parse_args(argv)
    print(args)

    if args.k:
        if not args.sepia or not args.implementation=='numpy':
            raise ValueError(f"k works only in sepia filter with numpy implementation")

    if args.runtime:
        if args.runtime < 1:
            raise ValueError(f"number of runs must be greater than 0")
    
    if args.gray:
        filter="color2gray"
        run_filter(file=args.file, out_file=args.out, filter=filter, implementation=args.implementation, scale=args.scale, calls=args.runtime, k=args.k) 
        
    if args.sepia:
        filter="color2sepia"
        run_filter(file=args.file, out_file=args.out, filter=filter, implementation=args.implementation, scale=args.scale, calls=args.runtime, k=args.k) 

    else:
        run_filter(file=args.file, out_file=args.out, implementation=args.implementation, scale=args.scale, calls=args.runtime)

