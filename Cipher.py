import FungsiBuatan

def encrypt(text, key):
    encryptedText = ""
    for i in range(FungsiBuatan.lenght(text)):
        if(65 <= ord(text[i]) <= 90):
            encryptedText += chr((ord(text[i]) - 65 + key) % 26 + 65)
        elif(97 <= ord(text[i]) <= 122):
            encryptedText += chr((ord(text[i]) - 97 + key) % 26 + 97)
        elif(48 <= ord(text[i]) <= 57):
            encryptedText += chr((ord(text[i]) - 48 + key) % 10 + 48)
        else:
            encryptedText += text[i]
    return encryptedText

def decrypt(text, key):
    decryptedText = ""
    for i in range(FungsiBuatan.lenght(text)):
        if(65 <= ord(text[i]) <= 90):
            decryptedText += chr((ord(text[i]) - 65 - key) % 26 + 65)
        elif(97 <= ord(text[i]) <= 122):
            decryptedText += chr((ord(text[i]) - 97 - key) % 26 + 97)
        elif(48 <= ord(text[i]) <= 57):
            decryptedText += chr((ord(text[i]) - 48 - key) % 10 + 48)
        else:
            decryptedText += text[i]
    return decryptedText