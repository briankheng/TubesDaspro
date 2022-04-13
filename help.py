def helpAdmin():
    print("====== HELP ======")
    print("1. register - Mendaftarkan user baru")
    print("2. login - Melakukan login ke dalam sistem")
    print("3. tambah game - Menambahkan daftar game ke dalam toko")
    print("4. ubah game - Mengubah informasi game pada toko")
    print("5. ubah stok - Mengubah stok game pada toko")
    print("6. listing game - Mengurutkan game di toko berdasarkan ID, tahun rilis, atau harga")
    print("7. cari game pada toko - Mencari game di toko berdasarkan ID, nama game, harga, kategori, atau tahun rilis")
    print("8. top up saldo - Menambahkan saldo kepada user")
    print("9. save - Menyimpan data ke dalam file setelah melakukan perubahan")
    
def helpUser():
    print("====== HELP ======")
    print("1. login - Melakukan login ke dalam sistem")
    print("2. listing game - Mengurutkan game di toko berdasarkan ID, tahun rilis, atau harga")
    print("3. beli game - Membeli game dengan memasukkan ID game yang ingin dibeli")
    print("4. lihat game - Melihat game yang dimiliki user")
    print("5. cari game yang dimiliki - Mencari game yang dimiliki berdasarkan ID dan tahun rilis")
    print("6. cari game pada toko- Mencari game di toko berdasarkan ID, nama game, harga, kategori, atau tahun rilis")
    print("7. riwayat pembelian - Melihat riwayat pembelian game")
    print("8. save - Menyimpan data ke dalam file setelah melakukan perubahan")

def helpBelumLogin():
    print("====== HELP ======")
    print("1. login - Melakukan login ke dalam sistem")

def help(pilihan):
    if(pilihan == 1):
        helpAdmin()
    elif(pilihan == 2):
        helpUser()
    else:
        helpBelumLogin()