import Data, FungsiBuatan

def riwayat():
    arr = []
    for i in range(6):
        for j in range(3,4):
            if id==Data.riwayat[i][j]:
                arr += [[Data.riwayat[i][0],Data.riwayat[i][1],Data.riwayat[i][2],Data.riwayat[i][4]]]
    if len(arr) == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        for i in arr:
            print(i[0],"|",i[1],"|",i[2],"|",i[3],"|")
    return
id=input()
riwayat()