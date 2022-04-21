import Data, FungsiBuatan

def cariGameToko():
    id = input("Masukkan ID Game: ")
    nama = input("Masukkan Nama Game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun = input("Masukkan Tahun Rilis Game: ")
    nomor = 0
    print("Daftar game pada toko yang memenuhi kriteria: ")
    for i in range(1, FungsiBuatan.lenght(Data.games)):
        if((str(Data.games[i][0].lower()) == id.lower() or id == '') and (str(Data.games[i][1].lower()) == nama or nama.lower() == '') 
        and (str(Data.games[i][2].lower()) == kategori.lower() or kategori == '') and (str(Data.games[i][3]) == tahun or tahun == '') 
        and (str(Data.games[i][4]) == harga or harga == '')):
            print(str(nomor+1)+'. '+str(Data.games[i][0])+' | '+str(Data.games[i][1])+' | '+str(Data.games[i][2])
                +' | '+str(Data.games[i][3])+' | '+str(Data.games[i][4])+' | '+str(Data.games[i][5]))
            nomor += 1
    if(nomor == 0):
        print("Tidak ada game pada toko yang memenuhi kriteria")