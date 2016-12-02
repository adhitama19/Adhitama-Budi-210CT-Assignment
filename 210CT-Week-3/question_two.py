"""This is the solution for question 7 coursework. The question ask us to create a recursive function
   to find if a number is a prime number or not. the function will be called as recursive_prime with
   'a' and 'number' as the input. number will be the value that is going to be checked if its prime
   or not. while a will be the value that will keep on increasing until it is not bigger than number"""

def recursive_prime (div, number):

    if number < 1:
        return False

    else:
        if div < number:      #base case

            if (number % div) == 0:
                return False

            else:
                return recursive_prime (div + 1, number) # keep adding div to reach base case

        return True


print (recursive_prime(2, 30))
print (recursive_prime(2, 41))


"""
PSEUDOCODE:

RECURSIVE_PRIME (DIV, NUMBER)

    IF number < 1:
        RETURN FALSE

    ELSE:
        IF div < number:        //Base Case

            IF number divided by div has no remainder
                RETURN FALSE

            ELSE
                RETURN RECURSIVE_PRIME (DIV + 1, NUMBER)

"""
