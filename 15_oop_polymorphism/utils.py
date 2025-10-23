from numbers import Number

def validate_number(value):        
    if not isinstance(value, Number):
        raise TypeError(f"elements must be numbers not {type(value)}")