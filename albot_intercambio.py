import albot_adivinanzas
from albot_auxiliares import imprimir_mensaje
import albot_consts
import albot_buscaminas
import buscaminas_main
import random
import time
import albot_pictionary
from datetime import date
from dateutil.relativedelta import relativedelta


def iniciar_intercambio(nombre_usuario):
    imprimir_mensaje(f"Hola, {nombre_usuario}. Te voy a contar un poco más de mí.")
    
    edad_albot = int(relativedelta(date.today(), albot_consts.NACIMIENTO_ALBOT).years)
    imprimir_mensaje(f"Tengo {edad_albot} años. Me crearon el 24 de febrero de 2020.\nSoy un programa hecho en Python y en constante modificación.")
    imprimir_mensaje("¿Cuál es tu edad?")
    edad = input(">>")
    while (not edad.isdigit()):
        imprimir_mensaje("\n>>Hmm.. Es no es un número. ¿Me lo podrías escribir con cifras?")
        time.sleep(1)
        imprimir_mensaje(f"Por ejemplo, yo tengo {edad_albot} años. Entonces cuando me preguntes cuántos años tengo, yo voy a decir '{edad_albot}'.")
        edad = input(">>")
    
    comentar_edad(int(edad),edad_albot)

    salir = False
    while (not salir):
        imprimir_mensaje(f"\nBueno, {nombre_usuario}: qué te gustaría hacer?")
        respuesta = imprimir_mensaje_opciones()
        while (respuesta not in ["A","B","C","D"]):
            imprimir_mensaje(random.choice(albot_consts.NO_RESPONSE))
            respuesta = imprimir_mensaje_opciones()
    
        if respuesta == "A":
            salir = albot_buscaminas.buscaminas()
        elif respuesta == "B":
            salir = albot_adivinanzas.adivinar(nombre_usuario)
        elif respuesta == "C":
            salir = albot_pictionary.pictionary(nombre_usuario)
        elif respuesta == "D":
            return
    

def imprimir_mensaje_opciones():
    respuesta = input("A) Jugar al buscaminas.\nB) Jugar a las adivinanzas.\nC) Jugar al Pictionary \nD) Despedirme.\n>>").upper()
    return respuesta

def comentar_edad(edad_usuario, edad_algobot):

    relacion = ""
    if (edad_algobot < edad_usuario):
        relacion = "grande"
    else:
        relacion = "joven"

    imprimir_mensaje(f"Wow! Nos llevamos {edad_usuario-edad_algobot} años! Sos más {relacion} que yo.")

