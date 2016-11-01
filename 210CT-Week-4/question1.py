def binarySearch(alist, low, high, item):         #This will create Binary Search function with its parameters.
    first = 0                                     #This is the first value of the list
    last = len(alist)-1                           #The last value for a list
    found = False                                 #Found is set as false so while loop can then run

    while first <= last and not found:            #While loop which indicates while first number is less tahn or equal to last and true.
        midpoint = (first + last)//2              #set the mid point
        lowVal = low < item                       #This will be the low set interval
        highVal = high > item                     # This will be the high set interval
        if alist[midpoint] == item:               #statement if midpoint is equal with the item return True
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint+1

    return found

list_One = [2, 3, 4, 5, 6, 10, 11, 12]
low = 9
high = 11
item = 10

print(binarySearch(list_One, low, high, item))

