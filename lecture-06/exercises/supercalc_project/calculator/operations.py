'''містить математичні функції та словник операцій'''
def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    return x / y

def modulo(x, y):
    """This function finds the modulus of two numbers"""
    return x % y

def idivide(x, y):
    """This function integer divides two numbers"""
    return x // y

def exponent(x, y):
    """This function raises x to the power of y"""
    return x ** y

# Словник операцій
ops = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '//': idivide,
    '%': modulo,
    '**': exponent
}