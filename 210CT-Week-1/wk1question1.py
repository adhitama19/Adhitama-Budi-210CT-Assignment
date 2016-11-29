""" This is the week 1 question 1 solution. The question ask us to write a function that shuffles an array
    of integers and should explain the rationale behind its implementation. For this question the function
    will be named shuffle_number and the parameter will be named numbers. The code will be commented to
    tell what each line do. """
 

from random import randrange  # This will import randrange function, which will shuffles number within range specified


def shuffle_number(list_number): # A new function is defined with shuffle_number as name, and numbers as the parameter
    
    new_list = []
    
    for x in list_number:   # for loop is made which will go through all value in empty_lst.
        
        random_index = randrange(0, len(list_number)-1) # using the built-in function randrange. This will give random_index a random value to shuffle numbers from its index
        new_list.insert(random_index, x) # This is the important line to shuffle the numbers. the object (x) will be inserted in a random index.

    return new_list #returns the empty_lst with new shuffled arrays

n = [5, 4, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(shuffle_number(n))
