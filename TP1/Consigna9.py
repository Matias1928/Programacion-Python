# Ejercicio 9- Matias Avalo
#MENU DE CALCULADORA
from Operaciones import Suma, Resta, Multiplicacion, Division

print("-----CALCULADORA-----")
print("         Menu\n") 

entrada=0
while entrada !=5:
    print("1--->SUMA  2--->RESTA 3--->MULTIPLICACION  4--->DIVISION  5--->SALIR") 
    entrada=int(input("Ingrese una opcion:"))
    if entrada==1: #Suma5
        print("SUMA")
        Suma()
        #num1=float(input("Ingrese Valor:"))
        #num2=float(input("Ingrese Valor:")) 
        #suma=num1+num2
        #print("SU RESULTADO ES:",)
    elif entrada==2: #Resta
        print("RESTA")
        Resta
        #num1=float(input("Ingrese Valor:"))
        #num2=float(input("Ingrese Valor:"))
        #resta=num1+num2
        #print("SU RESULTADO ES:",resta)
    elif entrada==3:#Multiplicacion
        print("MULTIPLICACIÓN")
        Multiplicacion()
        #num1=float(input("Ingrese Valor:"))
        #num2=float(input("Ingrese Valor:"))
        #multi=num1*num2
        #print("SU RESULTADO ES:",multi)
    elif entrada == 4:#Division
        print("DIVISIÓN")
        Division()
        #num1=float(input("Ingrese Valor:"))
        #num2=float(input("Ingrese Valor:"))
        #division=num1/num2
        #print(division)
    elif entrada==5:
        print("SALIR")
        break