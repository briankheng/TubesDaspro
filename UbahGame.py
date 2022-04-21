import Data, FungsiBuatan

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