def panjangarray(array):
    panjang = 0
    for i in array:
        panjang += 1
    return panjang


def append(array1, array2):
    return array1 + array2


def printmatrix(matrix):
    baris = panjangarray(matrix)
    kolom = panjangarray(matrix[0])
    maxlencolumn = [0 for i in range(kolom+1)]
    maxlencolumn[0] = panjangarray(str(baris-1))
    for i in range(kolom):
        maks = panjangarray(matrix[1][i])
        for j in range(2, baris):
            if maks < panjangarray(matrix[j][i]):
                maks = panjangarray(matrix[j][i])
        maxlencolumn[i+1] = maks

    for i in range(1, baris):
        print(str(i) + "." + (" " * (maxlencolumn[0] - panjangarray(str(i)))), end=" ")
        for j in range(kolom):
            data = matrix[i][j]
            if (j+1) != kolom:
                print(data + (" " * (maxlencolumn[j + 1] - panjangarray(data))), end=" | ")
            else:
                print(data + (" " * (maxlencolumn[j + 1] - panjangarray(data))))
