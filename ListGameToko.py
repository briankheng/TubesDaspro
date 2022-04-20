import Data, FungsiBuatan

def sortingGame(idx, c):
    sortedGames = FungsiBuatan.sorting(Data.games, idx)
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
listGame()