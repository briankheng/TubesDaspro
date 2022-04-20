import Save

def exit():
    simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while(simpan.lower() != 'y' and simpan.lower() != 'n'):
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if(simpan.lower() == 'y'):
        Save.save()
    quit()