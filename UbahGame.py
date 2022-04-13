import Data, FungsiBuatan

def writeToCSV(): # Melakukan overwrite dari variable di python ke file .csv
    game = open('FileEksternal/game.csv', 'w')
    for i in range(FungsiBuatan.lenght(Data.games)):
        if(Data.games[i][0] != ''):
            game.writelines(Data.games[i][0]+';'+Data.games[i][1]+';'+Data.games[i][2]+';'+Data.games[i][3]+';'+Data.games[i][4]+';'+Data.games[i][5]+'\n')

def ubahGame():
    id = input("Masukkan ID game: ")
    game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    for i in range(FungsiBuatan.lenght(Data.games)):
        if(Data.games[i][0] == id):
            if(game != ''):
                Data.games[i][1] = game
            if(kategori != ''):
                Data.games[i][2] = kategori
            if(tahun != ''):
                Data.games[i][3] = tahun
            if(harga != ''):
                Data.games[i][4] = harga
    #writeToCSV() # Hanya jika dilakukan perintah save (masukkin ke fungsi save)
ubahGame()