# Funciones encargadas de extraer los datos necesarios desde la pagina del SII
import urllib2 
import re 

# Extraccion de valores de la tabla de impuesto unico de segunda categoria
def Tabla_Impuesto_Unico():
	# Numero de Columnas
	n = 5
	# Numero de Filas
	m = 8

	# Listas con Datos de Rango
	rango_1 = []
	rango_2 = []
	rango_3 = []
	rango_4 = []
	rango_5 = []
	rango_6 = []
	rango_7 = []
	rango_8 = []

	# Matriz que almacena valores de Tabla
	Tabla = []
	
	# Inicializacion Matriz
	for i in range(m):
		Tabla.append([])
		for j in range(n):
			Tabla[i].append(0.0)

	# Se extraen datos desde la pagina de SII
	url   = 'http://www.sii.cl/pagina/valores/segundacategoria/imp_2da_septiembre2016.htm'
	page  = urllib2.urlopen(url)
	html  = page.read()

	# Se Buscan los Datos de la Tabla de Impuestos
	datos_tabla = re.findall(r'<td.*</td>', html , flags = re.DOTALL)
	
	# Se Limpia el String
	datos_str = re.findall(r'([0-9A-X\.\,\_]+)', datos_tabla[0])
	
	# Se Guardan los valores en cada lista de Rango
	for i in range(0,len(datos_str)):
		if datos_str[i+1] == '_' or datos_str[i+1] =='E':
			datos_str[i+1] = '0' 

		if i < 5 :
			rango_1.append(datos_str[i+1].replace('.',''))

		if i >= 5 and i < 10:
			rango_2.append(datos_str[i+1].replace('.',''))

		if i >= 10 and i < 15 :
			rango_3.append(datos_str[i+1].replace('.',''))

		if i >= 15 and i < 20 :
			rango_4.append(datos_str[i+1].replace('.',''))

		if i >= 20 and i < 25 :
			rango_5.append(datos_str[i+1].replace('.',''))

		if i >= 25 and i < 30 :
			rango_6.append(datos_str[i+1].replace('.',''))

		if i >= 30 and i < 35 :
			rango_7.append(datos_str[i+1].replace('.',''))

		if i >= 35 and i < 40 :
			rango_8.append(datos_str[i+1].replace('.',''))

		if i >= 40:
			break

	# Se Guardan las Listas en la Matriz
	for i in range(0,len(rango_1)):
		Tabla[0][i] = rango_1[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[1][i] = rango_2[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[2][i] = rango_3[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[3][i] = rango_4[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[4][i] = rango_5[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[5][i] = rango_6[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[6][i] = rango_7[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[7][i] = rango_8[i].replace(',','.')


	# NO QUITAR
	Tabla[0][3] = '0'

	return Tabla

# Extraccion de valores de la tabla de impuesto global
def Tabla_Impuesto_Global():
	# Numero de columnas
	n = 4
	# Numero de filas
	m = 8

	# Listas con Datos de Rango
	rango_1 = []
	rango_2 = []
	rango_3 = []
	rango_4 = []
	rango_5 = []
	rango_6 = []
	rango_7 = []
	rango_8 = []
	rango_9 = []

	# Matriz que almacena valores de Tabla
	Tabla = []

	# Inicializacion Matriz	
	for i in range(m):
		Tabla.append([])
		for j in range(n):
			Tabla[i].append(None)

	# Se extraen datos desde la pagina de SII
	url   = 'http://www.sii.cl/pagina/valores/global/igc2016.htm'
	page  = urllib2.urlopen(url)
	html  = page.read()

	# Se Buscan los Datos de la Tabla de Impuestos
	datos_tabla = re.findall(r'<p align="center">.*</p></td>', html , flags = re.DOTALL)

	# Se Limpia el String
	datos_str = re.findall(r'([0-9A-X\.\,]+)', datos_tabla[0])
	
	# Se Guardan los valores en cada lista de Rango
	for i in range(0,len(datos_str)):
		if datos_str[i+39] == '175' or datos_str[i+39] == '80' or datos_str[i+39] == '265' or datos_str[i+39] == '141'  :
			continue
		if datos_str[i+39] == 'EXENTO':
			datos_str[i+39] = '0'

		if i < 8:
			rango_1.append(datos_str[i+39].replace('.',''))

		if i >= 7 and i < 15:
			rango_2.append(datos_str[i+39].replace('.',''))

		if i >= 15 and i < 23 :
			rango_3.append(datos_str[i+39].replace('.',''))

		if i >= 23 and i < 31 :
			rango_4.append(datos_str[i+39].replace('.',''))

		if i >= 31 and i < 39 :
			rango_5.append(datos_str[i+39].replace('.',''))

		if i >= 39 and i < 47 :
			rango_6.append(datos_str[i+39].replace('.',''))

		if i >= 47 and i < 55 :
			rango_7.append(datos_str[i+39].replace('.',''))

		if i >= 55 and i < 63 :
			rango_8.append(datos_str[i+39].replace('.',''))

		if i >= 63:
			break


	# Se Guardan las Listas en la Matriz
	for i in range(0,len(rango_1)):
		Tabla[0][i] = rango_1[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[1][i] = rango_2[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[2][i] = rango_3[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[3][i] = rango_4[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[4][i] = rango_5[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[5][i] = rango_6[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[6][i] = rango_7[i].replace(',','.')
	for i in range(0,len(rango_1)):
		Tabla[7][i] = rango_8[i].replace(',','.')

	return Tabla

# Extraccion del valor actual de la unidad tributaria anual
def Valor_UTA():

	# Se Extrae valor desde la Pagina del SII
	url   = 'http://www.sii.cl/pagina/valores/global/igc2016.htm'
	page  = urllib2.urlopen(url)
	html  = page.read()

	# Se Busca el valor 
	datos_uta = re.findall(r'<td width="486" colspan="3" valign="top"><p><strong>.*</strong> </p></td>', html , flags = re.DOTALL)

	# Se Limpia el String en busca de los Numeros
	datos_str = re.findall(r'([0-9\.]+)', datos_uta[0])

	# Se extrae solo el valor de la UTA
	valor_UTA = datos_str[3].replace('.','')	
	valor_UTA = float(valor_UTA)*12

	return valor_UTA