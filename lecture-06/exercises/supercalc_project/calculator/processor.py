'''відповідає за розбір рядка введення (витяг операторів та операндів) та обчислення результату'''
from .operations import ops

def extract(entry):
    for o in ops.keys():
        if o in entry:
            parts = entry.split(o)
            if len(parts) == 2:
                a, b = parts
                return a.strip(), b.strip(), o
    return None, None, None

def result(a, b, operator):
    """This function returns the result"""
    try:
        a, b = float(a), float(b)
        if operator == '/' and b == 0:
            return None, "Oops, division by zero"
        elif operator in ('//', '%') and b == 0:
            return None, "Oops, division or modulo by zero"
        else:
            return ops[operator](a, b), ''
    except ValueError:
        return None, "Invalid input. Please enter numeric values."