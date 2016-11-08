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
