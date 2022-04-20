raw = open('riwayat.csv', 'r').readlines()
raw2 = open('game.csv', 'r').readlines()
def CSVParser (raw):
    M = [["" for col in range(6)] for row in range(100)]
    for i in range(len(raw)): # Fungsi len buat sendiri
        idx = 0
        temp = ""
        for j in range(len(raw[i])): # Fungsi len buat sendiri
            if(raw[i][j] == ';' or raw[i][j] == '\n'):
                M[i][idx] = temp
                temp = ""
                idx += 1
            else:
                temp += raw[i][j]
    return M
data_riwayat = CSVParser(raw)
game = CSVParser(raw2)

def riwayat():
    arr = []
    for i in range(6):
        for j in range(3,4):
            if id==data_riwayat[i][j]:
                arr += [[data_riwayat[i][0],data_riwayat[i][1],data_riwayat[i][2],data_riwayat[i][4]]]
    if len(arr) == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        for i in arr:
            print(i[0],"|",i[1],"|",i[2],"|",i[3],"|")
    return
id=input()
riwayat()