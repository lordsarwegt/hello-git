intentos=0
login= False
while login!=True:
    print('User')
    user=input()
    print('Contraseña')
    pasw=input()
    if user=="Usuario1" and pasw=="123":
        login=True
        print ("Entraste")
    else:
        print ("Contraseña incorrecta, por favor intentalo de nuevo")
        intentos +=1
    if intentos==3:
        print ('Usuario Bloqueado')
        break
    