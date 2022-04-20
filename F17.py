notExit = False

while notExit :
   askSave= input (“save y/n”)
   if askSave == y:
        save()
        notExit = True
   elif askSave == n:
        notExit = True
   else: 
       continue