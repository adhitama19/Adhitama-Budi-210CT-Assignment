""" This is the solution for week 1 question 2. The question ask us to count the number of trailing zero's in
    a factorial number. First of all i defined my function as count_factorial with n as the parameter. this
    function will output the value of the factorial and count the trailing zero's of that value."""




def count_factorial(number): # count_factorial function is defined with n as the parameters

    factorial_list = [] # empty list which will have a value range from 1 to n
    total_zeros = 0     # conditions which will be used to count how many trail zero's
    result = 1          # conditions to count the factorial of the n value

    for i in range (1, number+1):      # a for loop that will go through from range 1 to n value
        factorial_list.append(i)  # the i value will be appended to the factorial_list empt list

    for val in factorial_list:    # a for loop that will go through appended factorial list
        result *= val             # conditions update results by multiplying results with val

    for val in factorial_list:    # a for loop that will go through factorial_list to count the trail zero's
        while val > 0:            # a while loop to check if val is bigger than zero
            if val % 5 == 0:      # conditional statements to check if the remainder of the divisions is zero
                total_zeros = total_zeros + 1  # the condition to update total_zeroes if the divisions remainder is equal to zero
                val = val/5                    
    
            else:                 # else statement if the remainders conditions is not true
                break             # break statement to terminates the loop if the remainder is not zero


    if number < 20:
        print ("The factorial for this value is: %d" % (result))
        print ("and the trailing zero's for this value is: %d" % (total_zeros))
        

    else:
        print (total_zeros)


    

    
        
count_factorial(15)
