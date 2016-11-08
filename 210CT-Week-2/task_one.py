from math import sqrt

def perfect_square(n):
    answer = 0
    number_int = int(n)
    

    

    math_Count = (sqrt(number_int)) * (sqrt(number_int))
    square_root = sqrt(number_int)
    
    if math_Count == number_int:

        answer = square_root
        print ("This is a factorial number")
        print ("The root for your input value is: %d" % square_root)

    else:
        print ("Sorry that number is not a perfect square")

    return answer

  

print (perfect_square(205205625))
