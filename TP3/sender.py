from socket import *
import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def main():
	code = sys.argv[1]

	#AES-Counter Mode
	backend = default_backend()
	key = b"\n\xa2T\x8b\x14\xc4\xe5['\x10I\x07\xff\x05\xda\xae\xe4\n9\x92 \x01\x95\x1a\xceL\x19\x9dS\xa1\xb0)"
	iv = b'\xd6\xd1\xbc\xde\rWq\x9e\x9cF\xd3\xf8\xc6U\x0f\xbc'
	cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)
	encryptor = cipher.encryptor()
	ct = encryptor.update(code.encode()) + encryptor.finalize()

	s = socket(AF_INET,SOCK_DGRAM)
	host = "127.0.0.1"
	port = 9999
	buf = 1024
	addr = (host,port)
	s.sendto(ct,addr)
	s.close()

if __name__ == "__main__":
	main()
