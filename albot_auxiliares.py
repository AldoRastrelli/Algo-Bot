TIEMPO_RSTA_TEXTO = 0.15 # Segundos
TIEMPO_RSTA_IMAGEN = 0.1 # Segundos
SEP_TEXTO = ' '
UNIF_TEXTO = ' '
SEP_IMAGEN = '\n'
UNIF_IMAGEN = '\n'

import time

def imprimir_mensaje(string):
    
    imprimir_secuencia(string,SEP_TEXTO,UNIF_TEXTO,TIEMPO_RSTA_TEXTO)

def imprimir_imagen(string):

    imprimir_secuencia(string,SEP_IMAGEN,UNIF_IMAGEN,TIEMPO_RSTA_IMAGEN)

def imprimir_secuencia(string,separador, unificador,tiempo):
    
    palabras = string.split(separador)
    for i in range(len(palabras)):
        if i == len(palabras)-1 :
            unificador = "\n"

        print(palabras[i], end = unificador, flush = True)
        time.sleep(tiempo)

def loading():
    imprimir_mensaje("L O A D I N G . . .")