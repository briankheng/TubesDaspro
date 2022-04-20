import Data, FungsiBuatan

def asal():
    arr = []
    for i in range(100):
        for j in range(3,4):
            if id==Data.riwayat[i][j]:
                arr +=[Data.riwayat[i][0]]
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
                if asal()[index] == Data.game[i][0]:
                    print(Data.game[i][0],"|",Data.game[i][1],"|",Data.game[i][2],"|",Data.game[i][3],"|",Data.game[i][4])
                    index +=1
        return

id = input()
print(asal())
list_game()