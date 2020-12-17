import turtle
import re

def esegui_percorso(percorso,t):
    lista_valori = re.split(r"\D", percorso)
    lista_valori.pop(0)
    print(f"VALORI PRESENTI: {lista_valori}")

    #for l in range (0,len(lista_valori)):
    #    lista_valori[l] = int(lista_valori[l])
    
    lista_valori = [int(lista_valori[l]) for l in range(0,len(lista_valori))]

    #MOVIMENTO
    direzioni = re.split(r"\d", percorso)

    for a in range (0,2):
        c = 0
        for a in direzioni:
            if a == '':
                direzioni.pop(c)
            
            c = c + 1
    print(f"lista direzioni : {direzioni}")

    print(t.pos())
    #cont = 0

    for a,val in zip(direzioni,lista_valori):
        if a == 'L':
            t.left(val)
        elif a == 'F':
            t.forward(val)
        elif a == 'B':
            t.backward(val)
        elif a == 'R':
            t.right(val)
        #cont = cont + 1
