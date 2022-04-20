import FungsiBuatan, Data

def membeliGame(idxUser):
    # input user
    idGame = input("Masukkan ID Game: ")

    # mencari game
    for i in range(FungsiBuatan.lenght(Data.kepemilikan)):
        if((Data.kepemilikan[i][0] == idGame) and (Data.kepemilikan[i][1] == idxUser): # cek apakah user sudah memiliki game
            print("Anda sudah memiliki game tersebut.")
        else:
            for j in range (fungsiBuatan.lenght(Data.user)):
                if (Data.user[j][0] == idxUser):
                    for k in range (FungsiBuatan.lenght(Data.games)): # buka game
                        if (Data.games[k][0] == idGame):
                            if (Data.user[j][5] < Data.games[k][4]): # cek saldo
                                print("Saldo anda tidak cukup untuk membeli game tersebut.")
                            else: # cek stok
                                if (Data.game[k][5] == 0):
                                    print("Game tersebut sedang habis.")
                                else:
                                    print("Game" + str(Data.game[k][1]) + " berhasil dibeli."))
                                    Data.game[k][5] -= 1 # mengurangi stok
                                    Data.user[j][5] -= Data.games[k][4] # mengurangi saldo
                                    Data.kepemilikan.append([Data.games[k][0], Data.user[j][0]]) # menambahkan kepemilikan # ganti append jadi apa
