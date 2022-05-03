# Ejercicio 7- Matias Avalo
for i in range(1):
  nom=input("Ingrese su Nombre:")
  ape=input("Ingrese Su Apellido:")
  edad=float(input("Ingrese su Edad:"))
  diner=float(input("Ingrese el dinero que hay en su billetera:$"))
  hambr=int(input("¿Cuanto hambre tiene? 1 a 10:"))

if edad<35 and edad ==18:
    print(f"Hola {nom}"   "Eres una persona joven ya que tu edad es:",edad)
elif edad>=34 and diner>=500 and hambr>5:
    print(f"Hola {nom} {ape}" " ¿Hoy hay asado?")
elif (hambr >7 and diner <100 and edad<18):
    print(f"Hola {nom} {ape}" " ¿Vas a comer en lo de tus Papas")
else:
    print("Quedate en casa")