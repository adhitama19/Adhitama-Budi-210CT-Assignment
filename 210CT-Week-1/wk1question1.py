""" This is the week 1 question 1 solution. The question ask us to write a function that shuffles an array
    of integers and should explain the rationale behind its implementation. For this question the function
    will be named shuffle_number and the parameter will be named numbers. 
    
    The output will return a random shuffled elements
    Input: [1, 2, 3, 4, 5]
    Potential output: [1, 4, 2, 3, 5] 

"""
 

from random import randrange                                # Import random range


def shuffle_number(list_number): 
    
    new_list = []
    
    for x in list_number:                                   # for loop to go through each element in list_number.
        
        random_index = randrange(0, len(list_number)-1)     # using randrange to give random index 
        new_list.insert(random_index, x)                    # value x will be inserted to new_list with random index specified

    return new_list 

n = [5, 4, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(shuffle_number(n))
