"""
Tests for our array class
"""
import pytest
from array_class import Array
from numpy.testing import assert_allclose


# 1D tests (Task 4)
def test_str_1d():
    assert str(Array((5,),0,1,2,3,4))=='[0, 1, 2, 3, 4]'
    assert str(Array((4,),0.0,1.1,2.2,3.3))=='[0.0, 1.1, 2.2, 3.3]'
    assert str(Array((3,),True,False,True))=='[True, False, True]'


def test_add_1d():
    """
    self: type -> Array (int, float)
                bool array: NotImplemented (TypeError)
    right operand: type -> Array, int(bool X), float
                other types: NotImplemented (TypeError)
                bool array: NotImplemented (TypeError)
                array with different shape: ValueError
    
    commutativity check (commutative)
    """
    # Array + Array
    assert Array((3,),1,2,3) + Array((3,),2,4,6) == Array((3,),3,6,9) 
    assert Array((3,),2,4,6) + Array((3,),1,2,3) == Array((3,),3,6,9) # commutative

    assert Array((2,),0.1,0.2) + Array((2,),1.0,2.0) == Array((2,),1.1,2.2)
    assert Array((2,),1.0,2.0) + Array((2,),0.1,0.2) == Array((2,),1.1,2.2) 

    assert Array((2,),1,2) + Array((2,),1.0,2.0) == Array((2,),2.0,4.0)
    assert Array((2,),1.0,2.0) + Array((2,),1,2) == Array((2,),2.0,4.0)

    assert Array((1,),1) + Array((1,),0) == Array((1,),1)
    assert Array((1,),0) + Array((1,),1) == Array((1,),1)

    assert Array((1,),0.1) + Array((1,),0.2) == Array((1,),0.3) ## 0.30000000000000004

    # Array + Int / Int + Array
    assert Array((3,),1,2,3) + 3 == Array((3,),4,5,6)
    assert 3 + Array((3,),1,2,3) == Array((3,),4,5,6)

    # Array + float / float + Array
    assert Array((3,),1,2,3) + 0.5 == Array((3,),1.5,2.5,3.5)
    assert 0.5 + Array((3,),1,2,3) == Array((3,),1.5,2.5,3.5)

    # other types (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,),1,2,3) + [1,2,3]
    with pytest.raises(TypeError): 
        [1,2,3] + Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) + True
    with pytest.raises(TypeError): 
        True + Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) + "123"
    with pytest.raises(TypeError): 
        "123" + Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) + None
    with pytest.raises(TypeError): 
        None + Array((3,),1,2,3)

    # boolean array (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,),1,2,3) + Array((3,),True,False,True)
    with pytest.raises(TypeError): 
        Array((3,),True,False,True) + Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),True,False,True) + Array((3,),False,True,False)
    with pytest.raises(TypeError): 
        Array((3,),False,True,False) + Array((3,),True,False,True)

    with pytest.raises(TypeError): 
        Array((3,),True,False,True) + 0
    with pytest.raises(TypeError): 
        0 + Array((3,),True,False,True)

    with pytest.raises(TypeError): 
        Array((2,),False,True) + 1.0
    with pytest.raises(TypeError): 
        1.0 + Array((2,),False,True)

    # array with different shape: ValueError
    with pytest.raises(ValueError): 
        Array((3,),1,2,3) + Array((4,),4,3,2,1)
    with pytest.raises(ValueError): 
        Array((4,),4,3,2,1) + Array((3,),1,2,3)

    with pytest.raises(ValueError): 
        Array((2,),1.0,2.0) + Array((1,),1.5)
    with pytest.raises(ValueError): 
        Array((1,),1.5) + Array((2,),1.0,2.0)


