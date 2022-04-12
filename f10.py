import arraytools as at
import csvtools as csvt

# owned = csvt.csvtoarray('CSVFiles\kepemilikan.csv')
# matriksgamedata = csvt.csvtoarray('CSVFiles\game.csv')

def search_my_game(matriksgamedata, owned):
    gameid = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")

    # driven data - DELETELATER!
    loggedUser = 1 # loggedUser = user.csv[1]

    # hitung berapa banyak GAME yang dimiliki oleh user di kepemilikan.csv
    ada = False
    ownedIDs = []
    for i in range (at.panjangarray(owned)):
        if owned[i][1] == loggedUser: # apabila game dimiliki oleh user ID yg sama dengan yg ter log in,
            ownedIDs = at.append(matriksgamedata, owned) # append id game yang dimiliki oleh user
            ada = True

    # skema pencarian dan pengeprintan
    array = [] # inisialisasi
    found = False
    print("Daftar game pada inventory yang memenuhi kriteria:")
    if ada:
        if gameid and tahun_rilis:
            if gameid in ownedIDs:
                for i in at.panjangarray(matriksgamedata):
                    if matriksgamedata[i][3] == tahun_rilis and matriksgamedata[i][0] == gameid:
                        array = at.append(array, [matriksgamedata[i][0], matriksgamedata[i][1], matriksgamedata[i][4], matriksgamedata[i][2], matriksgamedata[i][3]])
                        found = True
        elif gameid:
            if gameid in ownedIDs:
                for i in at.panjangarray(matriksgamedata):
                    if matriksgamedata[i][0] == gameid:
                        array = at.append(array, [matriksgamedata[i][0], matriksgamedata[i][1], matriksgamedata[i][4], matriksgamedata[i][2], matriksgamedata[i][3]])
                        found = True
        elif tahun_rilis:
            for i in at.panjangarray(matriksgamedata):
                if matriksgamedata[i][3] == tahun_rilis:
                    array = at.append(array, [matriksgamedata[i][0], matriksgamedata[i][1], matriksgamedata[i][4], matriksgamedata[i][2], matriksgamedata[i][3]])
                    found = True                    
        else:
            if gameid in ownedIDs:
                for i in at.panjangarray(matriksgamedata):
                    array = at.append(array, [matriksgamedata[i][0], matriksgamedata[i][1], matriksgamedata[i][4], matriksgamedata[i][2], matriksgamedata[i][3]])
                    found = True
        # semua list game yang dimiliki user
        if found:
            at.printmatrix(array)
        else:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else: # tidak ada game yang dimiliki user
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")