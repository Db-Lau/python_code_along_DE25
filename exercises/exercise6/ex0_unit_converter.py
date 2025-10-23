from numbers import Number

def validate_positive_number(value) -> None:
    if not isinstance(value, Number):
        raise TypeError(f"the value must be a Number not a {type(value)}")

    if value < 0:
        raise ValueError(f"value can't be negative, not {value}")


class UnitConverter:
    # | means or
    def __init__(self, value: int | float):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # validation code
        validate_positive_number(new_value)

        self._value = new_value


unit_converter = UnitConverter(5)

# shortcut to get this output:
# unit_converter.value = 5
print(f"{unit_converter.value = }")

try:
    unit_converter.value = "5"
except TypeError as err:
    print(err)

try:
    unit_converter.value = -5
except ValueError as err:
    print(err)

