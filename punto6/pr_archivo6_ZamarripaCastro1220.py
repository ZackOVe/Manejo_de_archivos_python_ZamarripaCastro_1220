print("")
print("Zamarripa Castro Erick Fabian 1220")
print("")

#Abrir el archivo en modo escribir
Algo_Andaba_Mal5 = open("Algo_Andaba_Mal5.txt", "w")

#ingresa la palabra que quieras ingresar al archivo
palabra=input("ingresa la palabra a agregar:")

#Escribir nuevo contenido en el archivo
Algo_Andaba_Mal5.write(palabra)

#Cerrar el archivo
Algo_Andaba_Mal5.close()

#Abrir el archivo en modo lectura para mostrar el nuevo contenido
Funcion = open("Algo_Andaba_Mal5.txt", "r")

print(Funcion.read())

#Cerrar el archivo después de leer
Funcion.close()