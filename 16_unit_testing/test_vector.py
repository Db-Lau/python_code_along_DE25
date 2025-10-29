from pytest import raises
from vector import Vector


def test_valid_init():
    v = Vector(1, 2)
    assert v.numbers == (1, 2)


# TODO: you guys implement these until 11:30 and take some break also


# test negative values in init
def test_negative_valid_init():
    v = Vector(-1, -5, 3)
    assert v.numbers == (-1, -5, 3)

# test string in the init
def test_string_in_init():
    with raises(TypeError):
        Vector("1")


# test len() function

# test abs() function


def test_empty_vector_fail():
    with raises(ValueError):
        Vector()
