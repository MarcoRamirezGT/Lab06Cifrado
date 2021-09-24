import hashlib
import hmac
import codecs

##PARTE 1##
# Sha256 en hex, bin y base64
texto = input("Ingrese el texto a cifrar:\n")
convertBits = bytes(texto, 'utf-8')


sha256Hex = hashlib.sha256(convertBits).hexdigest()
sha256 = hashlib.sha256(convertBits).digest()
sha256B64 = codecs.encode(hashlib.sha256(convertBits).digest(), 'base64')


print("El resultado en hexadecimal es: \n")
print(sha256Hex)
print("El resultado en sha256 es: \n")
print(sha256)
print("El resultado en sha256 en base 64 es: \n")
print(sha256B64)

# Sha512 en hex, bin y base64

sha512Hex = hashlib.sha512(convertBits).hexdigest()
sha512 = hashlib.sha512(convertBits).digest()
sha512B64 = codecs.encode(hashlib.sha512(convertBits).digest(), 'base64')


print("El resultado en sha512 en hexadecimal es: \n")
print(sha512Hex)
print("El resultado en sha512 es: \n")
print(sha512)
print("El resultado en sha512 en base 64 es: \n")
print(sha512B64)


# Blake2b

blake2b_size = hashlib.blake2b(digest_size=20)
blake2b_size.update(convertBits)
blake2bHexadecimal = blake2b_size.hexdigest()
blake2b = blake2b_size.digest()
blake2bB64 = codecs.encode(blake2b, 'base64')
print("El resultado en blake2b es: \n")
print(blake2b)
print("El resultado en blake2b con tamano de 20 es: \n")
print(blake2bHexadecimal)
print("El resultado de blake2b en base64 es: \n")
print(blake2bB64)


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


# PARTE 3
# La parte 3 se realizo con hmac, y este no requeria de un salt aleatorio

def register(user, password):
    try:
        file = open("db.txt", "a+")
        m = hmac.new(password, digestmod=hashlib.blake2b)
        m.update(user)
        result = m.hexdigest()
        file.write(user.decode("utf-8")+" " +
                   password.decode("utf-8")+" "+result+"\n")

        file.close()
    except OSError:
        print("Could not open/read file:")


def login(user, password):
    try:

        m = hmac.new(password, digestmod=hashlib.blake2b)
        m.update(user)
        result = m.hexdigest()
        with open("db.txt") as temp_f:
            if result in temp_f.read():
                print("Bienvenido "+user.decode("utf-8"))
            else:
                print("El usuario ingresado no existe")

    except OSError:
        print("Could not open/read file:")


print("Bienido a laboratorio 2")
print("Que desea realizar el dia de hoy")
print("1.Registrarse\n2.Iniciar sesion")

op = input("")

if(op == "1"):

    user = input("ingrese el usuario:\n")
    user = bytes(user, 'utf-8')
    password = input("ingrese la clave:\n")
    password = bytes(password, 'utf-8')
    register(user, password)
if (op == "2"):

    user = input("ingrese el usuario:\n")
    user = bytes(user, 'utf-8')
    password = input("ingrese la clave:\n")
    password = bytes(password, 'utf-8')

    login(user, password)
