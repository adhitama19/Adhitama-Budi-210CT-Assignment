def count_factorial(n):

    factorial_list = []
    result = 1

    for i in range (1, n+1):
        factorial_list.append(i)

    for x in factorial_list:
        result *= x

    return result
        
print(count_factorial(10))
