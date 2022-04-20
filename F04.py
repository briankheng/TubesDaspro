# F04: tambah game baru


def tambah_game():
    new_game = ["" for i in range (5)]

    # input data new game
    new_game[0] = input("Masukkan nama game: ")
    new_game[1] = input("Masukkan kategori: ")
    new_game[2] = input("Masukkan tahun rilis: ")
    new_game[3] = input("Masukkan harga: ")
    new_game[4] = input("Masukkan stok awal: ")

    # validasi tidak ada input kosong
    while (new_game[0] == "" or new_game[1] == "" or new_game[2] == "" or new_game[3] == "" or new_game[4] == ""): 
        print("Mohon masukan semua informasi mengenai game agar bisa disimpan BNMO.")
        new_game[0] = input("Masukkan nama game: ")
        new_game[1] = input("Masukkan kategori: ")
        new_game[2] = input("Masukkan tahun rilis: ")
        new_game[3] = input("Masukkan harga: ")
        new_game[4] = input("Masukkan stok awal: ")

    # generate game id
    game_id = open ("game.csv", "r")
    banyak_game = len(game_id.readlines()) # fungsi len buat sendiri
    game_id.close()

    if banyak_game <= 9:
        game_id_new = "GAME00" + str(banyak_game)
    elif banyak_game <= 99:
        game_id_new = "GAME0" + str(banyak_game)
    elif banyak_game <= 999:
        game_id_new = "GAME0" + str(banyak_game)
    
    # write data to csv file
    writer = open('game.csv', 'a')
    writer.writelines(game_id_new + ";" + new_game[0] + ';' + new_game[1] + ';' + new_game[2] + ';' + new_game[3] + ';' + new_game[4] + '\n')

tambah_game()


