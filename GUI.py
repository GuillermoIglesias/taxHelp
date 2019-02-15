# Programa encargado de administrar la Interfaz Grafica del Usuario principal
from Tkinter import *
from Save_Load import *
from Calculator import *
import string
import tkMessageBox

def GUI(username, password):

	# Comprueba que los valores ingresados sean solo numericos
	def Check_Data(data1,data2):
		for i in range(12):
			if not data1[i].isdigit() or not data2[i].isdigit():
				return False
		return True

	# Extrae toda la informacion existente en la pantalla de la GUI
	def Get_Data():
		# Todos los valores no ingresados, seran reemplazados por 0
		# Almacenar los valores ingresados en strings[0-11]
		Sueldo_str, Hon_str = [], []
		for i in range(12):
			if not Sueldo[i].get():
				Sueldo_str.append(str('0'))
			else:
				Sueldo_str.append(Sueldo[i].get())
			if not Honorario[i].get():
				Hon_str.append(str('0'))
			else:
				Hon_str.append(Honorario[i].get())
		
		# Chequear si los valores son validos
		if Check_Data(Sueldo_str,Hon_str):
			return Sueldo_str, Hon_str
		else:
			# Caso contrario, enviar mensaje de error
			tkMessageBox.showerror("Error", "Datos ingresados invalidos, por favor ingresar solo valores numericos.")
			return -1,-1

	# Almacena los datos ingresados por el usuario en username_password.txt
	def Boton_Guardar():
		if tkMessageBox.askyesno("Atencion","Si guarda los datos ingresados, se sobreescribira la informacion anteriormente guardada, desea continuar?"):
			sueldo_data, honorario_data = Get_Data()
			if not sueldo_data == -1 or not honorario_data == -1:
				# Guarda los datos en el usuario ingresado anteriormente
				Save(username, password, sueldo_data, honorario_data)
				tkMessageBox.showinfo("Exito","Datos guardados exitosamente!")

	# Carga todos los datos guardados por el usuario anteriormente
	def Boton_Cargar():
		if tkMessageBox.askyesno("Atencion","Desea cargar los datos guardados? Se perdera toda la informacion no guardada anteriormente."):
			# Limpiar la pantalla antes de ingresar los datos
			Limpiar()
			# Carga los datos desde el txt del usuario
			sueldo_data, honorario_data = Load(username, password)
			# Rellena la interfaz con los valores correspondientes
			# En caso de ser 0 el valor, este se no se coloca
			for i in range(12):
				if not sueldo_data[i] == '0':
					Sueldo[i].insert(END, sueldo_data[i])
				if not honorario_data[i] == '0':
					Honorario[i].insert(END, honorario_data[i])

	# Muestra los resultados de la estimacion de impuestos
	def Boton_Calcular():
		sueldo_data, honorario_data = Get_Data()
		if not sueldo_data == -1 or not honorario_data == -1:
			# Limpieza de resultados anteriores
			Limpiar_Resultados()
			
			# Obtencion de resultados
			condicion = tkMessageBox.askyesno("Atencion","Desea realizar una proyeccion de sus datos? De lo contrario se calculara el impuesto normalmente.")
			if condicion:
				result = Resultado_Estimado(sueldo_data,honorario_data,condicion)
				impto1, impto2 = Impuesto_Mensual(sueldo_data, honorario_data, condicion)
			else:
				result = Resultado_Estimado(sueldo_data,honorario_data,condicion)
				impto1, impto2 = Impuesto_Mensual(sueldo_data, honorario_data, condicion)
			
			# Impresion de impuestos retenidos para meses ingresados
			for i in range(12):
				if not sueldo_data[i] == '0':
					Impuesto_S[i].config(state = NORMAL)
					Impuesto_S[i].insert(END, impto1[i])
					Impuesto_S[i].config(state = DISABLED)
				if not honorario_data[i] == '0':
					Impuesto_H[i].config(state = NORMAL)
					Impuesto_H[i].insert(END, impto2[i])
					Impuesto_H[i].config(state = DISABLED)

			# Impresion de resultado estimacion
			Resultado.config(state = NORMAL)
			Resultado.insert(END, str(result))
			Resultado.config(state = DISABLED)
			if result > 0:
				Proyeccion_Signo.config(text = "Impuesto a pagar")
			else:
				Proyeccion_Signo.config(text = "Impuesto a recibir")

	# Limpia valores de pantalla de la GUI
	def Limpiar():
		for i in range(12):
			Sueldo[i].delete(0, END)
			Honorario[i].delete(0, END)
		Limpiar_Resultados()

	def Boton_Limpiar():
		if tkMessageBox.askyesno("Atencion","Desea limpiar todos los campos? Se perdera toda la informacion no guardada anteriormente."):
			Limpiar()

	# Cierra el programa
	def Boton_Salir():
		if tkMessageBox.askyesno("Atencion","Desea salir del programa?"):
			GUI.quit()

	# Limpia solamente los valores de calculo
	def Limpiar_Resultados():
		for i in range(12):
			Impuesto_S[i].config(state = NORMAL)
			Impuesto_H[i].config(state = NORMAL)
			Impuesto_S[i].delete(0,END)
			Impuesto_H[i].delete(0,END)
			Impuesto_S[i].config(state = DISABLED)
			Impuesto_H[i].config(state = DISABLED)
		Resultado.config(state = NORMAL)
		Resultado.delete(0,END)
		Resultado.config(state = DISABLED)
		Proyeccion_Signo.config(text = "")


	# Inicializacion de interfaz grafica
	GUI = Tk()
	GUI.title("TAX Help")

	# Titulos de cada columna
	Mes = Label(GUI, text = "          Mes          ", justify = CENTER, font = "Verdana 8 bold", relief = GROOVE)
	Mes.grid(row = 2, column = 0, pady = 6)
	Sueldo = Label(GUI, text = "  Sueldos Imponibles  ", justify = CENTER, font = "Verdana 8 bold", relief = GROOVE)
	Sueldo.grid(row = 2, column = 1, pady = 6)
	Impto_Sueldo = Label(GUI, text = "  Impuestos Retenidos  ", justify = CENTER, font = "Verdana 8 bold", relief = GROOVE)
	Impto_Sueldo.grid(row = 2, column = 2, pady = 6)
	Honorario = Label(GUI, text = "   Honorarios Brutos   ", justify = CENTER, font = "Verdana 8 bold", relief = GROOVE)
	Honorario.grid(row = 2, column = 3, pady = 6)
	Impto_Honorario = Label(GUI, text = "  Impuestos Retenidos  ", justify = CENTER, font = "Verdana 8 bold", relief = GROOVE)
	Impto_Honorario.grid(row = 2, column = 4, pady = 6)

	# Generar planilla de interfaz
	Sueldo, Honorario, Impuesto_S, Impuesto_H = [], [], [], []
	Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
			"Noviembre", "Diciembre"]
			
	# Variables ENTRY almacenan los datos ingresados por el usuario
	for i in range(12):
		Sueldo_entry = Entry(GUI, justify = RIGHT)
		Sueldo_entry.grid(row = i+3, column = 1)
		Sueldo.append(Sueldo_entry)

		Honorario_entry = Entry(GUI, justify = RIGHT)
		Honorario_entry.grid(row = i+3, column = 3)
		Honorario.append(Honorario_entry)

		Mes_label = Label(GUI, text = Meses[i])
		Mes_label.grid(row = i+3, column = 0)

		Impuesto_S_entry = Entry(GUI, justify = RIGHT, state = DISABLED)
		Impuesto_H_entry = Entry(GUI, justify = RIGHT, state = DISABLED)
		Impuesto_S_entry.grid(row = i+3, column = 2)
		Impuesto_H_entry.grid(row = i+3, column = 4)
		Impuesto_S.append(Impuesto_S_entry)
		Impuesto_H.append(Impuesto_H_entry)

	# Lugar donde se imprimira el resultado final
	Proyeccion = Label(GUI, text = "Resultado:", justify = CENTER, font = "Verdana 8 bold")
	Proyeccion.grid(row = 15, column = 1, columnspan = 2, pady = 8, padx = 8)

	Proyeccion_Signo = Label(GUI, text = "", font = "Verdana 8 italic")
	Proyeccion_Signo.grid(row = 15, column = 3, columnspan = 2, pady = 8, padx = 8)

	Resultado = Entry(GUI, justify = CENTER, state = DISABLED)
	Resultado.grid(row = 15, column = 2, columnspan = 2, pady = 8, padx = 8)

	# Botones de la interfaz
	Save_button = Button(GUI, text = 'Guardar Datos', command = Boton_Guardar)
	Save_button.grid(row = 16, column = 0, pady = 8, padx = 8)

	Load_button = Button(GUI, text = 'Cargar Datos', command = Boton_Cargar)
	Load_button.grid(row = 16, column = 1, pady = 8, padx = 8)

	Calc_button = Button(GUI, text = 'Calcular Resultado', command = Boton_Calcular)
	Calc_button.grid(row = 16, column = 2, pady = 8, padx = 8)

	Clean_button = Button(GUI, text = 'Limpiar Pantalla', command = Boton_Limpiar)
	Clean_button.grid(row = 16, column = 3, pady = 8, padx = 8)

	Leave_button = Button(GUI, text = 'Salir del Programa', command = Boton_Salir)
	Leave_button.grid(row = 16, column = 4, pady = 8, padx = 8)

	# Titulo de la GUI
	Title = Label(GUI, text = "TAX HELP", justify = CENTER, font = "Verdana 14 bold")
	Title.grid(row = 0, columnspan = 5, pady = 6, padx = 8)

	# Instrucciones de la GUI
	Instrucciones = Label(GUI, text = "Instrucciones: Este programa le permite realizar una estimacion de la suma de pago/devolucion de impuestos \n"
										"para el siguiente periodo tributario, ingrese los datos correspondientes y luego presione el boton 'Calcular'.", justify = CENTER, font = "Verdana 8 italic")
	Instrucciones.grid(row = 1, columnspan = 5, padx = 8)

	# Loop que permite el funcionamiento de la GUI
	GUI.mainloop()