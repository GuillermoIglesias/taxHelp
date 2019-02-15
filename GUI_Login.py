# Programa encargado de la administracion de la Interfaz Grafica del Usuario para validar cuentas nuevas
from Tkinter import *
from Account import *
import tkMessageBox
import re

def Login_Screen(GUI_Login):

	def Boton_Ingresar():
		user  = username.get()
		passw = password.get()
		if len(user) == 0 or len(passw) == 0:
			tkMessageBox.showerror("Error","Por favor ingrese usuario y/o contrasena.")	
			return
		if Login(user,passw) == False:
			# Colocar lo que ocurre si el usuario es incorrecto
			tkMessageBox.showerror("Error","Usuario y/o contrasena incorrectos.")
		else:
			# Una vez realizada la validacion se cierra la interfaz para abrir la siguiente
			GUI_Login.quit()

	def Boton_Registrarse():
		user  = username.get()
		passw = password.get()
		# Validar los valores ingresados
		valid_user = re.findall(r'\W', user)
		valid_passw = re.findall(r'\W', passw)
		if not len(valid_user) == 0 or not len(valid_passw) == 0:		
			tkMessageBox.showerror("Error","El usuario y/o contrasena solo debe contener valores alfanumericos.")
			return
		if len(user) == 0 or len(passw) == 0:
			tkMessageBox.showerror("Error","Por favor ingrese usuario y/o contrasena.")	
			return
		if Registrar(user,passw) == False:
			# Colocar lo que ocurre si el usuario ya existe
			tkMessageBox.showerror("Error","Usuario ya existente.")
		else:
			tkMessageBox.showinfo("Correcto","Usuario creado existosamente!")

	# Inicializacion de interfaz grafica
	# GUI_Login = Tk() 
	GUI_Login.title("TAX Help Login Screen")

	# Etiquetas de cada opcion
	user_label = Label(GUI_Login, text = "Username:")
	user_label.grid(row = 2, column = 0, pady = 2, padx = 4)

	pass_label = Label(GUI_Login, text = "Password:")
	pass_label.grid(row = 3, column = 0, pady = 2, padx = 4)

	# Espacio para ingresar los datos
	username = Entry(GUI_Login, justify = CENTER)
	username.grid(row = 2, column = 1, pady = 2, padx = 4)
	password = Entry(GUI_Login, justify = CENTER, show = "*")
	password.grid(row = 3, column = 1, pady = 2, padx = 4)

	# Botones de la interfaz
	login_button = Button(GUI_Login, text = "Ingresar", command = Boton_Ingresar)
	login_button.grid(row = 4, column = 0, pady = 8, padx = 4)

	regis_button = Button(GUI_Login, text = "Registrarse", command = Boton_Registrarse)
	regis_button.grid(row = 4, column = 1, pady = 8, padx = 4)

	# Titulo de la interfaz
	Title = Label(GUI_Login, text = "Bienvenido a TAX Help!", justify = CENTER, font = "Verdana 10 bold")
	Title.grid(row = 0, column = 0, columnspan = 2, pady = 4, padx = 8)

	# Instrucciones de la interfaz
	Title2 = Label(GUI_Login, text = "Por favor ingrese sus datos", justify = CENTER, font = "Verdana 8 italic")
	Title2.grid(row = 1, column = 0, columnspan = 2, pady = 4, padx = 8)

	# Loop que permite el funcionamiento de la GUI
	GUI_Login.mainloop()

	# Retorna username y password del usuario para interactuar con el resto del programa
	return username.get(), password.get()