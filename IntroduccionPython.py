# Los comentarios en python se hacen por medio de '#' 
# Esto es evidentemente un comentario de una linea

# 1. Python se recorre en orden de arriba abajo

    # Mal!
#print(a) = a no Existe
#a = 5


    # Bien!
#print("a") = a
#a = 5
#print(a) = 5


#2. Los dos tipos de bucles son el WHILE y el FOR, y se usan los ':' para determinar el comienzo de un bloque de código
while(True):
    #Esto es un bucle infinito
    print("Bucle Infinito")

for a in range(10):
    #Este bucle se ejecuta 10 veces (0,10)
    print(a)

    