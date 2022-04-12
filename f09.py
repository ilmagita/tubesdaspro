import arraytools as at
import csvtools as csvt

# MASIH RADA BINGUNG DIKIT...

# owned = csvt.csvtoarray('CSVFiles\kepemilikan.csv')
# matriksgamedata = csvt.csvtoarray('CSVFiles\game.csv')

def list_game(matriksgamedata, owned):
    # driven data - DELETELATER!
    loggedUser = 1 # loggedUser = user.csv[1]

    # hitung berapa banyak GAME yang dimiliki oleh user di kepemilikan.csv
    
    ada = False
    ownedIDs = []
    for i in range (at.panjangarray(owned)):
        if owned[i][1] == loggedUser: # apabila game dimiliki oleh user ID yg sama dengan yg ter log in,
            ownedIDs = at.append(matriksgamedata, owned) # append id game yang dimiliki oleh user
            ada = True
    
    # fokus di  game.csv, cocokkan ID yang didapat dengan list game
    if ada:
        ownedGames = ['' for i in range(at.panjangarray(ownedIDs))]
        i = 0
        k = 0
        while i <= (at.panjangarray(ownedIDs)):
            if ownedIDs[i] in matriksgamedata:
                ownedGames[k] = matriksgamedata[i]
                k =+ 1
            i =+ 1
        at.printmatrix(ownedGames)
    else:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")