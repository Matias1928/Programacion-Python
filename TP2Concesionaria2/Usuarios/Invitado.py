
def invitado():
    while True:
        invi_usuario=str(input("Ingrese Usuario:")).lower()
        if invi_usuario != 'matias':
            print("Error de Usuario")
        else:
            print("Usuario correcto")
            break

    while True:
        invi_pasword=int(input("Ingrese Pasword:"))
        if invi_pasword != 1:
            print("Error de pasword")
        else:
            print("Bienvenido")
            break
    