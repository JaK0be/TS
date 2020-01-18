from socket import *
import sys
import os

def main():
	code = sys.argv[1]
	s = socket(AF_INET,SOCK_DGRAM)
	host = "127.0.0.1"
	port = 9999
	buf = 1024
	addr = (host,port)
	print(code)
	s.sendto(code.encode(),addr)
	s.close()

if __name__ == "__main__":
	main()