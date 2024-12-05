import socket 
from threading import Thread 


def Sending(s):
    while True : 
        msg = input()
        s.send(bytes(msg,"utf-8"))
def Receving(s):
    while True : 
        msg=s.recv(500)
        print(msg.decode("utf-8"))
SOCKET=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SOCKET.connect(("192.168.1.4",1234))

while True :
    Thread_1=Thread(target=Sending,args=(SOCKET, ))
    Thread_2=Thread(target=Receving,args=(SOCKET, ))
    Thread_1.start()
    Thread_2.start()

