""" This question will ask me to find the run-time bounds of last week questions using the
    Big O Notation """

# Question 1
from random import randrange  #randrange imported from random module.


def shuffle_number(list_number):

    new_list = []                                           # (1)

    for x in list_number:                                   # (n)

        random_index = randrange(0, len(list_number))     # (n)
        new_list.insert(random_index, x)                    # (n)

    return new_list                                         # (1)

n = [5, 4, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(shuffle_number(n))


# Big O Notation = O (n + n + n + 1 + 1)
# Big O Notation = O (3n + 2)
# Therefore the O notation = O(n)

#Question 2
def count_factorial(number): #

    numberInt = int(number)
    factorial_list = []                                                             # (1) 
    total_zeros = 0                                                                 # (1)    
    result = 1                                                                      # (1)         

    for num in range (1, number+1):                                                   # (n)     
        factorial_list.append(i)                                                    # (n)  

    for elm in factorial_list:                                                      # (n)    
        result *= elm                                                               # (n)            

    for elm in factorial_list:                                                      # (n)   
        while elm > 0:                                                              # (n * n)            
            if elm % 5 == 0:                                                        # (n * n)     
                total_zeros = total_zeros + 1                                       # (n * n)  
                elm = elm/5                                                         # (n * n)                  
    
            else:                                                                   # (n * n)                 
                break                                                               # (n * n)             


    if number < 20:                                                                 # (1)
        statement_less =  ("The factorial for this value is: %d \nand the trailing zero's for this value is: %d" % (result, total_zeros))   # (1)                   # (1)
        return (statement_less)                                                     # (1)
        

    else:                                                                                # (1)
        statement_more = ("The trailing zero's for this value is: %d" % (total_zeros))   # (1)
        return (statement_more)                                                          # (1)
    
    return    

# Big O Notation = O ((n * n) + (n * n) + (n * n) + (n * n) + (n * n) + (n * n) + n + n + n + n + n + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1)
# Big O Notation = O (6n ^ 2 + 5n + 9)
# Therefore the 0 Notation = O (n ^ 2)
