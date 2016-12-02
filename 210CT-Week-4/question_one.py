""" This is the solution for coursework question 9. It ask us to create a Binary Search Algorithm
    and instead of outputing a value is found. We should set a range interval to check if there is 
    a value between the range we set.
    
    [1, 2, 3, 4, 5]
    Input = low = 2 High = 4
    Output = True
"""

def binarySearch(alist, low, high):         
    first = 0                                    
    last = len(alist)-1                           
    found = False                                 

    while first <= last and not found:                          
        midpoint = (first + last)//2            # find the midpoint
            
        if alist[midpoint] > low and alist[midpoint] < high:    # check if there is elements between low and high
                found = True
            
        else:
            if alist[midpoint] > low :                          # if element bigger than low input
                    last = midpoint - 1                         # search from first up to midpoint-1
            else:                                               # if element smaller than low
                first = midpoint + 1                            # search from midpoint+1 to last

        
    return found

list_One = [2, 3, 4, 5, 6, 10, 11, 12, 14]
userInput_low = int(input("Please enter a low: "))
userInput_high = int(input("Please enter a high: "))

print(binarySearch(list_One, userInput_low, userInput_high))


"""
PSEUDOCODE:

BINARYSEARCH (LISTN, LOW, HIGH)

    first <- 0                                                          // (1)
    last <- length(LISTN) - 1                                           // (1)
    found <- FALSE                                                      // (1)

    WHILE first <= last AND NOT found                                   // (n)
        count the midpoint index                                        // (n)
        
        if midpoint element > LOW AND midpoint element < HIGH           // (n)
            found <- TRUE                                               // (n)
        
        else                                                            // (n)
            if midpoint element > low                                   // (n)
                set the midpoint as the maximum boundaries  //last      // (log n)
            else                                                        // (n)
                set midpoint as starting point  //first                 // (log n)
    
    return found                                                        // (n)

list_One <- [2, 3, 4, 5, 6, 7, 8]
userInput_low <- set int input for low
userInput_high <- set int input for high

print(BINARYSEARCH(LISTN, USERINPUT_LOW, USERINPUT_HIGH)

Big O Notation = O (2 log n + 8n + 3)
Big O Notation = O (log n)

"""
