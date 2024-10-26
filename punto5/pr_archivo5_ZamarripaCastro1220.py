print("")
print("Zamarripa Castro Erick Fabian 1220")
print("")

# Abre el archivo "Algo_Andaba_Mal4.txt"
Algo_Andaba_Mal4 = open("Algo_Andaba_Mal4.txt", "a")

# Solicita al usuario que ingrese una palabra.
palabra = input("Ingresa la palabra a agregar:")

# Escribe la palabra en el archivo.
Algo_Andaba_Mal4.write(palabra)

# Cierra el archivo para guardar los cambios.
Algo_Andaba_Mal4.close()

# Abre el archivo en modo lectura para mostrar su contenido.
Funcion = open("Algo_Andaba_Mal4.txt", "r")

# Imprime el contenido del archivo.
print(Funcion.read())

# Cierra el archivo de lectura.
Funcion.close()
