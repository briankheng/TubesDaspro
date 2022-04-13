import Data, FungsiBuatan

def cariGameInventory(idxUser):
    id = input("Masukkan ID game: ")
    tahun = input("Masukkan Tahun Rilis Game: ")

    nomor = 0
    print("Daftar game pada inventory yang memenuhi kriteria: ")
    for i in range(FungsiBuatan.lenght(Data.kepemilikan)):
        if(Data.kepemilikan[i][1] == Data.users[idxUser][0]):
            for j in range(FungsiBuatan.lenght(Data.games)):
                if(id == '' and tahun == '' and Data.games[j][0] == Data.kepemilikan[i][0]):
                    print(str(nomor+1)+". "+Data.games[j][0]+" | "+Data.games[j][1]+" | "+Data.games[j][2]+" | "+Data.games[j][3]+" | "+Data.games[j][4])
                    nomor += 1
                elif(id != '' and tahun == '' and Data.games[j][0] == Data.kepemilikan[i][0] == id):
                    print(str(nomor+1)+". "+Data.games[j][0]+" | "+Data.games[j][1]+" | "+Data.games[j][2]+" | "+Data.games[j][3]+" | "+Data.games[j][4])
                    nomor += 1
                elif(id == '' and tahun != '' and Data.games[j][3] == tahun and Data.games[j][0] == Data.kepemilikan[i][0]):
                    print(str(nomor+1)+". "+Data.games[j][0]+" | "+Data.games[j][1]+" | "+Data.games[j][2]+" | "+Data.games[j][3]+" | "+Data.games[j][4])
                    nomor += 1
                elif(id != '' and tahun != '' and Data.games[j][0] == Data.kepemilikan[i][0] == id and Data.games[j][3] == tahun):
                    print(str(nomor+1)+". "+Data.games[j][0]+" | "+Data.games[j][1]+" | "+Data.games[j][2]+" | "+Data.games[j][3]+" | "+Data.games[j][4])
                    nomor += 1
    if(nomor == 0):
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

cariGameInventory(1)