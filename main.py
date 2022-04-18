# Main Program dari Binomo

# KAMUS
# perintah : string
# stop, haslogin : boolean
# loggeduserdata : array of string
# database : array of array of array of array of string
# datasementara : array of [database, loggeduserdata]

# File yang diimport
import arraytools as at
import maintools as mt
import f03
import f15
import f17
# import b03


# Loading Database dengan memanggil fungsi load
database = f15.startsystem()  # database = [userdata, gamedata, riwayatdata, kepemilikandata]

stop = False  # Variabel untuk mengecek apakah program tetap dijalankan
haslogin = False  # Variabel untuk mengecek apakah pengguna sudah melakukan login

while not stop:  # Program akan selalu berjalan selama stop bernilai False
    perintah = input("\n>>> ")
    if perintah == "printdata":
        print(loggeduserdata)
        print()
        for i in range(4):
            at.printmatrix(database[i])
            print()
    elif mt.isperintahvalid(perintah):  # Mengecek apakah perintah yang dimasukkan valid
        if haslogin:
            if perintah == "exit":
                stop = f17.exit(database)
                print('Terima kasih telah menggunakan "Binomo"')
            # elif perintah == "tictactoe":
            #     b03.tictactoe()
            elif mt.isadmin(loggeduserdata):
                datasementara = mt.doperintahadmin(perintah, database, loggeduserdata)
                database = datasementara[0]
                loggeduserdata = datasementara[1]
            else:
                datasementara = mt.doperintahuser(perintah, database, loggeduserdata)
                database = datasementara[0]
                loggeduserdata = datasementara[1]
        else:
            if perintah == "login":
                logindata = f03.login(database[0])
                if logindata[0]:
                    haslogin = True
                    loggeduserdata = logindata[1]
            else:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    else:
        print("Perintah yang dimasukkan tidak valid!")
