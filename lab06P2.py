import hashlib
import hmac
import codecs

# PARTE 2
# Lee el archivo deseado
original_file = open("data.txt", "r")
mensaje = original_file.read()
# Recibe el mensaje del txt oiriginal
# Modifica el mensaje
new_message = mensaje.replace("a", "d")
# Guarda el mensaje en el nuevo txt
copy_file = open("copy_data.txt", "w+")
copy_file.write(new_message + "\n")
original_file.close()
copy_file.close()


def generateHash(filename, password):
    try:
        # Lee el archivo a codificar
        original_file = open(filename, "r")
        mensaje = original_file.read()
        mensaje = bytes(mensaje, 'utf-8')
        password = bytes(password, 'utf-8')

        hash = hashlib.sha256()
        hash.update(mensaje)
        hash.update(password)
        # Encripta el mensaje del archivo con la clave
        result = hash.hexdigest()
        # Escribe el resultado en otro txt para comparar
        compareFile = open("compare_data.txt", "a+")
        compareFile.write(result + "\n")
        original_file.close()
        compareFile.close()
    except OSError:
        print("Could not open/read file:", filename)
    print("Hash generado ")


filename = input("Ingrese el archivo al que desee generar hash (data.txt):\n")
password = input("ingrese la clave del archivo:\n")

generateHash(filename, password)
