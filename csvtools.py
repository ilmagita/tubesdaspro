import arraytools as AT
import os


def csvtoarray(namafolder, namafile):
    # Definisi dan Spesifikasi
    # Menerima nama file CSV lalu membuat matrix (array of array) berdasarkan isi csv tersebut

    # KAMUS LOKAL
    #

    # ALGORITMA
    openedfile = open(f'{namafolder}/{namafile}', 'r')
    string = openedfile.read()
    openedfile.close()

    banyakbaris = 0
    banyakkolom = 0

    for i in string:
        if i == ';' and banyakbaris == 0:
            banyakkolom += 1
        elif i == '\n':
            banyakbaris += 1
    banyakkolom += 1

    matrix = [['' for i in range(banyakkolom)] for j in range(banyakbaris)]
    indexkolom = 0
    indexbaris = 0

    for i in string:
        if i == '\n':
            indexbaris += 1
            indexkolom = 0
        elif i == ';':
            indexkolom += 1
        else:
            matrix[indexbaris][indexkolom] += i
    return matrix

    # Aplikasi
    # userdata = csvtoarray('user.csv')


def writecsv(matrix, namafolder, namafile):
    banyakbaris = AT.panjangarray(matrix)
    banyakkolom = AT.panjangarray(matrix[0])

    string = ''

    for i in range(banyakbaris):
        for j in range(banyakkolom):
            string += str(matrix[i][j])
            if j != (banyakkolom - 1):
                string += ';'
        if i != (banyakbaris - 1):
            string += '\n'

    print("Saving...")

    if not isfoldervalid(namafolder):
        os.makedirs(namafolder)

    openedfile = open(f'{namafolder}/{namafile}', 'w')
    openedfile.write(string)
    openedfile.close()

    print(f"Data telah disimpan pada folder {namafolder}")

    # Aplikasi
    # writecsv(userdata, 'CSVFiles', 'user.csv')


def isfoldervalid(namafolder):
    folderpython = os.getcwd()
    foldertujuan = os.path.join(folderpython, rf'{namafolder}')
    if not os.path.exists(foldertujuan):
        return False
    else:
        return True
