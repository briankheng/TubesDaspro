def helpAdmin():
    print("========================== HELP ==========================")
    print("1. register - Mendaftarkan user baru")
    print("2. login - Melakukan login ke dalam sistem")
    print("3. tambah_game - Menambahkan daftar game ke dalam toko")
    print("4. ubah_game - Mengubah informasi game pada toko")
    print("5. ubah_stok - Mengubah stok game pada toko")
    print("6. list_game_toko - Mengurutkan game di toko berdasarkan ID, tahun rilis, atau harga")
    print("7. search_game_at_store - Mencari game di toko berdasarkan ID, nama game, harga, kategori, atau tahun rilis")
    print("8. topup - Menambahkan saldo kepada user")
    print("9. save - Menyimpan data ke dalam file setelah melakukan perubahan")
    print("10.exit - Keluar dari aplikasi")
    print("11.kerangajaib - Menjawab pertanyaan secara ajaib")
    print("12.tictactoe - Permainan sederhana tic-tac-toe")
    
def helpUser():
    print("========================== HELP ==========================")
    print("1. login - Melakukan login ke dalam sistem")
    print("2. list_game_toko - Mengurutkan game di toko berdasarkan ID, tahun rilis, atau harga")
    print("3. buy_game - Membeli game dengan memasukkan ID game yang ingin dibeli")
    print("4. list_game - Melihat game yang dimiliki user")
    print("5. search_my_game - Mencari game yang dimiliki berdasarkan ID dan tahun rilis")
    print("6. search_game_at_store- Mencari game di toko berdasarkan ID, nama game, harga, kategori, atau tahun rilis")
    print("7. riwayat - Melihat riwayat pembelian game")
    print("8. save - Menyimpan data ke dalam file setelah melakukan perubahan")
    print("9. exit - Keluar dari aplikasi")
    print("10.kerangajaib - Menjawab pertanyaan secara ajaib")
    print("11.tictactoe - Permainan sederhana tic-tac-toe")

def helpBelumLogin():
    print("========================== HELP ==========================")
    print("1. login - Melakukan login ke dalam sistem")

def help(pilihan):
    if(pilihan == 1):
        helpAdmin()
    elif(pilihan == 2):
        helpUser()
    else:
        helpBelumLogin()