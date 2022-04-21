import os, FungsiBuatan, Data

def readCSV(dirPath, folder, file):
    arsipFile = open(dirPath + '/' + folder + '/' + file, 'r')
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
            if(os.path.isfile(dirPath + '/' + folder + '/' + "user.csv")):
                Data.users = readCSV(dirPath, folder, "user.csv")
            if(os.path.isfile(dirPath + '/' + folder + '/' + "game.csv")):
                Data.games = readCSV(dirPath, folder, "game.csv")
            if(os.path.isfile(dirPath + '/' + folder + '/' + "kepemilikan.csv")):
                Data.kepemilikan = readCSV(dirPath, folder, "kepemilikan.csv")
            if(os.path.isfile(dirPath + '/' + folder + '/' + "riwayat.csv")):
                Data.riwayat = readCSV(dirPath, folder, "riwayat.csv")