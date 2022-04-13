import Login, argparse

parser = argparse.ArgumentParser()
parser.add_argument("namaFolder", nargs='?')
args = parser.parse_args()
if(args.namaFolder is None):
    print("Tidak ada nama folder yang diberikan!")
    exit()
elif(args.namaFolder != "FileEksternal"):
    print('Folder "' + str(args.namaFolder) + '" tidak ditemukan.')
    exit()

keluar = False
sudahLogin = False
while(not keluar):
    x = input()
    if(x == "login"):
        idxUser = Login.login()
        if(idxUser != -1):
            sudahLogin = True
    # ...