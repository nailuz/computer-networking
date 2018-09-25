# -*- coding: utf-8 -*-
import rsa
import hashlib

# To generate keys
(public_key_one, private_key_one) = rsa.newkeys(128)
(public_key_two, private_key_two) = rsa.newkeys(128)

#Na chave publica temos N e E, que representam {N:O produto dos 2 numeros primos aleatorios; E: Um numero aleatorio inteiro que é primo entrei comparado ao produto de N}
#Na chave privada temos a chave publica, P, Q e D, que representam {P: Primeiro valor primo aleatorio; Q: Segundo valor primo aleatorio; D: Numero chave utilizado para agilisar a conta}

#Input message that you like
msg_inputed = input("Input your message: ")

# Turn message possible to be used in library rsa
msg = msg_inputed.encode('utf8')

# To generate encrypted and hashed message
msg_encrypted = rsa.encrypt(msg, public_key_one)
msg_hashed = hashlib.sha256(msg)

print("Message encrypted:", str(msg_encrypted))
print("Message hashed:", str(msg_hashed))

# Decrypting the message using it own private key
msg_decrypted = rsa.decrypt(msg_encrypted, private_key_one)
print("If you have de private key you can access. \nThis is the message:", str(msg_decrypted)[2:-1])

# Generate a hash by msg decrypted
msg_hashed_new = hashlib.sha256(msg_decrypted)

# if the first hash is equal the last hash it will work
if(msg_hashed.hexdigest() == msg_hashed_new.hexdigest()):
    print("The message is not modified")
else:
    print("The message is modified")