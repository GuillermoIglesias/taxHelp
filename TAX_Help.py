# Proyectos en TIC I 

from GUI_Login import *
from GUI import *
from Tkinter import *

# INSTRUCCIONES: 
# - Este es el programa principal
# - Se utiliza para unir ambas interfaces graficas
# - Deben estar los siguientes archivos en conjunto: 
# 	GUI.py, GUI_Login.py, Account.py, Save_Load.py, Calculator.py, Datos_SII.py
#	Ademas de la carpeta 'save' donde se almacenaran los usuarios creados
# - Para ejecutar requiere instalado Python27
# - Utilizar la linea de comandos: python TAX_Help.py

GUI_Login = Tk()
username, password = Login_Screen(GUI_Login)
GUI_Login.destroy()
GUI(username,password)