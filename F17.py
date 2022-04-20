notExit = False

def exit():
while notExit :
   askSave= input (“save y/n”)
   if askSave == "y" or askSave =="Y":
        save()
        notExit = True
   elif askSave == "n" or askSave =="N":
        notExit = True
   else: 
       continue