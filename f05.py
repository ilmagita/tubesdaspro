import csvtools as csvt
import arraytools as at


def ubahgame(matriksgamedata):
    id = input("Masukkan ID game: ")
    banyakbaris = at.panjangarray(matriksgamedata)

    if isidvalid(id, matriksgamedata):
        i = 0
        Found = False
        while i < banyakbaris and not Found:
            if matriksgamedata[i][0] == id:
                Found = True
                nama = input("Masukkan nama game: ")
                kategori = input("Masukkan kategori: ")
                tahun_rilis = input("Masukkan tahun rilis: ")
                harga = input("Masukkan harga: ")

                if nama:
                    matriksgamedata[i][1] = nama
                if kategori:
                    matriksgamedata[i][2] = kategori
                if tahun_rilis:
                    matriksgamedata[i][3] = tahun_rilis
                if harga:
                    matriksgamedata[i][4] = harga
            else:
                i += 1
        print("Data Game berhasil diubah")
        return matriksgamedata
    else:
        print("Tidak ada game dengan ID tersebut!")
        return matriksgamedata

    # Aplikasi
    # ubahgame(csvt.csvtoarray('game.csv'))


def isidvalid(id, matriksgamedata):
    banyakbaris = at.panjangarray(matriksgamedata)
    for i in range(banyakbaris):
        if matriksgamedata[i][0] == id:
            return True
    return False
