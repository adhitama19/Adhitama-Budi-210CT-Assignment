from math import sqrt

def fact_number(number):

    perfect_square = []
    yang_disamain = []
    n_int = int(number)


    for i in range (1, number):
            new_val = i * i
            perfect_square.append(new_val)

    if number in perfect_square:
        return sqrt(number)

    else:
        final_val = perfect_square[-1]
        final_Ans = sqrt(final_val)
        return sqrt(final_Ans)


print (fact_number(36))
