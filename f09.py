import arraytools as at
import csvtools as csvt


# MASIH RADA BINGUNG DIKIT...

# owned = csvt.csvtoarray('CSVFiles\kepemilikan.csv')
# matriksgamedata = csvt.csvtoarray('CSVFiles\game.csv')


def list_ownedgame(loggeduserdata, matriksgamedata, owned):
    # driven data - DELETELATER!
    loggedUser = loggeduserdata[0]  # loggedUser = user.csv[1]

    # hitung berapa banyak GAME yang dimiliki oleh user di kepemilikan.csv

    ownedIDs = []
    for i in range(at.panjangarray(owned)):
        if owned[i][1] == loggedUser:  # apabila game dimiliki oleh user ID yg sama dengan yg ter log in,
            ownedIDs = at.append(ownedIDs, [owned[i][0]])  # append id game yang dimiliki oleh user

    # fokus di  game.csv, cocokkan ID yang didapat dengan list game
    ownedGames = ['' for i in range(at.panjangarray(ownedIDs)+1)]
    ownedGames[0] = matriksgamedata[0]
    if ownedIDs:
        i = 0
        k = 0
        while k < (at.panjangarray(ownedIDs)):
            if ownedIDs[k] == matriksgamedata[i][0]:
                ownedGames[k+1] = matriksgamedata[i]
                k += 1
                i = 0
            i += 1

    return ownedGames


def printlistgame(loggeduserdata, matriksgamedata, owned):
    ownedgame = list_ownedgame(loggeduserdata, matriksgamedata, owned)

    if at.panjangarray(ownedgame) == 1:
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
    else:
        at.printmatrix(ownedgame)
