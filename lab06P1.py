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
