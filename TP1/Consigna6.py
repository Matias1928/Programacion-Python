# Ejercicio 6- Matias Avalo
amigos=[]
print("LISTA DE AMIGOS")
print("    Menu\n")
print("Ingrese Sus amigos y una ves finalice escriba exit, para finalizar ejecucion")
amg=0
exit="exit"
while amg != exit:
    amg=str(input("Ingrese el Nombre de sus amigos:"))
    amigos.append(amg)

    if amg == exit :
        print(*amigos,sep="-",)
        break