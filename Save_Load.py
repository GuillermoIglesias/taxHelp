# Funciones encargadas de Guardar y Cargar la informacion del usuario
import os.path

def Save(username,password,sueldos,honorarios):
	# Nombre archivo del usuario
	file_name = username + '_' + password + '.txt'
	file_dir = 'save'
	# Directorio archivo
	file_path = os.path.join(file_dir, file_name)
	# Abrir el archivo
	save_file = open(file_path,"w")

	# Se escriben los valores dentro del txt
	# Dentro del archivo los datos tienen la forma
	# Sueldo1 Honorario1 
	# Sueldo2 Honorario2 
	for i in range(len(sueldos)):
		save_file.write(sueldos[i])
		save_file.write(" %s\n" % honorarios[i])

	# Guardar archivo
	save_file.close()

def Load(username,password):
	# Nombre archivo del usuario
	file_name = username + '_' + password + '.txt'
	file_dir = 'save'
	# Directorio archivo
	file_path = os.path.join(file_dir, file_name)
	# Abrir el archivo
	load_file = open(file_path,"r")

	Sueldos, Honorarios = [], []
	# Traspasa los valores a dos arreglos
	for line in load_file:
		values = line.split()
		Sueldos.append(values[0])
		Honorarios.append(values[1])
		
	# Cerrar el archivo
	load_file.close()

	return Sueldos, Honorarios
