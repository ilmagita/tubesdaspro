import arraytools as AT


def csvtoarray(file):
    # Definisi dan Spesifikasi
    # Menerima nama file CSV lalu membuat matrix (array of array) berdasarkan isi csv tersebut

    # KAMUS LOKAL
    #

    # ALGORITMA
    openedfile = open(f'CSVFiles/{file}', 'r')
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


def writecsv(matrix, namafile):
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

    openedfile = open(f'CSVFiles/{namafile}', 'w')
    openedfile.write(string)
    openedfile.close()

    # Aplikasi
    # writecsv(userdata, 'user.csv')
