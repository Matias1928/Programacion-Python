def empleado():
    while True:
        emple_usuario=str(input("Ingrese Usuario:")).lower()
        if emple_usuario != 'ariel':
            print("Error de Usuario")
        else:
            print("Usuario correcto")
            break

    while True:
        emple_pasword=int(input("Ingrese Pasword:"))
        if emple_pasword != 2:
            print("Error de pasword")
        else:
            print("Bienvenido")
            break