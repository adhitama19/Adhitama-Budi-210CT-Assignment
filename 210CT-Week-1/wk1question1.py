""" This is the week 1 question 1 solution. The question ask us to write a function that shuffles an array
    of integers and should explain the rationale behind its implementation. For this question the function
    will be named shuffle_number and the parameter will be named numbers. The code will be commented to
    tell what each line do. """
 
import random # This line will import Python built-in function called random
from random import randrange  # This will import randrange function, which will shuffles number within range specified


def shuffle_number(numbers): # A new function is defined with shuffle_number as name, and numbers as the parameter

    empty_lst = []     # empty_lst will be appended from numbers, then it will be shuffled by the second for loop

    for i in numbers:   # This loop will go through all the value in "numbers" parameter
        
        empty_lst.append(i)   # using ".append" list function, the value of i will be appended to empty_lst

    for x in empty_lst:   # New for loop is made which will go through all value in empty_lst.
        
        random_index = randrange(0, len(empty_lst)+1) # using the built-in function randrange. This will give random_index a random value to shuffle numbers from its index
        empty_lst.insert(random_index, empty_lst.pop(x)) # This is the important line to shuffle the numbers. the object (x) will be inserted in a random index.

    return empty_lst #returns the empty_lst with new shuffled arrays

n = [5, 4, 2, 3, 1]

print(shuffle_number(n))
