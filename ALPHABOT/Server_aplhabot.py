#YURI ARMANDO 5^AROB
from logging import DEBUG
import socket as sock
import sqlite3
from sqlite3.dbapi2 import Cursor
import threading
import logging
import tkinter as tk

ip_serv = "192.168.1.146"
port_serv = 4500

logging.basicConfig(level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s') 

class alphabot_handle(threading.Thread):
    def __init__(self, connection, address ):
        threading.Thread.__init__(self)
        self.conn_tunnel = connection
        self.add = address


        return

    def run(self):
        self.alphabot_revice()


    def alphabot_revice(self):

        logging.info(f"Connessione stabilita {self.add} ")
        self.choice = self.conn_tunnel.recv(1024).decode()
        self.choice = self.choice.split(",")

        logging.info(f"Il messaggio ricevuto è : start" [{self.choice[1]}], stop [{self.choice[0]}])
        try:
            self.connection = sqlite3.connect("percorsi.db")
        except:
            logging.error(" Non connesso al db ")
            
        self.query_creating()
        return 

    def query_creating(self):

        cursor = self.connection.cursor()
        print("SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (SELECT id_start FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_start AND luoghi.nome = '{self.choice[1]}') = inizio_fine.id_start AND(SELECT id_end FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_end AND luoghi.nome = '{self.choice[0]}') = inizio_fine.id_end")
        cursor.execute(f"SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (SELECT id_start FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_start AND luoghi.nome = '{self.choice[1]}') = inizio_fine.id_start AND(SELECT id_end FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_end AND luoghi.nome = '{self.choice[0]}') = inizio_fine.id_end" )
        try:
            self.path = cursor.fetchone()
            if self.path != None:
                logging.info(f"Percorso : {self.path[0]}")
                self.connection.close()
            else:   
                logging.error("Percorso non trovato")
        except:
            logging.exception("Errore")
            
    def alphabot_sender(self):

        self.conn_tunnel.sendall(self.path[0].encode())

def main():
    try:
        serv = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        serv.bind((ip_serv, port_serv))
        serv.listen()
        while True:
            conn, add = serv.accept()
            alphabot = alphabot_handle(conn, add)
            alphabot.start()

    except:
        logging.error("Server non disponibile")

if __name__ == "__main__":
    main()