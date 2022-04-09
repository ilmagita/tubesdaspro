import arraytools as at


def topup(matriksuserdata):
    username = input("Masukkan username: ")
    saldoadded = int(input("Masukan saldo: "))

    baris = at.panjangarray(matriksuserdata)
    unameada = False

    for i in range(1, baris):
        if matriksuserdata[i][1] == username:
            unameada = True
            saldo = int(matriksuserdata[i][5])
            nama = matriksuserdata[i][2]
            break

    if not unameada:
        print(f'Username "{username}" tidak ditemukan.')
    else:
        if issaldoakhirvalid(saldo, saldoadded):
            saldoakhir = saldo + saldoadded
            matriksuserdata[i][5] = str(saldoakhir)
            print(f'Top up berhasil. Saldo {nama} bertambah menjadi {saldoakhir}.')
        else:
            print("Masukan tidak valid")
    return matriksuserdata

def issaldoakhirvalid(saldo, saldoadded):
    if saldo + saldoadded < 0:
        return False
    else:
        return True
