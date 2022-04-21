import FungsiBuatan, Data

def listGame(idxUser):
    arr = []
    for i in range(FungsiBuatan.lenght(Data.kepemilikan)):
        if(Data.kepemilikan[i][1] == Data.users[idxUser][0]):
            for j in range(FungsiBuatan.lenght(Data.games)):
                if(Data.games[j][0] == Data.kepemilikan[i][0]):
                    arr += [[Data.games[j][0], Data.games[j][1], Data.games[j][2], Data.games[j][3], Data.games[j][4]]]
    
    if(FungsiBuatan.lenght(arr) == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
    else:
        print("Daftar game:")
        nomor = 1
        for i in arr:
            print(str(nomor) + ". " + i[0] + " | " + i[1] + " | " + i[2] + " | " + i[3] + " | " + i[4] + " |")
            nomor += 1