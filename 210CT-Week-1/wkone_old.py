from random import *

def shuffle_number(numbers):
    empty_lst = []

    for i in numbers:
        empty_lst.append(i)

    empty_lst.insert(4, empty_lst.pop(3))
    empty_lst.insert(3, empty_lst.pop(2))
    empty_lst.insert(0, empty_lst.pop(4))



    return empty_lst


iseng = [1, 2, 3, 4, 5]

print(shuffle_number(iseng))
