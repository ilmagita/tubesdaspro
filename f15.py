import argparse
import os
import sys
from time import sleep

import csvtools as csvt


def startsystem():
    parser = argparse.ArgumentParser()
    parser.add_argument("namafolder", help="melakukan loading data ke sistem")
    args = parser.parse_args()

    folder = args.namafolder
    cwd = os.getcwd()
    # Memeriksa apakah nama folder yang dimasukkan terdapat pada direktori
    if os.path.isdir(cwd + '//' + folder):
        print('Loading...')
        sleep(2)
        print('Selamat datang di antarmuka "Binomo"')
        return load(folder)
    else:   # Apabila nama folder yang dimasukkan tidak ada
        print(f'Folder "{folder}" tidak ditemukan.')
        sys.exit()


def load(folder):
    # load userdata
    matrixuser = csvt.csvtoarray(folder, 'user.csv')

    # load gamedata
    matrixgame = csvt.csvtoarray(folder, 'game.csv')

    # load riwayatdata
    matrixriwayat = csvt.csvtoarray(folder, 'riwayat.csv')

    # load kepemilikandata
    matrixkepemilikan = csvt.csvtoarray(folder, 'kepemilikan.csv')
        
    database = [matrixuser, matrixgame, matrixriwayat, matrixkepemilikan]
    return database
