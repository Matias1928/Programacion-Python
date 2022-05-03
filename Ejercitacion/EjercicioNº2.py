'''Escribir un código que muestre en orden alfabético las palabras ingresadas'''

print("BIENVENIDO")
contador=int(input("Ingrese la cantidad de palabras a escribir:"))
listalfabetica=[]
for i in range(contador):
     mylista=input("Ingrese una palabra: ")
     listalfabetica.append(mylista)
     listalfabetica.sort()#funcion "sort" nos permite oredenar en forma alfabetica las palabras
else: 
        print("Palabras ordenadas Alfabeticamente...")
        print(listalfabetica)
        print ("Muchas Gracias")