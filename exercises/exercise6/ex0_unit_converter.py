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

        self._value = new_value

unit_converter = UnitConverter(5)

# shortcut to get this output: 
# unit_converter.value = 5 
print(f"{unit_converter.value = }")