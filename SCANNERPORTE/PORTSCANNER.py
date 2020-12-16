import socket

def main():
  
    portelibere = []
  
    
    ip = "XXX.XXX.X.XXX"	#192.168.1.146
  
    for port in range(8000,65536):
        print(f"port = {port}")
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
        res = c.connect_ex((ip,port))
        if  res == 0: #SE RESTITUISCE 0 LA PORTA E' DISPONIBILE
            print(f"PORTA LIBERA :{port}")
            portelibere.append(port)
        c.close()
    print(portelibere)
if __name__ == "__main__":
    main()