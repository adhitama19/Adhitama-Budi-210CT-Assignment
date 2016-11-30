"""This is the solution for question 7 coursework. The question ask us to create a recursive function
   to find if a number is a prime number or not. the function will be called as recursive_prime with
   'a' and 'number' as the input. number will be the value that is going to be checked if its prime
   or not. while a will be the value that will keep on increasing until it is not bigger than nummber"""

def recursive_prime (div, number): # new function is defined as recursive_prime. with parameter a and number

    if number < 1:               # conditional statement to check if number is less than 1. since number less than 1 are definitely not prime numbers
        return False             # this will return False

    else:                        # another conditional statement
        while div < number:        # a while loop that will be executed if div is lower than number

            if (number % div) == 0: 
                return False        

            else:
                return recursive_prime (div + 1, number) 

        return True # if there are no remainders it is returned as true.


print (recursive_prime(2, 13))
