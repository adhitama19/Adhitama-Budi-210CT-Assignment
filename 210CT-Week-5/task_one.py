list_one = [1, 2, 3, 4, 5, 1, 2, 3, 2, 3, 5]


def split_substring(split_list):

    first_elm = split_list[0]
    sub_list = [[first_elm]]

    for elm in split_list[1:]:
        if elm > first_elm:
            first_elm = elm
            sub_list[-1].append(elm)
            

        else:
            first_elm = elm
            sub_list.append([first_elm])

    maximum_sublist = max(sub_list, key = len)
    count_sublist = len(sub_list)

    
    print ("There are %d sub-list found from this list" % count_sublist)
    print ("The maximum substring in this set of list is: %s" % maximum_sublist)
    return sub_list
    


print(split_substring(list_one))
