"""
Array class for assignment 2
"""
from numpy import allclose
from itertools import repeat,product
from copy import deepcopy

class Array:

    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        def multiply_iter(iter):
            result = 1
            for x in iter:
                result = result * x
            return result
        # source ref: https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/

        def ndarray(shape, val=0):
            base = val
            for dim in reversed(shape):
                base = list(map(deepcopy, repeat(base, times=dim)))
            return base
        # source ref: https://stackoverflow.com/questions/71041205/is-it-possible-to-define-function-that-creates-an-n-dimensional-list-of-lists-ea

        def recursive_getitem(n, j, v, arr):
            if n == 1:
                return arr.__getitem__(v[j-1])            
            else:
                return recursive_getitem(n-1,j-1,v,arr).__getitem__(v[j-1])

        # Check if the values are of valid types
        if not isinstance(shape, tuple):
            raise TypeError("the shape is the wrong type")
        if not all(isinstance(v, (int, float)) for v in values): ## bool: a subclass of int
            raise TypeError("the values are the wrong type")

        # If the values are not all of the same type: ValueError
        if not all(type(v) is type(values[0]) for v in values[1:]): 
            raise ValueError("the values are not all of the same type")

        # Check that the amount of values corresponds to the shape
        # If the number of values does not fit with the shape: ValueError
        if len(shape)==1:
            if shape[0]!=len(values):
                raise ValueError("the number of values does not fit with the shape")
        else:
            # if shape[0]*shape[1]!=len(values): # works for 2d
            if multiply_iter(shape)!=len(values):
                raise ValueError("the number of values does not fit with the shape")

        # Set instance attributes
        self.shape = shape
        if len(self.shape)==1:
            self.flattened_values = list(values)
            self.values = list(values)
        else:
            self.flattened_values = list(values)
            nd_array = ndarray(shape)
            c=0
            for positions in product(*(range(i) for i in shape)):
                recursive_getitem(len(shape)-1,len(positions)-1,positions,nd_array).__setitem__(positions[-1],values[c])
                c+=1
            self.values = nd_array
            # self.values = [[values[shape[1]*row+col] for col in range(shape[1])] for row in range(shape[0])] # works for 2d

    def __getitem__(self, key):
        """Index Array with the given key.

        Args:
            key (int): the number to index to this array.

        Returns:
            indexed value of the array

        """
        return self.values[key]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return str(self.values) 
        
    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented
        if type(self.flattened_values[0])==bool or type(other)==bool or not isinstance(other, (Array, int, float)): # other: Array, int (bool X), float
            return NotImplemented
            
        if isinstance(other, Array): 
            if self.shape!=other.shape:
                raise ValueError("two array shapes do not match")
            if type(other.flattened_values[0])==bool:
                return NotImplemented
            else:
                return self.__class__(self.shape, *list(map(lambda x,y:x+y, self.flattened_values, other.flattened_values)))   
        else:
            return self.__class__(self.shape, *list(map(lambda x:x+other, self.flattened_values)))

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other) ## commutative

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        if type(self.flattened_values[0])==bool or type(other)==bool or not isinstance(other, (Array, int, float)): # other: Array, int (bool X), float
            return NotImplemented
            
        if isinstance(other, Array):
            if self.shape!=other.shape:
                raise ValueError("two array shapes do not match")
            if type(other.flattened_values[0])==bool:
                return NotImplemented
            else:
                return self.__class__(self.shape, *list(map(lambda x,y:x-y, self.flattened_values, other.flattened_values)))   
        else:
            return self.__class__(self.shape, *list(map(lambda x:x-other, self.flattened_values)))

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        if type(self.flattened_values[0])==bool or type(other)==bool or not isinstance(other, (Array, int, float)): # other: Array, int (bool X), float
            return NotImplemented

        if isinstance(other, Array): 
            if self.shape!=other.shape:
                raise ValueError("two array shapes do not match")
            if type(other.lattened_values[0])==bool:
                return NotImplemented
            else:
                return self.__class__(self.shape, *list(map(lambda x,y:y-x, self.flattened_values, other.flattened_values)))   
        else:
            return self.__class__(self.shape, *list(map(lambda x:other-x, self.flattened_values)))

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if type(self.flattened_values[0])==bool or type(other)==bool or not isinstance(other, (Array, int, float)): # other: Array, int (bool X), float
            return NotImplemented
            
        if isinstance(other, Array):
            if self.shape!=other.shape:
                raise ValueError("two array shapes do not match")
            if type(other.flattened_values[0])==bool:
                return NotImplemented
            else:
                return self.__class__(self.shape, *list(map(lambda x,y:x*y, self.flattened_values, other.flattened_values)))  
                
        else:
            return self.__class__(self.shape, *list(map(lambda x:x*other, self.flattened_values)))

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other) ## commutative

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if not isinstance(other, Array):
            return False
        if self.shape != other.shape:
            return False
     
        # if self.flattened_values == other.flattened_values:
        if all(list(map(lambda x,y:allclose(x,y), self.flattened_values, other.flattened_values))):
            return True
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        if type(other)==bool or not isinstance(other, (Array, int, float)):
            raise TypeError("the supplied argument is the wrong type")
        if isinstance(other, Array): 
            if self.shape!=other.shape:
                raise ValueError("two array shapes do not match")
            else:
                # return self.__class__(self.shape, *list(map(lambda x,y:x == y, self.flattened_values, other.flattened_values)))
                return self.__class__(self.shape, *list(map(lambda x,y:allclose(x,y), self.flattened_values, other.flattened_values)))
        else:
            # return self.__class__(self.shape, *list(map(lambda x:x == other, self.flattened_values)))
            return self.__class__(self.shape, *list(map(lambda x:allclose(x,other), self.flattened_values)))

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        if type(self.flattened_values[0])==bool:
            raise TypeError("type boolean is not supported") 
        else:
            return float(min(self.flattened_values))

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """
        if type(self.flattened_values[0])==bool:
            raise TypeError("type boolean is not supported") 
        else:
            return float(sum(self.flattened_values)/len(self.flattened_values))

    def __repr__(self):
        return str(self.values)
        # return f"{self.__class__.__name__}({self.values})" 