def test_sub_1d():
    """
    self: type -> Array (int, float)
                bool array: NotImplemented (TypeError)
    right operand: type -> Array, int(bool X), float
                other types: NotImplemented (TypeError)
                bool array: NotImplemented (TypeError)
                array with different shape: ValueError
    
    commutativity check (not commutative)
    """
    # Array - Array
    assert Array((3,),1,2,3) - Array((3,),2,4,6) == Array((3,),-1,-2,-3) 
    assert Array((3,),2,4,6) - Array((3,),1,2,3) == Array((3,),1,2,3) # not commutative 

    assert Array((2,),0.1,0.2) - Array((2,),1.0,2.0) == Array((2,),-0.9,-1.8)
    assert Array((2,),1.0,2.0) - Array((2,),0.1,0.2) == Array((2,),0.9,1.8) 

    assert Array((2,),1,2) - Array((2,),1.0,2.0) == Array((2,),0.0,0.0)
    assert Array((2,),1.0,2.0) - Array((2,),1,2) == Array((2,),0.0,0.0)

    assert Array((1,),1) - Array((1,),0) == Array((1,),1)
    assert Array((1,),0) - Array((1,),1) == Array((1,),-1)

    # Array - Int / Int - Array
    assert Array((3,),1,2,3) - 3 == Array((3,),-2,-1,0)
    assert 3 - Array((3,),1,2,3) == Array((3,),2,1,0)

    # Array - float / float - Array
    assert Array((3,),1,2,3) - 0.5 == Array((3,),0.5,1.5,2.5)
    assert 0.5 - Array((3,),1,2,3) == Array((3,),-0.5,-1.5,-2.5)

    ## other types (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,),1,2,3) - [1,2,3]
    with pytest.raises(TypeError): 
        [1,2,3] - Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) - True
    with pytest.raises(TypeError): 
        True - Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) - "123"
    with pytest.raises(TypeError): 
        "123" - Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) - None
    with pytest.raises(TypeError): 
        None - Array((3,),1,2,3)

    ## boolean array (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,),1,2,3) - Array((3,),True,False,True)
    with pytest.raises(TypeError): 
        Array((3,),True,False,True) - Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),True,False,True) - Array((3,),False,True,False)
    with pytest.raises(TypeError): 
        Array((3,),False,True,False) - Array((3,),True,False,True)

    with pytest.raises(TypeError): 
        Array((3,),True,False,True) - 0
    with pytest.raises(TypeError): 
        0 - Array((3,),True,False,True)

    with pytest.raises(TypeError): 
        Array((2,),False,True) - 1.0
    with pytest.raises(TypeError): 
        1.0 - Array((2,),False,True)

    # array with different shape: ValueError
    with pytest.raises(ValueError): 
        Array((3,),1,2,3) - Array((4,),4,3,2,1)
    with pytest.raises(ValueError): 
        Array((4,),4,3,2,1) - Array((3,),1,2,3)

    with pytest.raises(ValueError): 
        Array((2,),1.0,2.0) - Array((1,),1.5)
    with pytest.raises(ValueError): 
        Array((1,),1.5) - Array((2,),1.0,2.0)


def test_mul_1d():
    """
    self: type -> Array (int, float)
                bool array: NotImplemented (TypeError)
    right operand: type -> Array, int(bool X), float
                other types: NotImplemented (TypeError)
                bool array: NotImplemented (TypeError)
                array with different shape: ValueError
    
    commutativity check (commutative)
    """
    # Array * Array
    assert Array((3,),1,2,3) * Array((3,),2,4,6) == Array((3,),2,8,18) 
    assert Array((3,),2,4,6) * Array((3,),1,2,3) == Array((3,),2,8,18) # commutative

    assert Array((2,),0.1,0.2) * Array((2,),1.0,2.0) == Array((2,),0.1,0.4)
    assert Array((2,),1.0,2.0) * Array((2,),0.1,0.2) == Array((2,),0.1,0.4) 

    assert Array((2,),1,2) * Array((2,),1.0,2.0) == Array((2,),1.0,4.0)
    assert Array((2,),1.0,2.0) * Array((2,),1,2) == Array((2,),1.0,4.0)

    assert Array((1,),1) * Array((1,),0) == Array((1,),0)
    assert Array((1,),0) * Array((1,),1) == Array((1,),0)

    # Array * Int / Int * Array
    assert Array((3,),1,2,3) * 3 == Array((3,),3,6,9)
    assert 3 * Array((3,),1,2,3) == Array((3,),3,6,9)

    # Array * float / float * Array
    assert Array((3,),1,2,3) * 0.5 == Array((3,),0.5,1.0,1.5)
    assert 0.5 * Array((3,),1,2,3) == Array((3,),0.5,1.0,1.5)

    ## other types (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,),1,2,3) * [1,2,3]
    with pytest.raises(TypeError): 
        [1,2,3] * Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) * True
    with pytest.raises(TypeError): 
        True * Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) * "123"
    with pytest.raises(TypeError): 
        "123" * Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),1,2,3) * None
    with pytest.raises(TypeError): 
        None * Array((3,),1,2,3)

    ## boolean array (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,),1,2,3) * Array((3,),True,False,True)
    with pytest.raises(TypeError): 
        Array((3,),True,False,True) * Array((3,),1,2,3)

    with pytest.raises(TypeError): 
        Array((3,),True,False,True) * Array((3,),False,True,False)
    with pytest.raises(TypeError): 
        Array((3,),False,True,False) * Array((3,),True,False,True)

    with pytest.raises(TypeError): 
        Array((3,),True,False,True) * 1
    with pytest.raises(TypeError): 
        1 * Array((3,),True,False,True)

    with pytest.raises(TypeError): 
        Array((2,),False,True) * 1.0
    with pytest.raises(TypeError): 
        1.0 * Array((2,),False,True)

    # array with different shape: ValueError
    with pytest.raises(ValueError): 
        Array((3,),1,2,3) * Array((4,),4,3,2,1)
    with pytest.raises(ValueError): 
        Array((4,),4,3,2,1) * Array((3,),1,2,3)

    with pytest.raises(ValueError): 
        Array((2,),1.0,2.0) * Array((1,),1.5)
    with pytest.raises(ValueError): 
        Array((1,),1.5) * Array((2,),1.0,2.0)


