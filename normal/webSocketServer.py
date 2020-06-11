import socket
import time


HEADERSIZE = 10

# ipv4 , tcp
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),2643))
s.listen(5)

while True:
	clientsocket , address = s.accept()
	print (f"Connection from {address} has been established!")

	msg = "Welcome to the server!"
	msg = f'{len(msg):<{HEADERSIZE}}'+ msg

	clientsocket.send(bytes(msg,"utf-8"))

	while True:
		time.sleep(3)
		msg = f"the time is ! {time.time()}"
		msg= f'{len(msg):<{HEADERSIZE}}' + msg
		clientsocket.send(bytes(msg,"utf-8"))
		
	