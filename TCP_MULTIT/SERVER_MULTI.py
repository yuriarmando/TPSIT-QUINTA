#YURI ARMANDO 5^ROB
import socket
import threading

ip = "XXX.XXX.X.XXX" #192.168.1.146
port = 4500

connection_table = {}
threadattivi = []

class ClietThread(threading.Thread):
    #COSTRUTTORE
    def __init__(self,ip,port,connection): 
        threading.Thread.__init__(self)

        self.ip_address = ip
        self.port = port
        self.connection = connection
        self.again = 1


    def run(self): 
        while self.again:
            msg = self.connection.recv(4096)
            msg = msg.decode()
            print(f"{ip},{port} ha scritto : {msg}")
            self.connection.sendall(msg.encode())

            if msg == "exit":
                self.again = 0

def close_thread(t):
    if t in threadattivi:
        threadattivi[threadattivi.index(t)].join()
        threadattivi.pop(threadattivi.index(t))
        

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((ip,port))

    while True:
        s.listen()
        print("SERVER IN ATTESA\n")
        conn, add = s.accept()
        print("NUOVA UTENZA CONNESSA\n")
        t = ClietThread(add[0],add[1],conn)
        t.start()
        threadattivi.append(t)
        connection_table[conn] = add

if __name__ == "__main__":
    server()