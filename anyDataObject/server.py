import socket
import time
import pickle 





HEADERSIZE = 10

# ipv4 , tcp
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),2644))
s.listen(5)

while True:
	clientsocket , address = s.accept()
	print (f"Connection from {address} has been established!")

	d = {1:"hey",2: "There"}
	msg = pickle.dumps(d)
	msg= bytes (f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg 
	clientsocket.send(msg)

	# msg = "Welcome to the server!"
	# msg = f'{len(msg):<{HEADERSIZE}}'+ msg

	# clientsocket.send(bytes(msg,"utf-8"))

	# while True:
	# 	time.sleep(3)
	# 	#time = f"the time is ! {time.time()}"
	# 	d = {1:"hey",2: "There"}
	# 	msg = pickle.dumps(d)
	# 	msg= bytes (f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg 
	# 	clientsocket.send(msg)
		
	