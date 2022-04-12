import arraytools as at


def login(matriksuserdata):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    baris = at.panjangarray(matriksuserdata)
    berhasil = False
    unameada = False
    passwordbenar = False
    userdatabase = []

    for i in range(1, baris):
        if matriksuserdata[i][1] == username:
            unameada = True
            if matriksuserdata[i][3] == password:
                passwordbenar = True
                userdatabase = matriksuserdata[i]
                berhasil = True
            break
    
    if not unameada or not passwordbenar:
        print("Password atau username salah atau tidak ditemukan")
    else:
        nama = userdatabase[2]
        print(f'Halo {nama}! Selamat datang di "Binomo"')
    return berhasil, userdatabase