def test_eq_1d():
    """
    self: type -> Array (int, float, bool)
    right operand: type -> Array
                other types: False
                array with different shape: False
    
    commutativity check (commutative)
    """
    # same types, same shapes, same values: True
    assert Array((3,),1,2,3) == Array((3,),1,2,3)
    assert Array((1,),1.0) == Array((1,),1.0)
    assert Array((2,),True,False) == Array((2,),True,False)
    assert Array((1,),0.33333) == Array((1,),0.33333333)

    # different types, same shapes, same values: True
    assert Array((3,),1,1,0) == Array((3,),1.0,1.0,0.0)
    assert Array((3,),1.0,1.0,0.0) == Array((3,),1,1,0) # commutative

    assert Array((3,),0,1,1) == Array((3,),False,True,True)
    assert Array((3,),False,True,True) == Array((3,),0,1,1)

    assert Array((2,),1.0,0.0) == Array((2,),True,False)
    assert Array((2,),True,False) == Array((2,),1.0,0.0)

    # different shapes: False
    assert Array((3,),1,1,0) != Array((4,),1,1,1,0)
    assert Array((4,),1,0,1,0) != Array((2,),True,False)
    assert Array((3,),1.5,0.5,1.5) != Array((2,),True,False)
    assert Array((2,),True,False) != Array((3,),1.5,0.5,1.5)

    # same shapes, different values: False
    assert Array((3,),1,1,0) != Array((3,),1,1,1)
    assert Array((3,),1.2,0.2,1.2) != Array((3,),0.0,0.2,1.0)
    assert Array((2,),True,False) != Array((2,),False,False)
    assert Array((3,),1,1,0) != Array((3,),False,True,False)
    assert Array((3,),1.5,1.5,0.5) != Array((3,),False,True,False)
    assert Array((2,),1,0) != Array((2,),0.0,2.0)

    
