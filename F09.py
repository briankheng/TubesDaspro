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
riwayat = CSVParser(raw)
game = CSVParser(raw2)
print(riwayat)

def asal():
    arr = []
    for i in range(100):
        for j in range(3,4):
            if id==riwayat[i][j]:
                arr +=[riwayat[i][0]]
    return arr

def list_game():
    if len(asal()) == 0:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        index = 0
        for i in range(100):
            if index == len(asal()):
                break
            for j in range(1):
                if asal()[index] == game[i][0]:
                    print(game[i][0],"|",game[i][1],"|",game[i][2],"|",game[i][3],"|",game[i][4])
                    index +=1
        return

id = input()
print(asal())
list_game()