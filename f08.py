import arraytools as at


def beligame(database, loggeduserdata):
    userdata = database[0]
    gamedata = database[1]
    riwayatdata = database[2]
    kepemilikandata = database[3]
    datagameuser = usergames(gamedata, kepemilikandata, loggeduserdata)

    idgamedibeli = input("Masukkan ID Game: ")
    datagamedibeli = findgame(idgamedibeli, gamedata)

    if isgamebought(idgamedibeli, datagameuser):
        print("Anda sudah memiliki Game tersebut!")
    else:
        if isstokada(datagamedibeli):
            if issaldocukup(datagamedibeli, loggeduserdata):
                saldouser = int(loggeduserdata[5])
                hargagame = int(datagamedibeli[4])
                namagame = datagamedibeli[1]
                idpembeli = loggeduserdata[0]

                datagamedibeli[5] = str(int(datagamedibeli[5])-1)
                loggeduserdata[5] = str(saldouser - hargagame)

                datakepemilikanbaru = [idgamedibeli, idpembeli]
                kepemilikandata = at.append(kepemilikandata, [datakepemilikanbaru])

                riwayatbaru = [idgamedibeli, namagame, str(hargagame), idpembeli, "2022"]
                riwayatdata = at.append(riwayatdata, [riwayatbaru])

                userdata[int(idpembeli)][5] = str(saldouser - hargagame)

                database = [userdata, gamedata, riwayatdata, kepemilikandata]
                print(f'Game "{namagame}" berhasil dibeli!')
            else:
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        else:
            print("Stok Game tersebut sedang habis!")

    return database, loggeduserdata


def isgamebought(id, datagameuser):
    for i in range(at.panjangarray(datagameuser)):
        if id == datagameuser[0]:
            return True
    return False


def usergames(gamedata, datakepemilikan, loggeduserdata):
    iduser = loggeduserdata[0]
    usergamesdata = [gamedata[0]]

    for i in range(at.panjangarray(datakepemilikan)):
        if datakepemilikan[i][1] == iduser:
            idgame = datakepemilikan[i][0]
            boughtgamedata = findgame(idgame, gamedata)
            usergamesdata = at.append(usergamesdata, [boughtgamedata])

    return usergamesdata


def findgame(id, gamedata):
    for i in range(at.panjangarray(gamedata)):
        if id == gamedata[i][0]:
            return gamedata[i]


def isstokada(datagamedibeli):
    if int(datagamedibeli[5]) > 0:
        return True
    else:
        return False


def issaldocukup(datagamedibeli, datapembeli):
    saldouser = int(datapembeli[5])
    hargagame = int(datagamedibeli[4])

    if saldouser >= hargagame:
        return True
    else:
        return False
