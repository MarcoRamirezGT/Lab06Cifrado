import hashlib
import hmac
import codecs

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
