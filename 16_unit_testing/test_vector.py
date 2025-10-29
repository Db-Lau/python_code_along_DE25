from pytest import raises
from vector import Vector

def test_valid_init():
    v = Vector(1,2)
    assert v.numbers == (1,2)

# test negative values in init


# test string in the init


# test len() function


# test abs() function

def test_empty_vector_fail():
    with raises(ValueError):
        Vector()