# About The assignment

Implementing a class Array that supports basic arithmetic operations for ND arrays.



# Usage
Download *array_class.py* and import it.
```python
from array_class import Array

# Array((array_shape), array_values)

# Examples
a = Array((4,), 1, 2, 3, 4) 
# array shape: (4,) - 1D
# array values: 1, 2, 3, 4
print(a) # returns [1, 2, 3, 4]

b = Array((3,2), 1, 2, 3, 4, 5, 6) 
# array shape: (3,2) - 2D
# array values: 1, 2, 3, 4, 5, 6
print(b) # returns [[1, 2], [3, 4], [5, 6]]

c = Array((3,2), 1, 3, 5, 7, 9, 11)
# array shape: (3,2) - 2D
# array values: 1, 3, 5, 7, 9, 11
print(c) # returns [[1, 3], [5, 7], [9, 11]]

d = Array((2,2,3), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) 
# array shape: (2,2,3) - 3D
# array values: 1,2,3,4,5,6,7,8,9,10,11,12
print(d) # returns [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

b+c # returns [[2, 5], [8, 11], [14, 17]]
b-c # returns [[0, -1], [-2, -3], [-4, -5]]
b*c # returns [[1, 6], [15, 28], [45, 66]]
b==c # returns False
b.is_equal(c) # returns [[True, False], [False, False], [False, False]] # element-wise comparison
b.min_element() # returns 1.0
b.mean_element() # returns 3.5
```

# Unit test
## 1. Run *test_array.py*
```bash
python test_array.py
```
## 2. Use *pytest*
```bash
pip install -U pytest
```
Then
```bash
pytest [-v]
```
(It runs the files starting with test_*.py or *_test.py. See more [here](https://docs.pytest.org/en/7.1.x/getting-started.html))
