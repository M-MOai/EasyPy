# Importo las BIBLIOTECAS necesarias si alguna no te la reconoce deberás hacer "py install shutil"
import os 
import getpass
import subprocess
import shutil 

# Almaceno en las variables username y CurrentDir el nombre del usuario y el directorio en el que está el .py respectivamente
username = getpass.getuser()
currentDir = os.getcwd()

# Imprimo dichas variables para comprobar sus valores {Aparencen en la consola}
print("Nombre de usuario: " + username)
print("Directorio actual de ejec: " + currentDir)

# Declaro como variable el directorio actual + el nombre de mi archivo; es decir--> mi ruta absoluta 
MyPythonPath = currentDir + "\\HelloWorld.pyw"

# Mientras que a esté entre 0 y 5 siendo a = a + 1 cada vez...
for a in range(5):
    #destino = directorio actual + Nombre Archivo + a(0-5) + extensión
    dst = currentDir + "\\HelloWorld" + str(a) +".pyw"
    # Utilizo shutil copy pasandole el origen y el destino
    shutil.copy(MyPythonPath, dst)
