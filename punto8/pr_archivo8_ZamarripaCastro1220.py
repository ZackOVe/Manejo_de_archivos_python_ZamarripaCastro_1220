print("")
print("Zamarripa Castro Erick Fabian 1220")
print("")

import os

# Verificar si el archivo "demofile.txt" existe
if os.path.exists("Algo_Andaba_Mal7.txt"):
    # Si existe, eliminar el archivo
    os.remove("Act7.txt")
    print("El archivo 'Algo_Andaba_Mal7.txt' ha sido eliminado.")
else:
    # Si no existe, imprimir un mensaje
    print("El archivo 'Algo_Andaba_Mal7.txt' no existe.")
