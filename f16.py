import os
import csvtools as csvt
from time import sleep

def save(database):
    namafolder = input("Masukkan nama folder penyimpanan: ")
    csvt.writecsv(database[0], namafolder, 'user.csv')
    csvt.writecsv(database[1], namafolder, 'game.csv')
    csvt.writecsv(database[2], namafolder, 'riwayat.csv')
    csvt.writecsv(database[3], namafolder, 'kepemilikan.csv')

    print("Saving...")
    sleep(2)
    print("Data telah disimpan pada folder ", namafolder, "!")