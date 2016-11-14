def count_factorial(n):

    factorial_list = []
    trail_zeros = 0
    result = 1

    for i in range (1, n+1):
        factorial_list.append(i)

    for x in factorial_list:
        result *= x

    for y in factorial_list:
        while y > 0:
            if y % 5 == 0:
                trail_zeros = trail_zeros + 1
                y = y/5
            else:
                break
                

    return result, trail_zeros


    

    
        
print(count_factorial(5))
