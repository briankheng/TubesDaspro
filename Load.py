import os, FungsiBuatan, Data

def readCSV(dirPath, file):
    arsipFile = open(dirPath + '/' + file, 'r')
    rekFile = arsipFile.readlines()
    arsipFile.close()
    return FungsiBuatan.CSVParser(rekFile)

def findPath(folder):
    path = os.getcwd()
    for (root, dirs, files) in os.walk(path):
        for dir in dirs:
            if(dir == folder):
                return root
    return -1

def load(folder):
    if(folder is None):
        print("Tidak ada nama folder yang diberikan!")
        quit()
    else:
        dirPath = findPath(folder)
        if(dirPath == -1):
            print('Folder "' + folder + '" tidak ditemukan.')
            quit()
        else:
            dirPath = os.path.join(dirPath, folder)
            if(os.path.isfile(dirPath + '/' + "user.csv")):
                Data.users = readCSV(dirPath, "user.csv")
            if(os.path.isfile(dirPath + '/' + "game.csv")):
                Data.games = readCSV(dirPath, "game.csv")
            if(os.path.isfile(dirPath + '/' + "kepemilikan.csv")):
                Data.kepemilikan = readCSV(dirPath, "kepemilikan.csv")
            if(os.path.isfile(dirPath + '/' + "riwayat.csv")):
                Data.riwayat = readCSV(dirPath, "riwayat.csv")
            print("\nLoading...\n")
            print('Selamat datang di antarmuka "Binomo", ketik "help" untuk bantuan!')