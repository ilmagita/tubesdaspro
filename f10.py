import arraytools as at
import f09

# owned = csvt.csvtoarray('CSVFiles\kepemilikan.csv')
# matriksgamedata = csvt.csvtoarray('CSVFiles\game.csv')


def search_my_game(loggeduserdata, matriksgamedata, owned):
    gameid = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")

    ownedgames = f09.list_ownedgame(loggeduserdata, matriksgamedata, owned)

    # Menghilangkan kolom stok
    kolom = at.panjangarray(ownedgames[0]) - 1
    baris = at.panjangarray(ownedgames)

    tanpa_stok = [['' for i in range(kolom)] for j in range(baris)]

    for i in range(baris):
        for j in range(kolom):
            tanpa_stok[i][j] = ownedgames[i][j]

    # skema pencarian dan pengeprintan
    array = [tanpa_stok[0]]  # inisialisasi
    found = False
    print("Daftar game pada inventory yang memenuhi kriteria:")

    if gameid and tahun_rilis:
        for i in range(at.panjangarray(ownedgames)):
            if ownedgames[i][3] == tahun_rilis and ownedgames[i][0] == gameid:
                array = at.append(array, [tanpa_stok[i]])
                found = True
    elif gameid:
        for i in range(at.panjangarray(ownedgames)):
            if ownedgames[i][0] == gameid:
                array = at.append(array, [tanpa_stok[i]])
                found = True
    elif tahun_rilis:
        for i in range(at.panjangarray(ownedgames)):
            if ownedgames[i][3] == tahun_rilis:
                array = at.append(array, [tanpa_stok[i]])
                found = True
    else:
        array = tanpa_stok
    # semua list game yang dimiliki user

    if found:
        at.printmatrix(array)
    else:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")