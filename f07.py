import arraytools as at


def listgametoko(matriksgamedata):
    filterlist = input("Skema sorting: ")
    banyakbaris = at.panjangarray(matriksgamedata)
    if filterlist == "tahun+":
        at.printmatrix(filtertahunplus(matriksgamedata, banyakbaris))
    elif filterlist == "tahun-":
        at.printmatrix(filtertahunminus(matriksgamedata, banyakbaris))
    elif filterlist == "harga+":
        at.printmatrix(filterhargaplus(matriksgamedata, banyakbaris))
    elif filterlist == "harga-":
        at.printmatrix(filterhargaminus(matriksgamedata, banyakbaris))
    else:
        print("Skema sorting tidak valid!")


def filtertahunplus(matriks, banyakbaris):
    for i in range(1, banyakbaris-1):
        itahunmin = i
        tahunmin = int(matriks[itahunmin][3])
        for j in range(i+1, banyakbaris):
            if int(matriks[j][3]) < tahunmin:
                itahunmin = j
                tahunmin = int(matriks[j][3])
        temp = matriks[i]
        matriks[i] = matriks[itahunmin]
        matriks[itahunmin] = temp
    return matriks


def filtertahunminus(matriks, banyakbaris):
    for i in range(1, banyakbaris - 1):
        itahunmax = i
        for j in range(i + 1, banyakbaris):
            if int(matriks[j][3]) > int(matriks[itahunmax][3]):
                itahunmax = j
        temp = matriks[i]
        matriks[i] = matriks[itahunmax]
        matriks[itahunmax] = temp
    return matriks


def filterhargaplus(matriks, banyakbaris):
    for i in range(1, banyakbaris - 1):
        ihargamin = i
        for j in range(i + 1, banyakbaris):
            if int(matriks[j][4]) < int(matriks[ihargamin][4]):
                ihargamin = j
        temp = matriks[i]
        matriks[i] = matriks[ihargamin]
        matriks[ihargamin] = temp
    return matriks


def filterhargaminus(matriks, banyakbaris):
    for i in range(1, banyakbaris - 1):
        ihargamax = i
        for j in range(i + 1, banyakbaris):
            if int(matriks[j][4]) > int(matriks[ihargamax][4]):
                ihargamax = j
        temp = matriks[i]
        matriks[i] = matriks[ihargamax]
        matriks[ihargamax] = temp
    return matriks