def test_same_1d():
    """
    self: type -> Array (int, float, bool)
    right operand: type -> Array, int, float
                other types: TypeError
                array with different shape: ValueError
    """
    # Array.is_equal(Array) - same types
    assert Array((3,),1,3,5).is_equal(Array((3,),1,5,3))==(Array((3,),True,False,False))
    assert Array((3,),0.5,1.25,2.5).is_equal(Array((3,),0.50,1.25,2.500))==(Array((3,),True,True,True))
    assert Array((3,),True,False,True).is_equal(Array((3,),False,False,True))==(Array((3,),False,True,True))

    # Array.is_equal(Array) - different types
    assert Array((3,),1,3,5).is_equal(Array((3,),1.0,3.0,5.0))==(Array((3,),True,True,True))
    assert Array((4,),1.0,2.0,5.0,0.0).is_equal(Array((4,),True,False,True,False))==(Array((4,),True,False,False,True))
    assert Array((3,),True,True,False).is_equal(Array((3,),1,2,3))==(Array((3,),True,False,False))
    assert Array((1,),True).is_equal(Array((1,),1.0))==(Array((1,),True))

    # Array.is_equal(int/float) 
    assert Array((3,),1,3,5).is_equal(1)==(Array((3,),True,False,False))
    assert Array((3,),0.5,1.25,2.5).is_equal(1.250)==(Array((3,),False,True,False))
    assert Array((2,),True,False).is_equal(0.0)==(Array((2,),False,True))
    assert Array((4,),1.0,3.5,5.0,7.5).is_equal(5)==(Array((4,),False,False,True,False))

    # other types: TypeError
    with pytest.raises(TypeError): 
        Array((3,),1,2,3).is_equal([1,2,3])
    with pytest.raises(TypeError): 
        Array((1,),1).is_equal(True)
    with pytest.raises(TypeError): 
        Array((2,),1.0,2.5).is_equal((1.0,2.5))
    with pytest.raises(TypeError): 
        Array((2,),False,True).is_equal('True')
    
    # array with different shape: ValueError
    with pytest.raises(ValueError): 
        Array((3,),1,2,3).is_equal(Array((4,),1,2,3,4))
    with pytest.raises(ValueError): 
        Array((2,),1.0,2.5).is_equal(Array((3,),1.0,2.5,1.0))
    with pytest.raises(ValueError): 
        Array((2,),1.0,2.5).is_equal(Array((3,),1,2,3))
    with pytest.raises(ValueError): 
        Array((1,),True).is_equal(Array((2,),1,1))
    with pytest.raises(ValueError): 
        Array((1,),True).is_equal(Array((2,),False,True))


def test_smallest_1d():
    """
    self: type -> Array (int, float)
            bool array: TypeError

    returns: float
    """
    assert_allclose(Array((3,),1,3,5).min_element(), 1.0)
    assert_allclose(Array((3,),5.5,3.3,1.1).min_element(), 1.1)
    assert_allclose(Array((2,),-2,2).min_element(), -2)
    assert_allclose(Array((3,),-5.5,3.3,-1.1).min_element(), -5.5)
    assert_allclose(Array((1,),5).min_element(), 5.0)
    assert_allclose(Array((1,),0.0).min_element(), 0.0)


    # return type check
    assert type(Array((1,),-1).min_element()) == float
    assert type(Array((3,),0,1,2).min_element()) == float
    assert type(Array((3,),1.1,-2.2,3.3).min_element()) == float

    # boolean array: TypeError
    with pytest.raises(TypeError): 
        Array((3,),True,False,True).min_element()
    with pytest.raises(TypeError): 
        Array((1,),False).min_element()


def test_mean_1d():
    """
    self: type -> Array (int, float)
            bool array: TypeError

    returns: float
    """
    assert_allclose(Array((4,),1,2,3,4).mean_element(), 2.5)
    assert_allclose(Array((3,),5.5,3.3,1.1).mean_element(), 3.3)
    assert_allclose(Array((2,),-2,2).mean_element(), 0.0)
    assert_allclose(Array((4,),-5.5,3.3,-1.1,2.2).mean_element(), -0.275)
    assert_allclose(Array((1,),5).mean_element(), 5.0)
    assert_allclose(Array((1,),0.0).mean_element(), 0.0)
    assert_allclose(Array((3,),0,0,1).mean_element(), 0.33333333)

    # return type check
    assert type(Array((1,),-1).mean_element()) == float
    assert type(Array((3,),0,1,2).mean_element()) == float
    assert type(Array((3,),1.1,-2.2,3.3).mean_element()) == float

    # bool array: TypeError
    with pytest.raises(TypeError): 
        Array((3,),True,False,True).mean_element()
    with pytest.raises(TypeError): 
        Array((1,),False).mean_element()


