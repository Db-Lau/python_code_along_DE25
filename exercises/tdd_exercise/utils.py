import numbers


def validate_number(value):
    if not isinstance(value, numbers.Number):
        raise TypeError("must be a number")

    if isinstance(value, bool):
        raise TypeError("can't be bool")