#CLASSES LLAMADAS DE Classes.py...
from Classes import Acoplados, Autos, Bicicletas, Camiones, Camioneta, Colectivo, Motos

#programa general
print("---CONCESIONARIA---")
print("    ***MENU***\n")
entrada=0
while entrada !=5: #ingreso de Menu y opcion deseada
    print("1--->VENDER  2--->CONTROL DE STOCK  3--->CARGAR STOCK  4--->SALIR\n")
    entrada=int((input("Ingrese Opcion: ")))
 #INTERACCION CON MENU   
    if entrada==1:
        print("USTED ELIGIO 'VENDER'")
        #entry=0 (opcional por si entrada no funciona)
        while entrada!=8:
            print("\n'-Que desea Vender-'\n")
            print("1-BICICLETAS 2-MOTOS 3-AUTOS 4-CAMIONETA 5-COLECTIVO 6-CAMIONES 7-ACOPLADOS 8-EXIT")

            entrada=int((input("Ingrese Opcion: ")))
            if entrada==1:#BICICLETA
                print("---Bicicletas---")
                x=input("ingrese Color:")
                biciclettas=Bicicletas(x)#declaracion y llamado de variable
                print("Bicicleta:",biciclettas.marca)
                print("Rodado:",biciclettas.rodado)
                print("Color:",biciclettas.color)
            if entrada == 2:#MOTOS
                print("---Motos---")
                x=input("ingrese Color:")
                motos=Motos(x)#declaracion y llamado de variable
                print("Moto:",motos.marca)
                print("Modelo",motos.modelo)
                print("Color:",motos.color)
            if entrada == 3:#AUTOS
                print("---Autos---")
                x=input("Ingrese 'Marca' deseada:")
                y=input("Ingrese Color:")
                autos=Autos(x,y)#declaracion y llamado de variable
                print("Auto:",autos.marca)
                print("Modelo:",autos.Modelo)
                print("Color:",autos.color)
            if entrada == 4:#CAMIONETAS
                print("---Camioneta---")
                x=input("Ingrese 'Marca' deseada:")
                y=input("Ingrese Color:")
                camioneta=Camioneta(x,y)#declaracion y llamado de variable
                print("Camioneta:",camioneta.marca)
                print("Modelo:",camioneta.Modelo)
                print("Color:",camioneta.color)
            if entrada == 5:#COLECTIVOS
                 print("---Colectivos---")
                 colectivos=Colectivo()#declaracion y llamado de variable
                 print("Colectivo:",colectivos.marca)
                 print("Modelo:",colectivos.modelo)
                 print("Color:",colectivos.color)
                 print("Cantidad de Acientos:",colectivos.acientos)
                 print("Cantidad de Pisos:",colectivos.piso)
            if entrada == 6:#CAMIONES
                print("---Camiones---")
                camiones=Camiones()#declaracion y llamado de variable
                print("camion:",camiones.marca)
                print("Modelo:",camiones.modelo)
                print("Color Unico:",camiones.color)
            if entrada== 7:#Acoplados
                print("---Acoplados---")
                acoplado=Acoplados()
                print("Acoplado:",acoplado.marca)
                print("Modelo:",acoplado.modelo)
                print("Color:",acoplado.color)
            if entrada==8:
                print("Muchas gracias por su servicio...")
    if entrada==4:
        print("Muchas gracias por su servicio...")
        break




