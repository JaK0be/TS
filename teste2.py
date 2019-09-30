import os
import getpass
import base64
import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


def cifra():
	name = sys.argv[1] #Nome do ficheiro
	file = open(name,"rb")
	fc = open("ficheirocifrado.txt","wb")
	password = getpass.getpass()
	passwordBytes = password.encode()
	backend = default_backend()
	salt = os.urandom(16)
	kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations=100000,
	    backend=backend
	)
	key = kdf.derive(passwordBytes)
	#converter para base 64
	k = base64.b64encode(key)
	print(k)
	f = Fernet(k)
	conteudo = file.read(1024)
	token = f.encrypt(conteudo)
	print(token)
	fc.write(token)

def decifra():
	file = open("ficheirocifrado.txt","rb") #ficheiro cifrado
	fc = open("decifrado.txt","wb")
	password = getpass.getpass()
	passwordBytes = password.encode()
	backend = default_backend()
	salt = os.urandom(16)
	kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations=100000,
	    backend=backend
	)
	key = kdf.derive(passwordBytes)
	k = base64.b64encode(key)
	print(k)
	print("\n")
	f = Fernet(k)
	token = file.read(1024)
	print(token)
	#fc.write(f.decrypt(token))
	#kdf.verify(passwordBytes, key)
	#print("Tudo correu bem")

#kdf.verify(b"my great password", key)

cifra()
decifra()