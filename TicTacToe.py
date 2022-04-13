def valid(x, y, papan):
    if(x > 3 or x < 1 or y > 3 or y < 1):
        print("\nkotak tidak valid.\n")
        return False
    elif(papan[y-1][x-1] != '#'):
        print("\nKotak sudah terisi. Silakan pilih kotak lain.\n")
        return False
    else:
        return True

def adaPemenang(papan):
    if((papan[0][0] == papan[0][1] == papan[0][2] and papan[0][0] != '#') or (papan[1][0] == papan[1][1] == papan[1][2] and papan[1][0] != '#') or 
       (papan[2][0] == papan[2][1] == papan[2][2] and papan[2][0] != '#') or (papan[0][0] == papan[1][0] == papan[2][0] and papan[0][0] != '#') or 
       (papan[0][1] == papan[1][1] == papan[2][1] and papan[0][1] != '#') or (papan[0][2] == papan[1][2] == papan[2][2] and papan[0][2] != '#') or
       (papan[0][0] == papan[1][1] == papan[2][2] and papan[0][0] != '#') or (papan[0][2] == papan[1][1] == papan[2][0] and papan[0][2] != '#')):
        return True
    else:
        return False

def adaSlot(papan):
    for i in range(3):
        for j in range(3):
            if(papan[i][j] == '#'):
                return True
    return False

def status(papan):
    print("\nStatus Papan")
    for i in range(3):
        for j in range(3):
            print(papan[i][j], end='')
        print()
    print()

def inputAngka(papan, pemain):
    print('Giliran Pemain "' + pemain + '"')
    x = int(input("X: "))
    y = int(input("Y: "))
    while(not valid(x, y, papan)):
        print('Giliran Pemain "' + pemain + '"')
        x = int(input("X: "))
        y = int(input("Y: "))
    papan[y-1][x-1] = pemain
    return papan

def tictactoe():
    papan = [['#' for j in range(3)] for i in range(3)]
    giliranX = True
    print("Legenda:\n# Kosong\nX Pemain 1\nO Pemain 2")
    status(papan)
    while(not adaPemenang(papan) and adaSlot(papan)):
        if(giliranX):
            papan = inputAngka(papan, 'X')
            status(papan)
            giliranX = False
        else:
            papan = inputAngka(papan, 'O')
            status(papan)
            giliranX = True
    if(not adaPemenang(papan)):
        print('Permainan seri.')
    elif(giliranX):
        print('Pemain "O" menang.')
    else:
        print('Pemain "X" menang.')
tictactoe()