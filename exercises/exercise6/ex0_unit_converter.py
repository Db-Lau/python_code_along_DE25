from numbers import Number


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
        if not isinstance(new_value, Number):
            raise TypeError(f"the value must be a Number not a {type(new_value)}")

        self._value = new_value


unit_converter = UnitConverter(5)

# shortcut to get this output:
# unit_converter.value = 5
print(f"{unit_converter.value = }")
