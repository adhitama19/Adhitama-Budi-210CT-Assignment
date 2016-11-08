

import random
from random import randrange


def shuffle_number(numbers):
    empty_lst = []

    for i in numbers:
        empty_lst.append(i)

    for x in empty_lst:
        random_index = randrange(0, len(empty_lst))
        random_object = random.choice(empty_lst)
        empty_lst.insert(random_index, empty_lst.pop(x))

    return empty_lst

n = [1, 2, 3, 4, 5, 6]

print(shuffle_number(n))
