# Ex 1
from numpy.matrixlib.defmatrix import matrix


def print_matrix(matrix):
    for i in matrix:
        print(i)


# Ex 2
def make_matrix(side, height):
    matrix = []
    for i in range(side):
        line = []
        for j in range(height):
            line.append(0)
        matrix.append(line)
    return matrix


# Ex 3
def diagonal_matrix_to_one(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 1
    return matrix


# Ex 4
def counter_diagonal_matrix_to_one(matrix):
    for i in range(len(matrix)):
        matrix[i][(len(matrix)- 1)-i] = 1
    return matrix


# Ex 5
def under_above_diagonal_to_1(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j] = 1
    return matrix


# Ex 6
def transposed_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            aux = matrix [j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = aux
    return matrix

# Ex 8
def chess_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i+j)%2 == 0:
                matrix[i][j] = 1
    return matrix


# Ex 10
def covid_cinema(side):
    matrix = make_matrix(side, side)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i+j)%2==0:
                matrix[i][j]=1
    return matrix
matrix = covid_cinema(50)
print_matrix(matrix)

