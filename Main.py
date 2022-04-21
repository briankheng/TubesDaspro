import Login, Load, argparse, Data, Register, TambahGame, UbahGame, UbahStok, ListGameToko, MembeliGame
import ListGameInventory, CariGameInventory, CariGameToko, TopUp, MelihatRiwayat, Help, Save, Exit
import MagicConchShell, TicTacToe

parser = argparse.ArgumentParser()
parser.add_argument("namaFolder", nargs='?')
args = parser.parse_args()

Load.load(args.namaFolder)

sudahLogin = False
idxUser = -1

while True:
    perintah = input(">>> ")
    if(perintah == "register"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "Admin"):
                Register.register(args.namaFolder)
            else:
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "login"):
        if(not sudahLogin):
            idxUser = Login.login()
            if(idxUser != -1):
                sudahLogin = True
        else:
            print("Maaf, anda telah melakukan login sebelumnya, exit terlebih dahulu sebelum menjalankan perintah login!")
    elif(perintah == "tambah_game"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "Admin"):
                TambahGame.tambahGame()
            else:
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "ubah_game"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "Admin"):
                UbahGame.ubahGame()
            else:
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "ubah_stok"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "Admin"):
                UbahStok.ubahStok()
            else:
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "list_game_toko"):
        if(sudahLogin):
            ListGameToko.listGame()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "buy_game"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "User"):
                MembeliGame.membeliGame(idxUser)
            else:
                print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "list_game"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "User"):
                ListGameInventory.listGame(idxUser)
            else:
                print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "search_my_game"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "User"):
                CariGameInventory.cariGameInventory(idxUser)
            else:
                print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "search_game_at_store"):
        if(sudahLogin):
            CariGameToko.cariGameToko()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "topup"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "Admin"):
                TopUp.topUpSaldo()
            else:
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "riwayat"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "User"):
                MelihatRiwayat.riwayat(idxUser)
            else:
                print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "help"):
        if(sudahLogin):
            if(Data.users[idxUser][4] == "Admin"):
                Help.help(1)
            else:
                Help.help(2)
        else:
            Help.help(3)
    elif(perintah == "save"):
        if(sudahLogin):
            Save.save()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "exit"):
        if(sudahLogin):
            Exit.exit()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "kerangajaib"):
        if(sudahLogin):
            MagicConchShell.LCG()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    elif(perintah == "tictactoe"):
        if(sudahLogin):
            TicTacToe.tictactoe()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    else:
        print("Maaf, perintah yang anda masukkan tidak valid! Silakan coba lagi...")