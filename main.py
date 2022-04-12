import csvtools as csvt
import arraytools as at
import f15
import maintools as mt
import f03
import f17


database = f15.load()

# Akses Perintah:
# User : F3, F7, F8, F9, F10, F11, F13, F14, F16, F17
# Admin : F2, F3, F4, F5, F6, F7, F11, F12, F14, F16, F17

stop = False
haslogin = False
logindata = []
loggeduserdata = []

while not stop:
    perintah = input("\n>>> ")
    if perintah == "printdata":
        for i in range(4):
            at.printmatrix(database[i])
    elif mt.isperintahvalid(perintah):
        if haslogin:
            if perintah == "exit":
                stop = f17.exit(database)
                print('Terima kasih telah menggunakan "Binomo"')
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
