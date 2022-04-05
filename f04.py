import csvtools as csvt
import arraytools as at


def tambahgame(matriksgamedata):
    print(">>> tambah_game")
    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok_awal = input("Masukkan stok awal: ")

    baris = at.panjangarray(matriksgamedata)
    kolom = at.panjangarray(matriksgamedata[0])
    panjangid = at.panjangarray(str(baris))

    if nama and kategori and tahun_rilis and harga and stok_awal:
        matriksgamedata += [['' for i in range(kolom)]]

        id = 'GAME'
        for i in range(3 - panjangid):
            id += '0'
        id += str(baris)

        matriksgamedata[baris][0] = id
        matriksgamedata[baris][1] = nama
        matriksgamedata[baris][2] = kategori
        matriksgamedata[baris][3] = tahun_rilis
        matriksgamedata[baris][4] = harga
        matriksgamedata[baris][5] = stok_awal
        csvt.writecsv(matriksgamedata, 'tes.csv')
    else:
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        tambahgame(matriksgamedata)


tambahgame(csvt.csvtoarray('game.csv'))
