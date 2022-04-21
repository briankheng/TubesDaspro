import Login, Load, argparse

parser = argparse.ArgumentParser()
parser.add_argument("namaFolder", nargs='?')
args = parser.parse_args()

Load.load(args.namaFolder)

sudahLogin = False
while True:
    x = input()
    if(x == "login"):
        idxUser = Login.login()
        if(idxUser != -1):
            sudahLogin = True
    # ...