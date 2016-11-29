""" This is the question 3 coursework solution. It asks us to returns the highest perfect square of a value.
    If the value does not have the perfect square, it should return the lower highest perfect square of that
    value. """

from math import sqrt                     # import built-in sqrt function from math module

def fact_number(number):                  # a new function called fact_number is defined with number as the parameter

    perfect_square = []                   # empty list called perfect_square that will later be appended


    for i in range (1, number):           # a for loop that will go through range 1 to number parameter with less 1 value
            new_val = (i * i)               # a variable to multiply the square root of i
            perfect_square.append(new_val)  # perfect_square empty list will be appended with new_val value which creates a list with number that have a square root

    if number in perfect_square:            # conditional statement to check if the input number in perfect_square list
        print ("The square root for your value is: %d" % int(sqrt(number)))                 # statements that will return the square root of the input number

    else:                                   # statements that will be executed if input number is not perfect square
        final_val = perfect_square[-1]      # this will get the last value in a list that is lower 1 value of the input
        final_Ans = int(sqrt(sqrt(final_val)))         # this variable will be the square root of final_val
        
        print ("The perfect square of the number less than the input is: %d" % final_Ans)      #it will then return the sqrt of final_Ans as the answer
    

fact_number(1025)
