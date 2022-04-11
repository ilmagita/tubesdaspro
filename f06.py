import arraytools as at
import csvtools as csvt


def ubah_stok(matriksgamedata):
    id = input("Masukkan ID game: ")
    banyakbaris = at.panjangarray(matriksgamedata)

    if isidvalid(id, matriksgamedata):
        for i in range(banyakbaris):
            if matriksgamedata[i][0] == id:
                nama = matriksgamedata[i][1]
                stok = int(matriksgamedata[i][5])
                addedstock = int(input("Masukkan jumlah: "))
                if isstockvalid(stok, addedstock):
                    stok += addedstock
                    matriksgamedata[i][5] = str(stok)
                    if addedstock >= 0:
                        print(f"Stok game {nama} berhasil ditambahkan. Stok sekarang: {stok}")
                    else:
                        print(f"Stok game {nama} berhasil dikurangi. Stok sekarang: {stok}")
                    return matriksgamedata
                else:
                    print(f"Stok game {nama} gagal dikurangi karena stok kurang. Stok sekarang: {stok}")
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


def isstockvalid(jumlahstok, tambahanstok):
    if jumlahstok + tambahanstok < 0:
        return False
    return True
