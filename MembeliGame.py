import FungsiBuatan, Data
from time import gmtime

def membeliGame(idxUser):
    # input id Game yang ingin dibeli
    idGame = input("Masukkan ID Game: ")

    # mencari game
    punya = False
    for i in range(FungsiBuatan.lenght(Data.kepemilikan)):
        if((Data.kepemilikan[i][0] == idGame) and (Data.kepemilikan[i][1] == Data.users[idxUser][0])): # cek apakah user sudah memiliki game
            punya = True
            print("Anda sudah memiliki game tersebut.")

    if(not punya):
        adaGame = False
        for i in range(FungsiBuatan.lenght(Data.games)):
            if(Data.games[i][0] == idGame):
                adaGame = True
                if(int(Data.games[i][5]) == 0):
                    print("Stok Game tersebut sedang habis!")
                elif(int(Data.games[i][4]) > int(Data.users[idxUser][5])):
                    print("Saldo anda tidak cukup untuk membeli Game tersebut!")
                else:
                    print('Game "' + Data.games[i][1] + '" berhasil dibeli!')
                    Data.games[i][5] = int(Data.games[i][5]) - 1
                    Data.users[idxUser][5] = int(Data.users[idxUser][5]) - int(Data.games[i][4])
                    Data.kepemilikan += [[Data.games[i][0], Data.users[idxUser][0]]]
                    Data.riwayat += [[Data.games[i][0], Data.games[i][1], Data.games[i][4], Data.users[idxUser][0], gmtime().tm_year]]
        
        if(not adaGame):
            print("Game [id = " + idGame + "] tidak ditemukan pada toko!")