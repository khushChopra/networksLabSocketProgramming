import socket, sys, threading, json

class Client:
    def __init__(self, myPort, myName, serverAddress=9999):
        self.myName = myName
        self.myPort = myPort
        self.connections = {}
        self.serverAddress = serverAddress
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost',self.myPort))
        #self.registerToNetwork()
        self.receiveThread = threading.Thread(target=self.receiveThreadFunction, name=self.myName)
        self.receiveThread.start()

    def receiveThreadFunction(self):
        while True:
            data, recvAddress = self.sock.recvfrom(4096)
            print("From -",recvAddress,", message ->", data)

    def sendMessage(self, connectionPort, message):
        self.sock.sendto(bytearray(message, encoding ='utf-8'),('localhost',connectionPort))
    
    def registerToServer(self):
        self.sock.sendto(bytearray("register", encoding ='utf-8'), ('localhost',self.serverAddress))
    
    def broadcastMessage(self, message):
        self.sock.sendto(bytearray(message, encoding ='utf-8'), ('localhost',self.serverAddress))