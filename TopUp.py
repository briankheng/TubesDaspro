import Data, FungsiBuatan

def topUpSaldo():
    usernameValid = False

    # input user
    username = input("Masukkan username: ")
    saldo = input("Masukkan saldo: ")

    # mencari username
    for i in range(FungsiBuatan.lenght(Data.users)):
        if(Data.users[i][1] == username):
            if (int(Data.users[i][5]) + int(saldo) < 0): # validasi nilai saldo
                print("Masukan tidak valid.")
            else:
                Data.users[i][5] = int(Data.users[i][5]) + int(saldo)
                if (int(saldo) >= 0):
                    print ("Top up berhasil. Saldo " + Data.users[i][2] + " bertambah menjadi " + str(Data.users[i][5]) + ".")
                else:
                    print ("Top up berhasil. Saldo " + Data.users[i][2] + " berkurang menjadi " + str(Data.users[i][5]) + ".")
                
            usernameValid = True

    # pesan error
    if (usernameValid == False):
        print ("Username " + str(username) + " tidak ditemukan.")