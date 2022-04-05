def printmatrix(matrix):
    for i in range(panjangarray(matrix)):
        for j in range(panjangarray(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


def panjangarray(array):
    panjang = 0
    for i in array:
        panjang += 1
    return panjang

