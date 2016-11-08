def asc_Sequence (n):
    list_one = []

    for i in n:
        list_one.append(i)

    for x in n:
        if x == max(list_one):
            index_max = list_one.index(max(list_one))
            list_one[0] = list_one[index_max]
            
        

    return list_one

    

    


list_n = [12, 45, 33, 53]

print(asc_Sequence(list_n))
