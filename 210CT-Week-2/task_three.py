""" This solution is to solve the addition, subtraction, and multiplication of two matrices.
New functions will be defined where each addition, multiplication, and division will be calculated
separately."""


"""ADD_MATRIX (MAT_A, MAT_B)

    fin_result <- matrix list       // the list should be list inside list          (1)

    for row in range(length(MAT_A))	            // Iterate rows of both matrix     (n)

        for colm in range(length(MAT_A[0]))	  // Iterate Columns of both          (n * n)

            result [row][colm] <- MAT_A[row][colm] + MAT_B[row][colm]               (n * n)

    return fin_result            

ADD_MATRIX Big O Notation = O (2n ^ 2 + n + 2) = O (n ^ 2)

MULTIPLY_MATRIX (MAT_A, MAT_B)

    fin_result <- matrix list 					        //(1)

    for a in range(length(MAT_A))                                  //go through MAT_A row (n)

        for b in range(length(MAT_B[0]))                           //go through MAT_B colm (n * n)

            for c in range (length(MAT_B))                     //go through MAT_B row  (n * n * n)

                fin_result[a][b] <- MAT_A[a][c] * MAT_B[c][b]         //update result list (n * n * n)
    
return fin_result                                                                     // (1)     

MULTIPLY_MATRIX Big O Notation = O (2n ^ 3 + n ^ 2 + n + 2) = O(n ^ 3)

SINGLE_MULTIPLICATION (VALUE, MATRIX) // Multiply single digit with matrix

   fin_result <- matrix list                                                  //(1)

   for a in range(length(MATRIX))                                // go through MATRIX row (n)

        for b in range(length(MATRIX[0]))                    // go through MATRIX colm (n * n)

              result[a][b] = value * MATRIX[a][b]              // Update result list    (n * n)

   return fin_result                                                              //(1)             
  
SINGLE_MULTIPLICATION Big O Notation = O(2n ^ 2 + n + 2) = O (n ^ 2)

MATRIX_SUBTRACTION (MAT_A, MAT_B)

    fin_result = matrix list                                            // (1)

    for row in range(length (MAT_A))                             // go through MAT_A rows (n)

        for colm in range(length(MAT_A[0]))                   // go through MAT_B rows (n * n)

            fin_result[row][colm] = MAT_A[row][colm] – MAT_B[row][colm]      

                                // same matrix size row and colm can be applied to MAT_B(n * n)

    return result                                                    // (1)             

MATRIX_SUBTRACTION Big O Notation = O (2n ^ 2 + n + 2) = O (n ^ 2)

MATRIX_ONE <- [[1, 2, 3],
	      [2, 1, 2],
               [1, 2, 4]]

MATRIX_TWO <- [[2, 2, 2],
	      [1, 1, 1],
               [1, 2, 2]]

VALUE <- 2			// for SINGLE_MULTIPLICATION.


// Equation <- A <- B*C–2*(B+C)

set_one = output of MATRIX_MULTIPLICATION (MATRIX_ONE, MATRIX_TWO)  // MATRIX_A * MATRIX B
set_two = output of MATRIX_ADDITION (MATRIX_ONE, MATRIX_TWO)	  // MATRIX_A + MATRIX_B
set_three = output of SINGLE_MULTIPLICATION (2, A)		 // VALUE * (MATRIX_A + MATRIX_B)
final_set = output of MATRIX_SUBTRACTION (a, c)                  // set_one – set_three

"""
