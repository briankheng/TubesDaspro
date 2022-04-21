import Data, FungsiBuatan, os

def findPath(folder):
    path = os.getcwd()
    for (root, dirs, files) in os.walk(path):
        for dir in dirs:
            if(dir == folder):
                return root
    return -1

def writeToCSV(dirPath, file, memori):
    arsipFile = open(dirPath + '/' + file, 'w')
    for i in range(FungsiBuatan.lenght(memori)):
        temp = ""
        for j in range(FungsiBuatan.lenght(memori[i])):
            if(j == FungsiBuatan.lenght(memori[i]) - 1):
                temp += (memori[i][j] + '\n')
            else:
                temp += (memori[i][j] + ';')
        arsipFile.writelines(temp)
    arsipFile.close()

def save():
    folder = input("Masukan nama folder penyimpanan: ")

    dirPath = findPath(folder)
    if(dirPath == -1):
        dirPath = os.path.join(os.getcwd(), folder)
        os.mkdir(dirPath) # Buat directory baru jika belum ada.
    else:
        dirPath = os.path.join(dirPath, folder)

    # Buat File CSV jika belum ada.
    if(not os.path.isfile(dirPath + '/' + "user.csv")):
        open(dirPath + '/' + "user.csv", 'a').close()
    if(not os.path.isfile(dirPath + '/' + "game.csv")):
        open(dirPath + '/' + "game.csv", 'a').close()
    if(not os.path.isfile(dirPath + '/' + "kepemilikan.csv")):
        open(dirPath + '/' + "kepemilikan.csv", 'a').close()
    if(not os.path.isfile(dirPath + '/' + "riwayat.csv")):
        open(dirPath + '/' + "riwayat.csv", 'a').close()

    # Menuliskan data dari memori ke CSV
    writeToCSV(dirPath, "user.csv", Data.users)
    writeToCSV(dirPath, "game.csv", Data.games)
    writeToCSV(dirPath, "kepemilikan.csv", Data.kepemilikan)
    writeToCSV(dirPath, "riwayat.csv", Data.riwayat)