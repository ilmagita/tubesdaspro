from logging import RootLogger
import arraytools as at


def register(matriksuserdata):
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    baris = at.panjangarray(matriksuserdata)
    kolom = at.panjangarray(matriksuserdata[0])
    unamesama = False

    if not isunamevalid(username):
        print("Username yang dimasukkan tidak valid")
        print("Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")
    else: 
        for i in range(1, baris):
            if matriksuserdata[i][1] == username:
                unamesama = True
                print(f"Username {nama} sudah terpakai, silakan menggunakan username lain")
        
        if not unamesama:
            matriksuserbaru = ['' for i in range(kolom)]
            matriksuserbaru[0] = str(baris)
            matriksuserbaru[1] = username
            matriksuserbaru[2] = nama
            matriksuserbaru[3] = password
            matriksuserbaru[4] = "User"
            matriksuserbaru[5] = "0"
            matriksuserdata = at.append(matriksuserdata, [matriksuserbaru])
            print(f'Username {nama} telah berhasil register ke dalam "Binomo".')
        
        return matriksuserdata

def isunamevalid(uname):
    for i in uname:
        ac = ord(i)  # asciicode dari i
        if not (ac == 45 or 47 < ac < 58 or 64 < ac < 91 or ac == 95 or 96 < ac < 123):
            return False
    return True