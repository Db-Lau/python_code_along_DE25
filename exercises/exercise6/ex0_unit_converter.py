class UnitConverter:
    # | means or
    def __init__(self, value: int | float):
        self.value = value


unit_converter = UnitConverter(5)

print(unit_converter.value)