import time

def LCG():
    input("Apa pertanyaanmu? ")
    seed = int(time.time())
    randomValue = (seed * 7 + 3) % 6
    if(randomValue == 0):
        print("\nYa.")
    elif(randomValue == 1):
        print("\nTidak.")
    elif(randomValue == 2):
        print("\nBisa Jadi.")
    elif(randomValue == 3):
        print("\nMungkin.")
    elif(randomValue == 4):
        print("\nTentunya.")
    else:
        print("\nTidak Mungkin.")

LCG()