# Ejercicio 10- Matias Avalo
import random
print("----ADIVINADOR DE NUMEROS----")
print("Instrucciones: Debe ingresar un valor del 0 al 10...")
contador=0
for i in range(5):
    contador -=1
    ale=random.randint(0,10)
    valor=int(input("Ingrese un valor:"))
    if valor == ale:
        print ("Usted ha Acertado el numero")
        break
    else:
        print ("A perdido pruebe nuevamente...")
else:
    print("EL VALOR ERA:",ale)