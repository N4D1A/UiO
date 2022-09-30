# Profiling report

## Questions

A few questions below to help understand the kind of information we can get from profiling outputs.
 We are not asking for lots of detail, just 1-2 sentences each.

### Question 1

> Which profiler produced the most useful output, and why?

`line-profiler` overall produced useful outputs than `cProfile`. `cProfile` shows the runtime for each function, whereas `line-profiler` shows the runtime for each line within each function, so I can get more specific information about which line took much time. However, 'line-profiler' also has a disadvantage that the results do not show properly in some optimization tools.

### Question 2

> Pick one profiler output (e.g. `cprofile numpy_color2sepia`).
  Based on this profile, where should we focus effort on improving performance?

> **Hint:** two things to consider when picking an optimization:

> - how much time is spent in the step? (reducing a step that takes 1% of the time all the way to 0 can only improve performance by 1%)
> - are there other ways to do it? (simple steps may already be optimal. Complex steps often have many implementations with different performance)

selected profile: 
line_profiler python_color2sepia  

It takes about 100% of the accumulated time for nested loops to apply sepia filter with pure python implementation. Considering that the runtime with numpy implementation using vectorizing is greatly reduced, improving the nested loop steps using vectorizing will help improve performance.



## Profile output

Paste the outputs of `python3 -m instapy.profiling` below:

<details>
<summary>cProfile output</summary>

```
Profiling python color2gray with cprofile:
         9 function calls in 6.095 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    6.095    2.032    6.095    2.032 python_filters.py:6(python_color2gray)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.empty}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numpy color2gray with cprofile:
         12 function calls in 0.015 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.014    0.005    0.015    0.005 numpy_filters.py:7(numpy_color2gray)
        3    0.001    0.000    0.001    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 {built-in method numpy.empty}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numba color2gray with cprofile:
         9 function calls in 0.001 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.001    0.000    0.001    0.000 numba_filters.py:7(numba_color2gray)
        3    0.000    0.000    0.000    0.000 serialize.py:29(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling cython color2gray with cprofile:
         9 function calls (6 primitive calls) in 0.012 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      6/3    0.012    0.002    0.012    0.004 cython_filters.pyx:6(cython_color2gray)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling python color2sepia with cprofile:
         2764815 function calls in 20.840 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3   19.971    6.657   20.840    6.947 python_filters.py:23(python_color2sepia)
  2764800    0.869    0.000    0.869    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.001    0.000 <__array_function__ internals>:2(empty_like)
        3    0.001    0.000    0.001    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 multiarray.py:80(empty_like)


Profiling numpy color2sepia with cprofile:
         117 function calls in 0.500 seconds

   Ordered by: cumulative time
   List reduced from 31 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.024    0.008    0.500    0.167 numpy_filters.py:25(numpy_color2sepia)
        3    0.044    0.015    0.472    0.157 function_base.py:2135(__call__)
        3    0.307    0.102    0.429    0.143 function_base.py:2234(_vectorize_call)
        9    0.121    0.013    0.121    0.013 {built-in method numpy.asanyarray}
        3    0.000    0.000    0.048    0.016 function_base.py:2244(<listcomp>)
        3    0.003    0.001    0.003    0.001 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 function_base.py:2165(_get_ufunc_and_otypes)
        3    0.000    0.000    0.000    0.000 numeric.py:2130(identity)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}


Profiling numba color2sepia with cprofile:
         9 function calls in 0.004 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.004    0.001    0.004    0.001 numba_filters.py:26(numba_color2sepia)
        3    0.000    0.000    0.000    0.000 serialize.py:29(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling cython color2sepia with cprofile:
         96 function calls (93 primitive calls) in 0.518 seconds

   Ordered by: cumulative time
   List reduced from 24 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      6/3    0.028    0.005    0.518    0.173 cython_filters.pyx:20(cython_color2sepia)
        3    0.042    0.014    0.490    0.163 function_base.py:2135(__call__)
        3    0.320    0.107    0.448    0.149 function_base.py:2234(_vectorize_call)
        9    0.128    0.014    0.128    0.014 {built-in method numpy.asanyarray}
        3    0.000    0.000    0.048    0.016 function_base.py:2244(<listcomp>)
        3    0.000    0.000    0.000    0.000 function_base.py:2165(_get_ufunc_and_otypes)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(empty_like)
        3    0.000    0.000    0.000    0.000 function_base.py:2103(__init__)
        3    0.000    0.000    0.000    0.000 function_base.py:2195(<listcomp>)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}

```