# 2D tests (Task 6)
def test_add_2d():
    """
    self: type -> Array (int, float)
                bool array: NotImplemented (TypeError)
    right operand: type -> Array, int(bool X), float
                other types: NotImplemented (TypeError)
                bool array: NotImplemented (TypeError)
                array with different shape: ValueError
    
    commutativity check (commutative)
    """
    # Array + Array
    assert Array((3,2),1,2,3,4,5,6) + Array((3,2),0,2,4,6,8,10) == Array((3,2),1,4,7,10,13,16)
    assert Array((3,2),0,2,4,6,8,10) + Array((3,2),1,2,3,4,5,6) == Array((3,2),1,4,7,10,13,16) # commutative

    assert Array((2,2),1.1,2.2,3.3,4.4) + Array((2,2),0.5,1.0,1.5,2.0) == Array((2,2),1.6,3.2,4.8,6.4)
    assert Array((2,2),0.5,1.0,1.5,2.0) + Array((2,2),1.1,2.2,3.3,4.4) == Array((2,2),1.6,3.2,4.8,6.4)

    assert Array((1,3),1,2,3) + Array((1,3),0.5,1.0,1.5) == Array((1,3),1.5,3.0,4.5)
    assert Array((1,3),0.5,1.0,1.5) + Array((1,3),1,2,3) == Array((1,3),1.5,3.0,4.5)

    assert Array((1,1),1) + Array((1,1),0.1) == Array((1,1),1.1)
    assert Array((1,1),0.1) + Array((1,1),1) == Array((1,1),1.1)

    # Array + Int / Int + Array
    assert Array((3,2),1,2,3,4,5,6) + 2 == Array((3,2),3,4,5,6,7,8)
    assert 2 + Array((3,2),1,2,3,4,5,6) == Array((3,2),3,4,5,6,7,8)

    # Array + float / float + Array
    assert Array((3,2),1,2,3,4,5,6) + 0.5 == Array((3,2),1.5,2.5,3.5,4.5,5.5,6.5)
    assert 0.5 + Array((3,2),1,2,3,4,5,6) == Array((3,2),1.5,2.5,3.5,4.5,5.5,6.5)

    # other types (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((1,3),1,2,3) + [1,2,3]
    with pytest.raises(TypeError): 
        [1,2,3] + Array((1,3),1,2,3)

    with pytest.raises(TypeError): 
        Array((1,1),1) + True
    with pytest.raises(TypeError): 
        True + Array((1,1),1)

    with pytest.raises(TypeError): 
        Array((2,2),1,2,3,4) + "1234"
    with pytest.raises(TypeError): 
        "1234" + Array((2,2),1,2,3,4)

    with pytest.raises(TypeError): 
        Array((2,3),0,1,2,3,4,5) + None
    with pytest.raises(TypeError): 
        None + Array((2,3),0,1,2,3,4,5)

    # boolean array (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,1),1,2,3) + Array((3,1),True,False,True)
    with pytest.raises(TypeError): 
        Array((3,1),True,False,True) + Array((3,1),1,2,3)

    with pytest.raises(TypeError): 
        Array((2,2),True,False,True,True) + Array((2,2),False,True,False,True)
    with pytest.raises(TypeError): 
        Array((2,2),False,True,False,True) + Array((2,2),True,False,True,True)

    with pytest.raises(TypeError): 
        Array((1,2),True,False) + 0
    with pytest.raises(TypeError): 
        0 + Array((1,2),True,False)

    with pytest.raises(TypeError): 
        Array((1,1),False) + 1.0
    with pytest.raises(TypeError): 
        1.0 + Array((1,1),False)

    # array with different shape: ValueError
    with pytest.raises(ValueError): 
        Array((3,),1,2,3) + Array((2,2),4,3,2,1)
    with pytest.raises(ValueError): 
        Array((2,2),4,3,2,1) + Array((3,),1,2,3)
    
    with pytest.raises(ValueError): 
        Array((4,),1,2,3,4) + Array((2,2),4,3,2,1)
    with pytest.raises(ValueError): 
        Array((2,2),4,3,2,1) + Array((4,),1,2,3,4)

    with pytest.raises(ValueError): 
        Array((2,1),1.0,2.0) + Array((1,2),1.5,2.5)
    with pytest.raises(ValueError): 
        Array((1,2),1.5,2.5) + Array((2,1),1.0,2.0)

    with pytest.raises(ValueError): 
        Array((2,3),1,2,3,4,5,6) + Array((2,2),1,2,3,4)
    with pytest.raises(ValueError): 
        Array((2,2),1,2,3,4) + Array((2,3),1,2,3,4,5,6)


