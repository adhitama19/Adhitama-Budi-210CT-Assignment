""" This is the solution for week 1 question 2. The question ask us to count the number of trailing zero's in
    a factorial number. I begin by counting the factorial then continued with the trailing zero's.

    The code input will be an integer, and the output will be the factorial and trailing zero's of the value.

    Input: 5
    Output: The factorial for this value is: 120, and the trailing zeros for this value is: 1

    Input: 21
    Output: The trailing zeros for this value is: 4

    
"""




def count_factorial(number): 

    numberInt = int(number)
    factorial_list = [] 
    total_zeros = 0     
    result = 1          

    for num in range (1, numberInt+1):      
        factorial_list.append(num)              # the range from 1 to number appended to empty list  

    for elm in factorial_list:    
        result *= elm                           # do multiplication for each element           

    for elm in factorial_list:    
        while elm > 0:            
            if elm % 5 == 0:      
                total_zeros = total_zeros + 1  
                elm = elm/5                     # to stop while, when "if" condition true                    
    
            else:                 
                break                           # to stop infinity loop when "if" is not true            


    if number < 20:                             # to return the factorial of a number if less than 20
        statement_less = ("The factorial for this value is: %d \nand the trailing zeros for this value is: %d" % (result,total_zeros ))
        return (statement_less)

    else:                                       # to return only the trailing zeros if input is more than 20
        statement_more = ("The trailing zero's for this value is: %d" % (total_zeros))
        return (statement_more)

    return 




    

    
        
print(count_factorial(21))
