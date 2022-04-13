import arraytools as at
import f02
import f04
import f05
import f06
import f07
import f08
import f09
import f10
import f11
import f12
import f13
import f14
import f16


def isperintahvalid(perintah):
    perintahvalid = ["register", "login", "tambah_game", "ubah_game", "ubah_stok", "list_game_toko",
                     "buy_game", "list_game", "search_my_game", "search_game_at_store", "topup", "riwayat",
                     "help", "save", "exit", "tictactoe"]
    for i in range(at.panjangarray(perintahvalid)):
        if perintah == perintahvalid[i]:
            return True
    return False


def isperintahadmin(perintah):
    perintahadmin = ["register", "login", "tambah_game", "ubah_game", "ubah_stok", "list_game_toko",
                     "search_game_at_store", "topup", "help", "save", "exit"]
    for i in range(at.panjangarray(perintahadmin)):
        if perintah == perintahadmin[i]:
            return True
    return False


def isperintahuser(perintah):
    perintahuser = ["login", "list_game_toko", "buy_game", "list_game", "search_my_game", "search_game_at_store",
                    "riwayat", "help", "save", "exit"]
    for i in range(at.panjangarray(perintahuser)):
        if perintah == perintahuser[i]:
            return True
    return False


def isadmin(loggeduserdata):
    if loggeduserdata[4] == "Admin":
        return True
    else:
        return False


def doperintahadmin(perintah, database, datauser):
    if isperintahadmin(perintah):
        if perintah == "register":
            database[0] = f02.register(database[0])
        elif perintah == "login":
            print("Anda sudah login.")
        elif perintah == "tambah_game":
            database[1] = f04.tambahgame(database[1])
        elif perintah == "ubah_game":
            database[1] = f05.ubahgame(database[1])
        elif perintah == "ubah_stok":
            database[1] = f06.ubah_stok(database[1])
        elif perintah == "list_game_toko":
            f07.listgametoko(database[1])
        elif perintah == "search_game_at_store":
            f11.search_game(database[1])
        elif perintah == "topup":
            database[0] = f12.topup(database[0])
        elif perintah == "help":
            f14.list_help(datauser)
        elif perintah == "save":
            f16.save(database)
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.", end=" ")
        print("Mintalah ke administrator untuk melakukan hal tersebut.")
    return database, datauser


def doperintahuser(perintah, database, datauser):
    if isperintahuser(perintah):
        if perintah == "login":
            print("Anda sudah login.")
        elif perintah == "list_game_toko":
            f07.listgametoko(database[1])
        elif perintah == "buy_game":
            Temp = f08.beligame(database, datauser)
            database = Temp[0]
            datauser = Temp[1]
        elif perintah == "list_game":
            f09.printlistgame(datauser, database[1], database[3])
        elif perintah == "search_my_game":
            f10.search_my_game(datauser, database[1], database[3])
        elif perintah == "search_game_at_store":
            f11.search_game(database[1])
        elif perintah == "riwayat":
            f13.riwayat(datauser, database[2])
        elif perintah == "help":
            f14.list_help(datauser)
        elif perintah == "save":
            f16.save(database)
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.", end="")
        print("Mintalah ke administrator untuk melakukan hal tersebut.")
    return database, datauser
