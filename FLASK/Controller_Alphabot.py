
from flask import Flask, render_template, request, url_for
import logging
from time import sleep
# importing Alphabot form the Alphabot Class
#from Alphabot import AlphaBot

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')#IMPOSTAZIONI LOGGING

app = Flask(__name__)

@app.route('/') #CARICAMENTO DEL TEMPLATE
def index():
    return render_template('index.html')

#PROCEDURA AVANTI
@app.route('/avanti')
def forward():
    logging.debug('avanti')
    #ap.forward()
    sleep(1)
    return render_template('index.html')

#PROCEDURA INDIETRO
@app.route('/indietro')
def backward():
    logging.debug('indietro')
    #ap.backward()
    sleep(1)
    return render_template('index.html')

#PROCEDURA SINISTRA
@app.route('/sin')
def left():
    logging.debug('sinistra')
    #ap.left()
    sleep(1)
    return render_template('index.html')

#PROCEDURA DESTRA
@app.route('/destra')
def right():
    logging.debug('destra')
    #ap.right()
    sleep(1)
    return render_template('index.html')
  #MAIN
if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
