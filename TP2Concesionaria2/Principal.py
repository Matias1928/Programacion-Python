from Controlador.menuadmin import menuAdmin
from Interfaz.vista import interfaz
from Usuarios.Admin import admin
from Usuarios.Empleado import empleado
from Usuarios.Invitado import invitado
from Controlador.menuinvitado import menuInvitado
from Controlador.menuempleado import menuEmpleado
#Seleccion de Perfil.
interfaz()
#Ingreso de Perfil.
usuario=int(input("Seleccione su Perfil:"))
if usuario==1:
    #invitado()
    menuInvitado()
if usuario==2:
    #empleado()
    menuEmpleado()
if usuario==3:
    #admin()
    menuAdmin()