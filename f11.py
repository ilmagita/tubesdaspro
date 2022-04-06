import arraytools as at


def search_game(matriksgamedata):
    gameid = input("Masukkan ID Game: ")
    nama = input("Masukkan Nama Game: ")
    harga = input("Masukkan Harga: ")
    kategori = input("Masukkan Kategori: ")
    tahun_rilis = input("Masukkan Tahun Rilis: ")

    arrayoffilter = [gameid, nama, kategori, tahun_rilis,  harga]
    filtereddata = [matriksgamedata[0]]
    kolom = at.panjangarray(arrayoffilter)
    matrikskosong = [['' for i in range(kolom)]]
    k = 1
    ada = False
    for i in range(1, kolom):
        j = 0
        memenuhi = True
        while j < kolom and memenuhi:
            if arrayoffilter[j]:
                if arrayoffilter[j] != matriksgamedata[i][j]:
                    memenuhi = False
            j += 1
        if memenuhi:
            filtereddata = at.append(filtereddata, matrikskosong)
            filtereddata[k] = matriksgamedata[i]
            k += 1
            ada = True

    if ada:
        at.printmatrix(filtereddata)
    else:
        print("Tidak ada game di toko yang memenuhi kriteria")
