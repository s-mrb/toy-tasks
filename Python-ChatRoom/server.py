from threading import *
from socket import *


connections = {'clients':{}, 'IP':{}}

SOCK = socket(AF_INET, SOCK_STREAM)
SOCK.bind(("127.0.0.1",55552))
BUFFER_SIZE = 64000

def receive_client():
    while True:
        sock, ip = SOCK.accept()
        print("{} connected!".format(ip))
        sock.send(bytes("\nWelcome to ChatRoom, enter -1 to quit","utf8"))
        connections[sock] = ip
        Thread(target=handle_client, args=(sock, ip)).start()



def handle_client(sock, ip):
    sock.send(bytes("\nPlease enter your name","utf8"))
    name = sock.recv(BUFFER_SIZE).decode("utf8")
    message = "%s has joined the chat!\n" % (name)
    broadcast(bytes(message,"utf8"),name)
    connections["clients"][sock] = name

    while True:
        message = sock.recv(BUFFER_SIZE)
        if message != bytes("-1", "utf8"):
            broadcast(message,name+" : ")
        else:
            sock.send(bytes("-1","utf8"))
            sock.close()
            del connections["clients"][sock]
            broadcast(bytes("%s has left chat!"%name,"utf8"),name)
            break



def broadcast(message, name):
    for sock in connections["clients"]:
        sock.send(bytes(name,"utf8")+message)



SOCK.listen(10)  # Listens for 5 connections at max.
print("Server ran successfully!!")
ACCEPT_THREAD = Thread(target=receive_client)
ACCEPT_THREAD.start()  # Starts the infinite loop.
ACCEPT_THREAD.join()
SOCK.close()
