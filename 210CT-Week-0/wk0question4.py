def deletestring (letter, i, n):
    list_string = list(letter)
    del_1 = list_string.pop(i)
    del_2 = list_string.pop(n)
    string_join = "".join(list_string)
    return (string_join)
    
    


new_let = "Beautiful"
i = 4
n = 3

print (deletestring(new_let, 4, 3))
