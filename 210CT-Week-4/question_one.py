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
