"""
This is the coursework question 10 solutions. Where it asks us to create a sublist from a list.
The sublist should extract the sub-sequence of maximum length in an ascending order.

Input = [1, 2, 3, 4, 1, 2, 3, 1, 2]
Output = [1, 2, 3, 4]

"""

list_one = [1, 2, 3, 4, 5, 1, 2, 3, 2, 3, 5, 0, 4, 5, 7, 8, 10, 12, 13, 14, 15, 20]


def split_substring(split_list):

    first_elm = split_list[0]               # set the first element for comparison
    sub_list = [[first_elm]]                # set list inside list

    for elm in split_list[1:]:              # loop list starting from index 1
        if elm > first_elm:                 # compare if the element is bigger than first
            first_elm = elm                 # set the first_elm to current elm
            sub_list[-1].append(elm)        # append item to the last sub_list


        else:
            first_elm = elm
            sub_list.append([first_elm])    # creates new list inside sub_list list

    maximum_sublist = max(sub_list, key = len)  # sort the longest length in sub_list
    count_sublist = len(sub_list)               # count number of sublist created


    statement =  ("There are %d sub-list found from this list \nThe maximum substring in this set of list is: %s" % (count_sublist, maximum_sublist))

    return statement


print(split_substring(list_one))
