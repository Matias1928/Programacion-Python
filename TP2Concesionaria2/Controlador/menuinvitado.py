from Data.AlmacenarAuto import agregaAutos
from Vehiculos.Auto import Auto
def  menuInvitado ():
    usuario=int(input(("Menú Invitado \n 1:Ver Vehiculos \n 2:Salir \n Ingrese la operación deseada:" )))

    if usuario == 1:
     print('Listado de Vheiculos')
     agregaAutos()