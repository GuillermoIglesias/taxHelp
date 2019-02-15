# Funciones encargadas de los calculos pertinentes para estimar proyecciones de impuestos
from Datos_SII import *

# Calculo de la proyeccion de los honorarios
def Proyecciones(Sueldos, Honorarios, Condicion):

	cont = 0
	cont2 = 0
	aux = 0
	aux2 = 0
	Suma_Honorarios = 0
	Suma_Sueldos = 0
	Proyeccion_Honorarios = []
	Proyeccion_Sueldos = []

	if Condicion == True:
		for i in range(0,12):
			Proyeccion_Honorarios.append('0')
			Proyeccion_Sueldos.append('0') 

		for i in range(0,len(Honorarios)):
			if not float(Honorarios[i]) == 0:
				cont = cont + 1

			Suma_Honorarios = Suma_Honorarios + float(Honorarios[i])

		if cont == 0:
			Promedio_Honorarios = 0
		else: 
			Promedio_Honorarios = Suma_Honorarios/cont

		for i in range(0,len(Sueldos)):
			if not float(Sueldos[i]) == 0:
				cont2 = cont2 + 1

			Suma_Sueldos = Suma_Sueldos + float(Sueldos[i])

		if cont2 == 0:
			Promedio_Sueldos = 0
		else:
			Promedio_Sueldos = Suma_Sueldos/cont2

		for i in xrange(len(Sueldos)-1, -1, -1):
			if Sueldos[i] == '0':
				aux2 = aux2 + 1
			else:
				break

		for i in xrange(len(Honorarios) -1, -1, -1):
			if Honorarios[i] == '0':
				aux = aux + 1
			else:
				break

		if aux >= aux2:
			num = aux2
		else:
			num = aux

		for i in range(0,len(Sueldos)-num):
			Proyeccion_Sueldos[i] = Sueldos[i]
			Proyeccion_Honorarios[i] = Honorarios[i]

		for i in range(len(Sueldos)-num, len(Sueldos)):
			Proyeccion_Sueldos[i] = str(Promedio_Sueldos)
			Proyeccion_Honorarios[i] = str(Promedio_Honorarios)

		return Proyeccion_Sueldos, Proyeccion_Honorarios

	else:
		return Sueldos, Honorarios


# Calculo del total del impuesto real a pagar
def Total_Impuesto_SII(Sueldos, Honorarios, Condicion):

	suma = 0
	Suma_Honorarios = 0
	Gasto_Presunto = 0

	Proyeccion_Sueldos, Proyeccion_Honorarios  = Proyecciones(Sueldos,Honorarios,Condicion)

	Tabla_Global = Tabla_Impuesto_Global()

	# Suma de todos sueldos y honorarios
	for i in range(0,len(Proyeccion_Sueldos)):
		suma = suma + float(Proyeccion_Sueldos[i]) + float(Proyeccion_Honorarios[i])
	

	for i in range(0,len(Proyeccion_Honorarios)):
		Suma_Honorarios = Suma_Honorarios + float(Proyeccion_Honorarios[i])

	# Calculo de Gastos Presuntos
	
	UTA = Valor_UTA()

	if Suma_Honorarios*0.3 > 15*UTA:
		Gastos_Presuntos = 15*UTA
	else:
		Gastos_Presuntos = Suma_Honorarios*0.3
		
	suma = suma - Gastos_Presuntos

	# SumaAnterior * FactorTabla - CantidadRebajada
	for i in range(0,8):
		if Tabla_Global[i][1] == 'MAS':
			Impuesto_Pagar = suma*float(Tabla_Global[i][2]) - float(Tabla_Global[i][3])
			break

		if float(Tabla_Global[i][0]) <= suma and suma <= float(Tabla_Global[i][1]):
			Impuesto_Pagar = suma*float(Tabla_Global[i][2]) - float(Tabla_Global[i][3]) 
			break



	return str(Impuesto_Pagar)

# Calculo de los impuestos retenidos para cada mes procedentes de sueldos
def Impuesto_Mensual(Sueldos, Honorarios, Condicion):

	Impuesto_Mensual_Sueldos = []
	Impuesto_Mensual_Honorarios = [] 
	Proyeccion_Sueldos, Proyeccion_Honorarios = Proyecciones(Sueldos, Honorarios, Condicion)
	Tabla_Segunda_Categoria = Tabla_Impuesto_Unico()



	for i in range(0,12):
		Impuesto_Mensual_Sueldos.append('0')
		Impuesto_Mensual_Honorarios.append('0')


	# Suma de todos los impuestos correspondientes a cada mes por sueldos
	# Sumatoria( SueldoImponible * FactorTabla - CantidadRebajada )
	for j in range(0,12):
		for i in range(0,8):
			if Tabla_Segunda_Categoria[i][1] == 'MAS':
				Impuesto_Mensual_Sueldos[j] = str(int(float(Proyeccion_Sueldos[j])*float(Tabla_Segunda_Categoria[i][2]) - float(Tabla_Segunda_Categoria[i][3])))
				break
				
			if float(Tabla_Segunda_Categoria[i][0]) <= float(Proyeccion_Sueldos[j]) and float(Proyeccion_Sueldos[j]) <= float(Tabla_Segunda_Categoria[i][1]):
				Impuesto_Mensual_Sueldos[j] = str(int(float(Proyeccion_Sueldos[j])*float(Tabla_Segunda_Categoria[i][2]) - float(Tabla_Segunda_Categoria[i][3])))
				break		

	# Suma de todos los impuestos correspondientes a cada mes por honorarios
	# Sumatoria( HonorarioBruto * 0.1 )
	for i in range(0,len(Proyeccion_Honorarios)):
		Impuesto_Mensual_Honorarios[i] = str(int(float(Proyeccion_Honorarios[i])*0.1))

	return Impuesto_Mensual_Sueldos, Impuesto_Mensual_Honorarios



# Funcion principal, calcula el monto estimado que debera pagarse o devolverse
def Resultado_Estimado(Sueldos, Honorarios, Condicion):

	Impuestos_Sueldos_Retenido  = 0
	Impuestos_Honorarios_Retenido = 0	

	Impuesto_Real_Pagar = Total_Impuesto_SII(Sueldos, Honorarios, Condicion)

	# Lista de impuestos retenidos
	Impuesto_Pagado_Mensual, Impuesto_Pagado_Honorarios = Impuesto_Mensual(Sueldos,Honorarios,Condicion)
	

	# Calculo de los impuestos totales retenidos
	for i in range(0,12):
		Impuestos_Sueldos_Retenido = Impuestos_Sueldos_Retenido + float(Impuesto_Pagado_Mensual[i]) 
		Impuestos_Honorarios_Retenido = Impuestos_Honorarios_Retenido + float(Impuesto_Pagado_Honorarios[i])

	# Resultado final: Impuesto real a pagar - Impuestos totales retenidos
	Impuestos_Anual_Tributario = float(Impuesto_Real_Pagar) - Impuestos_Sueldos_Retenido - Impuestos_Honorarios_Retenido

	return int(Impuestos_Anual_Tributario)
