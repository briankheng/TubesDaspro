import Data, FungsiBuatan, Cipher

def validasi(username, password): # Validasi username & password dari variable global users
    for i in range(FungsiBuatan.lenght(Data.users)):
        if (Data.users[i][1] == username and Cipher.decrypt(Data.users[i][3], 4) == password):
            return i
    return -1

def login(): # Melakukan login, jika login tervalidasi maka mengembalikan idxUser
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    idxUser = validasi(username, password)
    if(idxUser != -1):
        print("Halo " + Data.users[idxUser][2] + '! Selamat datang di "Binomo".')
        return idxUser
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return -1