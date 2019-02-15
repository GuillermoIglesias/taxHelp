# Funciones encargadas de Crear y Validar usuarios
import os.path

def Registrar(user, password):
	# Directorio a guardar
	file_dir = 'save'
	
	# Nombre archivo
	file_name = user + '_' + password + '.txt'
	
	# Checkear que el archivo no exista previamente
	if os.path.isfile("save/" + file_name):
		return False
	
	# Directorio archivo
	file_path = os.path.join(file_dir, file_name)
	
	# Crear archivo
	user_file = open(file_path, "w")

	# Se llenan los espacios default
	for i in range(0,12):
		user_file.write("0 0\n")
	
	# Cierra el archivo para guardar los cambios
	user_file.close()

	# Usuario creado existosamente
	return True

def Login(user, password):
	# Nombre archivo
	file_name = user + '_' + password + '.txt'

	# True si el archivo del usuario existe
	return os.path.isfile("save/" + file_name)
