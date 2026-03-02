def rotate_matrix(matrix):
    n = len(matrix)

    # Transpose--------to change something from one position to the another position
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse rows
    for row in matrix:
        row.reverse()

    return matrix

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))

# output : [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