def test_mult_2d():
    """
    self: type -> Array (int, float)
                bool array: NotImplemented (TypeError)
    right operand: type -> Array, int(bool X), float
                other types: NotImplemented (TypeError)
                bool array: NotImplemented (TypeError)
                array with different shape: ValueError
    
    commutativity check (commutative)
    """
    # Array * Array
    assert Array((3,2),1,2,3,4,5,6) * Array((3,2),0,1,2,3,4,5) == Array((3,2),0,2,6,12,20,30)
    assert Array((3,2),0,1,2,3,4,5) * Array((3,2),1,2,3,4,5,6) == Array((3,2),0,2,6,12,20,30) # commutative

    assert Array((2,2),1.1,2.2,3.3,4.4) * Array((2,2),0.5,1.0,1.5,2.0) == Array((2,2),0.55,2.2,4.95,8.8) ## 4.949999999999999
    assert Array((2,2),0.5,1.0,1.5,2.0) * Array((2,2),1.1,2.2,3.3,4.4) == Array((2,2),0.55,2.2,4.95,8.8) 

    assert Array((1,3),1,2,3) * Array((1,3),0.5,1.0,1.5) == Array((1,3),0.5,2.0,4.5)
    assert Array((1,3),0.5,1.0,1.5) * Array((1,3),1,2,3) == Array((1,3),0.5,2.0,4.5)

    assert Array((1,1),1) * Array((1,1),0.1) == Array((1,1),0.1)
    assert Array((1,1),0.1) * Array((1,1),1) == Array((1,1),0.1)

    # Array * Int / Int * Array
    assert Array((3,2),1,2,3,4,5,6) * 2 == Array((3,2),2,4,6,8,10,12)
    assert 2 * Array((3,2),1,2,3,4,5,6) == Array((3,2),2,4,6,8,10,12)

    # Array * float / float * Array
    assert Array((3,2),1,2,3,4,5,6) * 0.5 == Array((3,2),0.5,1.0,1.5,2.0,2.5,3.0)
    assert 0.5 * Array((3,2),1,2,3,4,5,6) == Array((3,2),0.5,1.0,1.5,2.0,2.5,3.0)

    # other types (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((1,3),1,2,3) * [1,2,3]
    with pytest.raises(TypeError): 
        [1,2,3] * Array((1,3),1,2,3)

    with pytest.raises(TypeError): 
        Array((1,1),1) * True
    with pytest.raises(TypeError): 
        True * Array((1,1),1)

    with pytest.raises(TypeError): 
        Array((2,2),1,2,3,4) * "1234"
    with pytest.raises(TypeError): 
        "1234" * Array((2,2),1,2,3,4)

    with pytest.raises(TypeError): 
        Array((2,3),0,1,2,3,4,5) * None
    with pytest.raises(TypeError): 
        None * Array((2,3),0,1,2,3,4,5)

    # boolean array (NotImplemented): TypeError
    with pytest.raises(TypeError): 
        Array((3,1),1,2,3) * Array((3,1),True,False,True)
    with pytest.raises(TypeError): 
        Array((3,1),True,False,True) * Array((3,1),1,2,3)

    with pytest.raises(TypeError): 
        Array((2,2),True,False,True,True) * Array((2,2),False,True,False,True)
    with pytest.raises(TypeError): 
        Array((2,2),False,True,False,True) * Array((2,2),True,False,True,True)

    with pytest.raises(TypeError): 
        Array((1,2),True,False) * 0
    with pytest.raises(TypeError): 
        0 * Array((1,2),True,False)

    with pytest.raises(TypeError): 
        Array((1,1),False) * 1.0
    with pytest.raises(TypeError): 
        1.0 * Array((1,1),False)

    # array with different shape: ValueError
    with pytest.raises(ValueError): 
        Array((3,),1,2,3) * Array((2,2),4,3,2,1)
    with pytest.raises(ValueError): 
        Array((2,2),4,3,2,1) * Array((3,),1,2,3)
    
    with pytest.raises(ValueError): 
        Array((4,),1,2,3,4) * Array((2,2),4,3,2,1)
    with pytest.raises(ValueError): 
        Array((2,2),4,3,2,1) * Array((4,),1,2,3,4)

    with pytest.raises(ValueError): 
        Array((2,1),1.0,2.0) * Array((1,2),1.5,2.5)
    with pytest.raises(ValueError): 
        Array((1,2),1.5,2.5) * Array((2,1),1.0,2.0)

    with pytest.raises(ValueError): 
        Array((2,3),1,2,3,4,5,6) * Array((2,2),1,2,3,4)
    with pytest.raises(ValueError): 
        Array((2,2),1,2,3,4) * Array((2,3),1,2,3,4,5,6)


