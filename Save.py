import Data, FungsiBuatan, os

# ga ngerti bikin folder, ga ngerti os
# cek nama folder uda ada ato belonnya juga ga paham hehehe mian

def save ():
    # nama folder
    folder = input("Masukan nama folder penyimpanan: ")

    # save user
    user = open('FileEksternal/user.csv', 'w')
    for i in range (FungsiBuatan.lenght(Data.user)):
        user.writelines(Data.user[i][0]+';'+Data.user[i][1]+';'+Data.user[i][2]+';'+Data.user[i][3]+';'+Data.user[i][4]+';'+ Data.user[i][5]+'\n')

    # save games
    games = open('FileEksternal/games.csv', 'w')
    for i in range (FungsiBuatan.lenght(Data.games)):
        user.writelines(Data.games[i][0] + ";" + Data.games[i][1] + ";" + Data.games[i][2] + ";" + Data.games[i][3] + ";" + Data.games[i][4] + ";" + Data.games[i][5] + "\n")

    # save kepemilikan
    kepemilikan = open('FileEksternal/kepemilikan.csv', 'w')
    for i in range (FungsiBuatan.lenght(Data.kepemilikan)):
        user.writelines(Data.kepemilikan[i][0] + ";" + Data.kepemilikan[i][1] + "\n")
    
    # save riwayat
    riwayat = open('FileEksternal/riwayat.csv', 'w')
    for i in range (FungsiBuatan.lenght(Data.riwayat)):
        user.writelines(Data.riwayat[i][0] + ";" + Data.riwayat[i][1] + ";" + Data.riwayat[i][2] + ";" + Data.riwayat[i][3] + "\n")