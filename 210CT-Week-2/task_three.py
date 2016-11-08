def matrix_Addition (b, c):


    result = [[0,0],
              [0,0],
              [0,0]]

    

    for row in range(len(b)):
        for column in range (len(c)):
            result [row][column] = b[row][column] + c[row][column]

    for r in result:
        print (result)

    return result


matrix_b = [[12, 14],
            [15, 2],
            [3, 7]]

matrix_c = [[2, 3],
            [5, 13],
            [2, 7]]


print(matrix_Addition(matrix_b, matrix_c))

"""or this

list_a = [1, 2,
          3, 4]

list_b = [1, 2,
          3, 4]

answer = [ ]

for a, b in zip(list_a, list_b):
    count = a + b
    answer.append(count)

print (answer)"""
