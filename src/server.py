import socket, sys, threading, json

class Server:
    def __init__(self, serverAddress=9999):
        self.connections = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverAddress = serverAddress
        self.sock.bind(('localhost',self.serverAddress))
        #self.registerToNetwork()
        self.receiveThread = threading.Thread(target=self.receiveThreadFunction, name="Server")
        self.receiveThread.start()

    def receiveThreadFunction(self):
        while True:
            data, recvAddress = self.sock.recvfrom(4096)
            if(data.decode()=="register"):
                self.registerNewNode(recvAddress)
            else:
                self.broadcastMessage(data.decode(), recvAddress)

    def registerNewNode(self, connectionPort):
        self.connections.append(connectionPort)
        print(connectionPort, "is now registered")
        print(self.connections)
    
    def broadcastMessage(self, message, recvAddress):
        for connection in self.connections:
            
            if connection!=recvAddress:
                print("Chala")
                self.sock.sendto(bytearray(message, encoding ='utf-8'), connection)