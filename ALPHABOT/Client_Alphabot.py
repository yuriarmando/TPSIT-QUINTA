#YURI ARMANDO 5^ROB
import socket as sock
import turtle
import logging
import time
import re

server_ip = "XXX.XXX.X.XXX"
server_port = 4500
full_address = (server_ip, server_port)

# CREAZIONE SOCKET
def set_socket():
    client = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    client.connect(full_address)
    
    client.recv()

    return client

def inputdati_send(client): #RICHIESTA PERCORSO
    print("INSERIRE DATI PERCORSO")
    inputdati = input(':')

    try:
        logging.debug(inputdati)
        # MANDA LA RICHIESTA AL SERVER
        client.sendall(inputdati.encode())
    except:
        logging.exception("ERRORE")

def receiving_path(client): 
    #RICEZIONE DATI DAL SERVER 
    try:
        risultato = client.recv(1024)
        risultato = risultato.decode()
        risultato = risultato[1]
        print(risultato)

    except:
        logging.exception("ERRORE")

    return risultato



def risultato_check(risultato):

    if re.findall("^0", risultato):
        #ECCEZIONI SERVER
        logging.debug(risultato)
    else:
        semi_path = re.split('R|L|F|B', risultato) 
        path = {} 
        for elements in semi_path:
            tempo_path = re.split("[0-9]",semi_path)
            path.update({tempo_path[0]: tempo_path[1]})
        
        return path
        
"""
def turtle_draw(commands):
    
    alphabot = turtle.Turtle()

    

    return"""


def main():

    client = set_socket()
    inputdati_send(client)
    
    risultato = receiving_path(client)

    commands = risultato_check(risultato)

    turtle_draw(commands)



    return

if __name__ == "__main__":
    main()