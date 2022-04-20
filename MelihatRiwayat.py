import Data, FungsiBuatan

def riwayat(idxUser):
    arr = []
    for i in range(FungsiBuatan.lenght(Data.riwayat)):
        if(Data.users[idxUser][0] == Data.riwayat[i][3]):
            arr += [[Data.riwayat[i][0], Data.riwayat[i][1], Data.riwayat[i][2], Data.riwayat[i][4]]]
    if(FungsiBuatan.lenght(arr)) == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        print("Daftar game:")
        nomor = 1
        for i in arr:
            print(str(nomor) + ". " + i[0] + " | " + i[1] + " | " + i[2] + " | " + i[3] + " |")
            nomor += 1