'''Desarrollar un software que permita ingresar números. Por cada ingreso se debe mostrar el mayor, menor, el total y el promedio hasta el momento.'''


from statistics import mean


print("BIENVENIDO")
numero=[]
while True:
    print("\n")
    num=int(input("ingrese un Número:"))
    print("\n")
    numero.append(num)
    val_max=max(numero)#Funcion "MAX" sirve para encontrar el mayor de una lista
    val_min=min(numero)#Funcion "MIN" sirve para encontrar el mayor de una lista
    val_suma=sum(numero)#Funcion "SUM" suma todos los valores de un lista 
    val_promedio=mean(numero)#Funcion "mean" saca el promedio de una lista
    print("Valor Maximo:",val_max)
    print("Valor Minimo:",val_min)
    print("Suma de Valore:",val_suma)
    print("Promedio:",val_promedio)
    print("Lista Completa:",numero)



