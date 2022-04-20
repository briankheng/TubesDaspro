import Data, FungsiBuatan

def topUpSaldo():
    usernameValid = False

    # input user
    username = input("Masukkan username: ")
    saldo = input("Masukkan saldo: ")

    # mencari username
    for i in range(FungsiBuatan.lenght(Data.user)):
        if(Data.user[i][1] == id):
            if (Data.user[i][5] + int(saldo) < 0): # validasi nilai saldo
                print("Masukan tidak valid.")
            else:
                Data.user[i][5] += int(saldo)
                if (int(saldo) >= 0):
                    print ("Top up berhasil. Saldo " + str(username) + "bertambah menjadi " + str(Data.user[i][5]) + ".")
                else:
                    print ("Top up berhasil. Saldo " + str(username) + "berkurang menjadi " + str(Data.user[i][5]) + ".")
                
            usernameValid = True

    # pesan error
    if (usernameValid == False):
        print ("Username" + str(username) + "tidak ditemukan.")

topUpSaldo()