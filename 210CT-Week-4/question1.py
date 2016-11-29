def binarySearch(alist, low, high):         
    first = 0                                    
    last = len(alist)-1                           
    found = False                                 

    while first <= last and not found:           
        midpoint = (first + last)//2
            
        if alist[midpoint] > low and alist[midpoint] < high:
                found = True
            
        else:
            if alist[midpoint] > low :
                    last = midpoint - 1
            else:
                first = midpoint + 1

        
    return found

list_One = [2, 3, 4, 5, 6, 10, 11, 12, 14]
low = 15
high = 16

print(binarySearch(list_One, low, high))
