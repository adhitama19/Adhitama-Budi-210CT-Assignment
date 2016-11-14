""" This solution is to solve the addition, subtraction, and multiplication of two matrices.
New functions will be defined where each addition, multiplication, and division will be calculated
separately."""


def function_add(b, c):
    addition = b, c
    return addition

def function_multiply(function_add):
    multiply = 2 * (function_add)
    return multiply

def function_Newtiply(b, c):
    multiply = b * c
    return multiply

def result_A (function_multiply, function_newtiply):

    result = function_Newtiply - function_multiply
    return result

print (function_add(3, 2))
print (function_multiply(function_add))
print (function_Newtiply(3, 2))
print (result_A (function_multiply, function_newtiply))
