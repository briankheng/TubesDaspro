import FungsiBuatan, Data

def tambahGame():
    newGame = ["" for i in range (5)]

    # input data new game
    newGame[0] = input("Masukkan nama game: ")
    newGame[1] = input("Masukkan kategori: ")
    newGame[2] = input("Masukkan tahun rilis: ")
    newGame[3] = input("Masukkan harga: ")
    newGame[4] = input("Masukkan stok awal: ")

    # validasi tidak ada input kosong
    while (newGame[0] == "" or newGame[1] == "" or newGame[2] == "" or newGame[3] == "" or newGame[4] == ""): 
        print("Mohon masukan semua informasi mengenai game agar bisa disimpan BNMO.")
        newGame[0] = input("Masukkan nama game: ")
        newGame[1] = input("Masukkan kategori: ")
        newGame[2] = input("Masukkan tahun rilis: ")
        newGame[3] = input("Masukkan harga: ")
        newGame[4] = input("Masukkan stok awal: ")

    # generate game id
    banyakGame = FungsiBuatan.lenght(Data.games) + 1

    if banyakGame <= 9:
        gameIdNew = "GAME00" + str(banyakGame)
    elif banyakGame <= 99:
        gameIdNew = "GAME0" + str(banyakGame)
    elif banyakGame <= 999:
        gameIdNew = "GAME" + str(banyakGame) # pesan error stlh 999
    
    # Add data to Global Variable
    Data.games += [[gameIdNew, newGame[0], newGame[1], newGame[2], newGame[3], newGame[4]]]

tambahGame()