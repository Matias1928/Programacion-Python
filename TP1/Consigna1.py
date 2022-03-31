# Ejercicio 1- Matias Avalo
#LIST DE MATERIAS
materia_list1=[]
#LISTA DE NOTAS
nota_1=[]
#PEDIDO DE NOTA Y MATERIAS POR UN BUCLE FOR

print("...MENU...")
print("¡Por favor ingrese Cuatro Materia!")
materia=0
for i in range (4):
    
    materia=input("Ingrese Materias: ")
    materia_list1.append(materia)
    nota1=float (input("Ingrese Nota:"))
    nota2=float(input("Ingrese Nota:"))
    nota3=float(input("Ingrese Nota:"))
    nota_1.append([nota1, nota2, nota3])
    suma= nota1+nota2+nota3
    promedio= suma/3

    if promedio >8:
        print ("Promociono")
    elif promedio >=6:
        print ("aprobado")
    else:
        print("desaprobado")