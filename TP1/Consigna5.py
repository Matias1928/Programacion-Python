# Ejercicio 5- Matias Avalo
print("¡Ingrese Tres Numeros!")
num1=int(input("Ingrese  Número:"))
num2=int(input("Ingrese  Número:"))
num3=int(input("Ingrese  Número:"))
if num1 > num2 and num1 >num3: 
    print("Numero uno es Mayor:",num1)
elif num2 > num1 and num2 >num3: 
    print("Numero dos es Mayor:",num2)
elif num3 > num1 and num3 >num2: 
    print("Numero tres es Mayor:",num3)
else:
    print("No se pudo establecer el Mayor")