def test_same_2d():
    """
    self: type -> Array (int, float, bool)
    right operand: type -> Array, int, float
                other types: TypeError
                array with different shape: ValueError
    """
    # Array.is_equal(Array) - same types
    assert Array((3,1),1,3,5).is_equal(Array((3,1),1,5,3))==(Array((3,1),True,False,False))
    assert Array((2,2),0.5,1.25,2.5,1.0).is_equal(Array((2,2),0.50,1.25,2.500,1.0))==(Array((2,2),True,True,True,True))
    assert Array((1,2),True,False).is_equal(Array((1,2),False,False))==(Array((1,2),False,True))

    # Array.is_equal(Array) - different types
    assert Array((3,2),1,3,5,7,9,0).is_equal(Array((3,2),1.0,3.00,5.5,7.00,9.0,9.9))==(Array((3,2),True,True,False,True,True,False))
    assert Array((2,2),1.0,2.0,5.0,0.0).is_equal(Array((2,2),True,False,True,False))==(Array((2,2),True,False,False,True))
    assert Array((4,1),True,True,False,False).is_equal(Array((4,1),1,2,3,0))==(Array((4,1),True,False,False,True))
    assert Array((1,1),True).is_equal(Array((1,1),1.0))==(Array((1,1),True))

    # Array.is_equal(int/float) 
    assert Array((3,2),1,3,5,1,0,1).is_equal(1)==(Array((3,2),True,False,False,True,False,True))
    assert Array((1,3),0.5,1.25,2.5).is_equal(1.250)==(Array((1,3),False,True,False))
    assert Array((2,1),True,False).is_equal(0.0)==(Array((2,1),False,True))
    assert Array((2,2),1.0,3.5,5.0,7.5).is_equal(5)==(Array((2,2),False,False,True,False))

    # other types: TypeError
    with pytest.raises(TypeError): 
        Array((1,3),1,2,3).is_equal([1,2,3])
    with pytest.raises(TypeError): 
        Array((1,1),1).is_equal(True)
    with pytest.raises(TypeError): 
        Array((2,1),1.0,2.5).is_equal((1.0,2.5))
    with pytest.raises(TypeError): 
        Array((2,2),False,True,False,True).is_equal('True')
    
    # array with different shape: ValueError
    with pytest.raises(ValueError): 
        Array((3,1),1,2,3).is_equal(Array((2,2),1,2,3,4))
    with pytest.raises(ValueError): 
        Array((1,2),1.0,2.5).is_equal(Array((3,1),1.0,2.5,1.0))
    with pytest.raises(ValueError): 
        Array((2,1),1.0,2.5).is_equal(Array((3,1),1,2,3))
    with pytest.raises(ValueError): 
        Array((1,1),True).is_equal(Array((2,1),1,1))
    with pytest.raises(ValueError): 
        Array((1,1),True).is_equal(Array((1,2),False,True))


def test_mean_2d():
    """
    self: type -> Array (int, float)
            bool array: TypeError

    returns: float 
    """
    assert_allclose(Array((2,2),1,2,3,4).mean_element(), 2.5)
    assert_allclose(Array((3,1),5.5,3.3,1.1).mean_element(), 3.3)
    assert_allclose(Array((2,1),-2,2).mean_element(), 0.0)
    assert_allclose(Array((2,2),-5.5,3.3,-1.1,2.2).mean_element(), -0.275)
    assert_allclose(Array((1,1),5).mean_element(), 5.0)
    assert_allclose(Array((1,1),0.0).mean_element(), 0.0)
    assert_allclose(Array((1,3),0,0,1).mean_element(), 0.33333333)
    assert_allclose(Array((2,3),1,0,1,0,1,0).mean_element(), 0.5)

    # return type check
    assert type(Array((1,1),-1).mean_element()) == float
    assert type(Array((2,2),0,1,2,3).mean_element()) == float
    assert type(Array((3,1),1.1,-2.2,3.3).mean_element()) == float

    # bool array: TypeError
    with pytest.raises(TypeError): 
        Array((2,2),True,False,True,False).mean_element()
    with pytest.raises(TypeError): 
        Array((1,1),False).mean_element()


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
