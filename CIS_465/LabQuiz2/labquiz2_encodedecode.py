import cv2
import numpy as np


def encode_matrix(array):
    new_matrix = []
    # print("enter elements: ")
    # initialize array size
    row = len(array)
    col = len(array[0])

    # matrix encode
    for i in range(0, row):
        new_array = []
        for j in range(0, col):

            # first and last row and column ignored
            if i in (0, row - 1) or j in (0, col - 1):
                new_array.insert(len(new_array), matrix[i][j])
            else:
                # 3x3 surrounding matrix
                matrixOfThree = [[matrix[i - 1][j - 1] - matrix[i][j],
                                  matrix[i - 1][j] - matrix[i][j],
                                  matrix[i - 1][j + 1] - matrix[i][j]],
                                 [matrix[i][j - 1] - matrix[i][j],
                                  matrix[i][j], matrix[i][j + 1] - matrix[i][j]],
                                 [matrix[i + 1][j - 1] - matrix[i][j],
                                  matrix[i + 1][j] - matrix[i][j],
                                  matrix[i + 1][j + 1] - matrix[i][j]]]

                # setting binary numbers
                for k in range(0, 3):
                    for l in range(0, 3):
                        if k != 1 or l != 1:
                            if matrixOfThree[k][l] >= 0:
                                matrixOfThree[k][l] = 1
                            else:
                                matrixOfThree[k][l] = 0
                # binary string
                binary_string = str(matrixOfThree[0][0]) \
                                + str(matrixOfThree[1][0]) \
                                + str(matrixOfThree[2][0]) \
                                + str(matrixOfThree[2][1]) \
                                + str(matrixOfThree[2][2]) \
                                + str(matrixOfThree[1][2]) \
                                + str(matrixOfThree[0][2]) \
                                + str(matrixOfThree[0][1])

                # getting the integer value
                integer_val = int(binary_string, 2)
                # input the value to the new matrix
                new_array.insert(len(new_array), integer_val)
        new_matrix.insert(len(new_matrix), new_array)
    return new_matrix


# gettinng rows and columns from user
row = cv2.imread('CSU_greyscale170.jpg')
col = cv2.imread('CSU_greyscale170.jpg')
matrix = []
cv2.imshow('HORIZONTAL',row)
cv2.imshow('VERTICAL',col)

# getting the elements from the user
for i in range(0, row):
    new_array = []
    for j in range(0, col):
        new_array.insert(len(new_array), int(input()))
        matrix.insert(len(matrix), new_array)

# encoding the matrix
new_matrix = encode_matrix(matrix)
# encoded matrix
print('encoded matrix: ')
for k in range(0, len(new_matrix)):
    for l in range(0, len(new_matrix[0])):
        print(str(new_matrix[k][l]), end="")

print("")