</details>

<details>
<summary>line_profiler output</summary>

```
Profiling python color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 7.43834 s
File: C:\Users\Narae\OneDrive - Universitetet i Oslo\IN4110\assignments\_3\assignment3\instapy\python_filters.py
Function: python_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           def python_color2gray(image: np.array) -> np.array:
     7                                               """Convert rgb pixel array to grayscale
     8
     9                                               Args:
    10                                                   image (np.array)
    11                                               Returns:
    12                                                   np.array: gray_image
    13                                               """
    14         3        284.0     94.7      0.0      gray_image = np.empty(shape=image.shape[:2], dtype=np.uint8)
    15                                               # iterate through the pixels, and apply the grayscale transform
    16      1443       7779.0      5.4      0.0      for i in range(image.shape[0]):
    17    923040    4959708.0      5.4      6.7          for j in range(image.shape[1]):
    18    921600   69415647.0     75.3     93.3              gray_image[i,j] = image[i,j][0]*0.21+image[i,j][1]*0.72+image[i,j][2]*0.07
    19
    20         3         25.0      8.3      0.0      return gray_image

Profiling numpy color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 0.0150001 s
File: C:\Users\Narae\OneDrive - Universitetet i Oslo\IN4110\assignments\_3\assignment3\instapy\numpy_filters.py
Function: numpy_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def numpy_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15
    16         3        605.0    201.7      0.4      gray_image = np.empty(shape=image.shape[:2], dtype=np.uint8)
    17
    18                                               # Hint: use numpy slicing in order to have fast vectorized code
    19         3     149222.0  49740.7     99.5      gray_image = (image @ [0.21, 0.72, 0.07]).astype(np.uint8)
    20
    21                                               # Return image (make sure it's the right type!)
    22         3        174.0     58.0      0.1      return gray_image

Profiling numba color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 0 s
File: C:\Users\Narae\OneDrive - Universitetet i Oslo\IN4110\assignments\_3\assignment3\instapy\numba_filters.py
Function: numba_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           @jit(nopython=True)
     8                                           def numba_color2gray(image: np.array) -> np.array:
     9                                               """Convert rgb pixel array to grayscale
    10
    11                                               Args:
    12                                                   image (np.array)
    13                                               Returns:
    14                                                   np.array: gray_image
    15                                               """
    16                                               gray_image = np.empty(shape=image.shape[:2], dtype=np.uint8) # 이것만 써도 됨
    17
    18                                               # iterate through the pixels, and apply the grayscale transform
    19                                               for i in range(image.shape[0]):
    20                                                   for j in range(image.shape[1]):
    21                                                       gray_image[i,j] = image[i,j][0]*0.21+image[i,j][1]*0.72+image[i,j][2]*0.07
    22
    23                                               return gray_image

Profiling cython color2gray with line_profiler:
Timer unit: 1e-07 s

Total time: 0.0170765 s
File: instapy\cython_filters.pyx
Function: cython_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           cpdef np.ndarray[np.uint8_t, ndim=2] cython_color2gray(np.ndarray[np.uint8_t, ndim=3] image):

Profiling python color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 25.0729 s
File: C:\Users\Narae\OneDrive - Universitetet i Oslo\IN4110\assignments\_3\assignment3\instapy\python_filters.py
Function: python_color2sepia at line 23

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    23                                           def python_color2sepia(image: np.array) -> np.array:
    24                                               """Convert rgb pixel array to sepia
    25
    26                                               Args:
    27                                                   image (np.array)
    28                                               Returns:
    29                                                   np.array: sepia_image
    30                                               """
    31         3        450.0    150.0      0.0      sepia_image = np.empty_like(image, dtype=np.uint8) # shape: 3d
    32
    33                                               # Iterate through the pixels
    34                                               # applying the sepia matrix
    35      1443      13770.0      9.5      0.0      for i in range(image.shape[0]):
    36    923040    8584482.0      9.3      3.4          for j in range(image.shape[1]):
    37    921600   80406240.0     87.2     32.1              sepia_image[i,j][0] = min(255, image[i][j][0]*0.393+image[i][j][1]*0.769+image[i][j][2]*0.189)
    38    921600   80820424.0     87.7     32.2              sepia_image[i,j][1] = min(255, image[i][j][0]*0.349+image[i][j][1]*0.686+image[i][j][2]*0.168)
    39    921600   80904000.0     87.8     32.3              sepia_image[i,j][2] = min(255, image[i][j][0]*0.272+image[i][j][1]*0.534+image[i][j][2]*0.131)
    40
    41                                               # Return image
    42                                               # don't forget to make sure it's the right type!
    43         3         32.0     10.7      0.0      return sepia_image

Profiling numpy color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 0.495996 s
File: C:\Users\Narae\OneDrive - Universitetet i Oslo\IN4110\assignments\_3\assignment3\instapy\numpy_filters.py
Function: numpy_color2sepia at line 25

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    25                                           def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    26                                               """Convert rgb pixel array to sepia
    27
    28                                               Args:
    29                                                   image (np.array)
    30                                                   k (float): amount of sepia filter to apply (optional)
    31
    32                                               The amount of sepia is given as a fraction, k=0 yields no sepia while
    33                                               k=1 yields full sepia.
    34
    35                                               (note: implementing 'k' is a bonus task,
    36                                               you may ignore it for Task 9)
    37
    38                                               Returns:
    39                                                   np.array: sepia_image
    40                                               """
    41
    42         3         58.0     19.3      0.0      if not 0 <= k <= 1:
    43                                                   # validate k (optional)
    44                                                   raise ValueError(f"k must be between [0-1], got {k=}")
    45
    46         3        533.0    177.7      0.0      sepia_image = np.empty_like(image, dtype=np.uint8) # shape: 3d
    47
    48                                               # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    49         6        454.0     75.7      0.0      sepia_matrix = np.array([
    50         3         64.0     21.3      0.0                      [ 0.393, 0.769, 0.189],
    51         3         37.0     12.3      0.0                      [ 0.349, 0.686, 0.168],
    52         3         36.0     12.0      0.0                      [ 0.272, 0.534, 0.131]])
    53
    54         3        876.0    292.0      0.0      identity_matrix = np.identity(3)
    55
    56         3        533.0    177.7      0.0      sepia_matrix = identity_matrix + (sepia_matrix - identity_matrix) * k
    57
    58                                               # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    59                                               # use Einstein sum to apply pixel transform matrix
    60                                               # Apply the matrix filter
    61                                               # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    62         3    4957213.0 1652404.3     99.9      sepia_image = np.vectorize(min)(255,(image @ sepia_matrix.T)).astype(np.uint8)
    63
    64                                               # Return image (make sure it's the right type!)
    65         3        155.0     51.7      0.0      return sepia_image

Profiling numba color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 0 s
File: C:\Users\Narae\OneDrive - Universitetet i Oslo\IN4110\assignments\_3\assignment3\instapy\numba_filters.py
Function: numba_color2sepia at line 26

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    26                                           @jit(nopython=True)
    27                                           def numba_color2sepia(image: np.array) -> np.array:
    28                                               """Convert rgb pixel array to sepia
    29
    30                                               Args:
    31                                                   image (np.array)
    32                                               Returns:
    33                                                   np.array: sepia_image
    34                                               """
    35                                               sepia_image = np.empty_like(image, dtype=np.uint8) # shape: 3d
    36                                               # Iterate through the pixels
    37                                               # applying the sepia matrix
    38                                               for i in range(image.shape[0]):
    39                                                   for j in range(image.shape[1]):
    40                                                       sepia_image[i,j][0] = min(255, image[i][j][0]*0.393+image[i][j][1]*0.769+image[i][j][2]*0.189)
    41                                                       sepia_image[i,j][1] = min(255, image[i][j][0]*0.349+image[i][j][1]*0.686+image[i][j][2]*0.168)
    42                                                       sepia_image[i,j][2] = min(255, image[i][j][0]*0.272+image[i][j][1]*0.534+image[i][j][2]*0.131)
    43
    44                                               # Return image
    45                                               # don't forget to make sure it's the right type!
    46                                               return sepia_image

Profiling cython color2sepia with line_profiler:
Timer unit: 1e-07 s

Total time: 0.483548 s
File: instapy\cython_filters.pyx
Function: cython_color2sepia at line 20

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    20                                           cpdef np.ndarray[np.uint8_t, ndim=3] cython_color2sepia(np.ndarray[np.uint8_t, ndim=3] image):

```

</details>
