import Data, FungsiBuatan, Cipher, os
from Save import writeToCSV

def validasiUsername(username): # Mengecek apakah username sudah terpakai atau belum
    for i in range (FungsiBuatan.lenght(Data.users)):
        if(Data.users[i][1] == username):
            return False
    return True

def register(folder):
    nama = input("Masukan nama : ")
    username = input("Masukan username : ")
    password = input("Masukan password : ")

    if(validasiUsername(username)):
        Data.users += [[str(FungsiBuatan.lenght(Data.users)), username, nama, Cipher.encrypt(password, 4), "User", str(0)]]
        writeToCSV(os.path.join(os.getcwd(), folder), "user.csv", Data.users)
        print("\nUsername " + username + ' telah berhasil register ke dalam "Binomo".')
    else:
        print("\nUsername " + username + " sudah terpakai, silakan menggunakan username lain.")