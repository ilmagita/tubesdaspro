import csvtools as csvt
import arraytools as at
import f04
import f05
import f06
import f07
import f11


namafolder = input()
while not csvt.isfoldervalid(namafolder):
    print(f'Folder "{namafolder}" tidak ditemukan\n')
    namafolder = input()

userdata = csvt.csvtoarray(namafolder, 'user.csv')
gamedata = csvt.csvtoarray(namafolder, 'game.csv')
riwayatdata = csvt.csvtoarray(namafolder, 'riwayat.csv')
kepemilikandata = csvt.csvtoarray(namafolder, 'kepemilikan.csv')


# Akses Perintah:
# User : F3, F7, F8, F9, F10, F11, F13, F14, F16, F17
# Admin : F2, F3, F4, F5, F6, F7, F11, F12, F14, F16, F17

stop = False

while not stop:
    perintah = input(">>> ")
    if perintah == "tambah_game":
        gamedata = f04.tambahgame(gamedata)
    elif perintah == "ubah_game":
        gamedata = f05.ubahgame(gamedata)
    elif perintah == "ubah_stok":
        gamedata = f06.ubah_stok(gamedata)
    elif perintah == "list_game_toko":
        f07.listgametoko(gamedata)
    elif perintah == "search_game_at_store":
        f11.search_game(gamedata)
    else:
        stop = True
        print("Terima kasih telah menggunakan BNMO")
