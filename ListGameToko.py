import Data, FungsiBuatan

def sortingArr(arr, idx): # Melakukan sorting ascending suatu arr berdasarkan parameter idx
    tempArr = arr
    for i in range(FungsiBuatan.lenght(arr)-1):
        for j in range(FungsiBuatan.lenght(arr)-1, i, -1):
            if(tempArr[j][idx] < tempArr[j-1][idx]):
                temp = tempArr[j][idx]
                tempArr[j][idx] = tempArr[j-1][idx]
                tempArr[j-1][idx] = temp
    return tempArr

def sortingGame(idx, c):
    sortedGames = sortingArr(Data.games, idx)
    if(c == '+'):
        for i in range(FungsiBuatan.lenght(Data.games)):
            print(str(i+1)+'. '+sortedGames[i][0]+' | '+sortedGames[i][1]+' | '+sortedGames[i][2]
                +' | '+sortedGames[i][3]+' | '+sortedGames[i][4]+' | '+sortedGames[i][5])
    else:
        nomor = 0
        for i in range(FungsiBuatan.lenght(Data.games)-1, -1, -1):
            print(str(nomor+1)+'. '+sortedGames[i][0]+' | '+sortedGames[i][1]+' | '+sortedGames[i][2]
                +' | '+sortedGames[i][3]+' | '+sortedGames[i][4]+' | '+sortedGames[i][5])
            nomor += 1

def listGame():
    x = input("Skema sorting : ")
    if(x == ''):
        sortingGame(0, '+')
    elif(x[0:5].lower() == 'tahun' and FungsiBuatan.lenght(x) == 6 and (x[5] == '+' or x[5] == '-')):
        sortingGame(3, x[5])
    elif(x[0:5].lower() == "harga" and FungsiBuatan.lenght(x) == 6 and (x[5] == '+' or x[5] == '-')):
        sortingGame(4, x[5])
    else:
        print("Skema sorting tidak valid!")