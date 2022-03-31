# Ejercicio 8- Matias Avalo
print("---DATOS A VALIDA---")
voc=0
while voc <3:
    print("Ingrese  -NOMBRE Y APELLIDO-:")
    nom_ape=input()
    Nom_Ape=nom_ape.lower()
    for letters in nom_ape:
        if letters == "a" or letters == "e" or letters == "i" or letters =="o" or letters == "u":
            voc+=1
    
error=1
while error >0:
    año=input("Ingrese -AÑO- en el que Nacio: ")
    error=0
    while len(año)!=4:
        print("Ingrese -AÑO- en el que Nacio...")
        año=int(input())
    for caracter in año:
        if caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9":
            continue
        else:
            error+=1
signos=0
while signos <1:
    signos=0
    password=input("Ingrese Paswor: ")

    while len(password) <8 or len(password)>16:
        password=input("Ingrese Paswor: ") 
        for caracter in password:
            if caracter == "#" or caracter == "$" or caracter == "!" or caracter == "''" or caracter == "%" or caracter == "&" or caracter == "." :
                signos+=1

print("HOLA",nom_ape)



