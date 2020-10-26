from cryptography.fernet import Fernet
import os
# funciones para crear key de acceso


def GENERA_KEY_DE_ACCESO () :

	KEY = Fernet.generate_key()
	with open ( (NOMBRE_DE_ARCHIVO + str(".key")) ,"wb") as ARCHIVO_DE_ACCESO :
		ARCHIVO_DE_ACCESO.write(KEY)

def CARGA_KEY_DE_ACCESO ():

	return open( (NOMBRE_DE_ARCHIVO + str(".key")) ,"rb").read()


def ENCRIPTADO_DE_ARCHIVOS (NOMBRE_DE_ARCHIVO,KEY):
	
	f = Fernet(KEY);
	with open (NOMBRE_DE_ARCHIVO,"rb") as file :
		ARCHIVO_A_ENCRIPTAR = file.read()
	DATOS_ENCRIPTADOS = f.encrypt(ARCHIVO_A_ENCRIPTAR)
	with open (NOMBRE_DE_ARCHIVO, "wb") as file:
		file.write(DATOS_ENCRIPTADOS)

def DESENCRIPTADO_DE_ARCHIVOS (NOMBRE_DE_ARCHIVO,acceso):
	
	f = Fernet(KEY);
	with open (NOMBRE_DE_ARCHIVO,"rb") as file :
		ARCHIVO_A_DESENCRIPTAR = file.read()
	DATOS_DESENCRIPTADOS = f.decrypt(ARCHIVO_A_DESENCRIPTAR)
	with open (NOMBRE_DE_ARCHIVO, "wb") as file:
		file.write(DATOS_DESENCRIPTADOS)

def borrarPantalla():
	if os.name == "posix":
   		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   		os.system ("cls")

# empieza el proceso de encriptado

OPCION = 0
borrarPantalla()

print ("=======================")
print ("Seleccione una opcion :")
print ("=======================")
print ("by : D3f4ul7 ;)")
print ("=======================")

print ("1. ENCRIPTAR")
print ("2. DESENCRIPTAR")

OPCION = int(input())

if OPCION == 1 :

	borrarPantalla()
	print ("============")
	print (" ENCRIPTAR  ")
	print ("============")
	print ("Digite la ruta o el nombre del archivo a encriptar: ")
	NOMBRE_DE_ARCHIVO = input()
	GENERA_KEY_DE_ACCESO() 
	KEY = CARGA_KEY_DE_ACCESO()
	ENCRIPTADO_DE_ARCHIVOS (NOMBRE_DE_ARCHIVO,KEY)
	print ("listo...")
	print ("Se ha encriptado y creado un archivo llamado " + str(NOMBRE_DE_ARCHIVO) + ".key en la ruta: ")
	os.system("pwd")
	print ("guarda muy bien este archivo para desencriptar despues")

if OPCION == 2 :

	borrarPantalla()
	print ("============")
	print ("DESENCRIPTAR")
	print ("============")
	print ("Digite la ruta o el nombre del archivo a encriptar: ")
	NOMBRE_DE_ARCHIVO = input()
	KEY = CARGA_KEY_DE_ACCESO()
	DESENCRIPTADO_DE_ARCHIVOS (NOMBRE_DE_ARCHIVO,KEY)
	f = open (NOMBRE_DE_ARCHIVO , "r")
	IMPRIMIR = f.read()
	print (IMPRIMIR)
	f.close()
	print ("listo...")
	print ("Archivo desencriptado en: ")
	os.system("pwd")
