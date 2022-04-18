import arraytools as at

# owned = csvt.csvtoarray('CSVFiles\kepemilikan.csv')
# matriksgamedata = csvt.csvtoarray('CSVFiles\game.csv')
# riwayat = csvt.csvtoarray('CSVFiles\riwayat.csv')


def riwayat(loggeduserdata, datariwayat):
    # driven data
    loggedUser = loggeduserdata[0]  # loggedUser = user.csv[1]

    # berapa banyak game yang dimiliki user?
    dipunya = 0
    ada = False
    for i in range(at.panjangarray(datariwayat)):
        if datariwayat[i][3] == loggedUser:
            dipunya += 1
            ada = True

    # oke sekarang kita ambil game yang dimiliki user dan diprint
    if ada:
        riwayatBeli = ['' for i in range(dipunya)]  # inisialisasi
        i = 0
        k = 0
        while i <= at.panjangarray(datariwayat):
            if datariwayat[i][3] == loggedUser:  # apabila game dimiliki oleh user ID yg sama dengan yg ter log in,
                riwayatBeli[k] = datariwayat[i]  # append game yang dimiliki oleh user di iterasi ke-i
                k += 1
            i += 1
        at.printmatrix(riwayatBeli)
    else:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game")