import Data, FungsiBuatan

def ubahStok():
    id = input("Masukkan ID game: ")

    benar = 0

    for i in range(FungsiBuatan.lenght(Data.games)):
        if(Data.games[i][0] == id):        
            tambahStok = int(input("Masukkan jumlah: "))
            benar = 1
            
            Data.games[i][5] = int(Data.games[i][5]) + tambahStok
            
            if(int(Data.games[i][5]) > 0):
                if tambahStok < 0:
                    print("Stok game",Data.games[i][1],"berhasil dikurangi. Stok sekarang:",Data.games[i][5])
                else:
                    print("Stok game",Data.games[i][1],"berhasil ditambahkan. Stok sekarang:",Data.games[i][5])
            else:
                Data.games[i][5] = int(Data.games[i][5]) - tambahStok
                print("Stok game",Data.games[i][1],"gagal dikurangi karena stok kurang. Stok sekarang:",Data.games[i][5])
    
    if(benar == 0):
        print("Tidak ada game dengan ID tersebut!")