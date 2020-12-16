"""
Yuri Armando
Telefono senza fili 
"""
import socket
def client(msgClient):
    msgPerClient = str(input("Scrivi la parola: "))
    bytesSend = str.encode(msgClient)
    porta = ("192.168.1.146", 4500)
    bufferSize = 1024

    #Creazione del Socket Client 
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketClient.sendto(bytesSend, porta)

def server():
    ip = "192.168.1.146"
    porta = 4500
    bufferSize = 1024
    #Creazione del Socket Server  
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketServer.bind((ip, porta))
    print("SERVER IN ATTESA....")

    #Fase di Ascolto 
    datiSocket = socketServer.recvfrom(bufferSize)
    #recvfrom => istruzione bloccante 
    msgC = datiSocket[0]
    address = datiSocket[1]
    msgClient = "Parola: {}".format(str(msgC,'utf-8'))
    ipClient = "Client: {}".format(address)
    
    print("[" + ipClient + "]" + " " + msgClient)
    return msgClient

def main(): 
    msgClient = server()
    client(msgClient)

if __name__ == "__main__":
    main()