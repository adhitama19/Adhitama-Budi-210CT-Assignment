""" This is the question 3 coursework solution. It asks us to returns the highest perfect square of a value.
    If the value does not have the perfect square, it should return the lower highest perfect square of that
    value.

    Input: 16
    Output: 4

    Input: 20
    Output: 4


"""



def fact_number(number):

    perfect_square = []


    for i in range (1, number):
            new_val = (i * i)                               
            perfect_square.append(new_val)                                  # numbers that have perfect square appended to perfect_square list

    if number in perfect_square:
        sqrt = int(number ** (0.5))                                         # to get the perfect square of the number
        statereturn = ("The square root for your value is: %d" % (sqrt))
        return (statereturn)

    else:
        final_Val = perfect_square[-1]                                      # get the last element from perfect square list
        final_Sqrt = int((final_Val ** 0.5) ** 0.5)                         # to get the square root that is less than input number                         
        final_ans = final_Sqrt

        statereturn = ("The perfect square of the number less than the input is: %d" % (final_ans))         # statement that is returned when the input value is not perfect square
        return (statereturn)

    return




print(fact_number(20))


"""

PSEUDOCODE:


FACT_NUMBER (NUMBER)

    perfect_square <- []

    FOR i <- 1 to number
        new_val <- (i * i)
        new_val appended to perfect_square empty list

    IF number is inside perfect_square
        do square root calculation
        return square root of the number //output

    ELSE number is not in perfect_square
        final_Val <- perfect_square[-1] //get final value from list
        do square root calculation
        final_ans <- final_Sqrt
        return the square root that is less from number //output



"""
