def admin():
    while True:
        admin_usuario=str(input("Ingrese Usuario:")).lower()
        if admin_usuario != 'jorge':
            print("Error de Usuario")
        else:
            print("Usuario correcto")
            break

    while True:
        admin_pasword=int(input("Ingrese Pasword:"))
        if admin_pasword != 3:
            print("Error de pasword")
        else:
            print("Bienvenido")
            break