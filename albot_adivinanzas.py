import albot_consts
from albot_auxiliares import imprimir_mensaje
from albot_auxiliares import loading
import random
import time

def adivinar(nombre_usuario):

    imprimir_mensaje("\n>>Genial! Juguemos a las adivinanzas")
    loading()
    
    juego_nuevo = True
    while (juego_nuevo):
        iniciar_partida(nombre_usuario)
        imprimir_mensaje("\n>>Gran partida!\nSi querés jugar de nuevo, apreta 'Y'. Sino, apretá cualquier tecla.")
        juego_nuevo = (input("\n>>").upper() == 'Y')

    imprimir_mensaje("\n>>Para volver al menú anterior, apretá 'M'. Para salir, apretá cualquier tecla.")
    salir = (input("\n>>").upper() != 'M')

    return salir
    

def iniciar_partida(nombre_usuario):

    puntajes = crear_tabla_puntajes(nombre_usuario)
    for i in range(5):
        print(f"\nRONDA NÚMERO {i+1}")
        albot_adivina(puntajes,nombre_usuario)
        imprimir_puntaje(nombre_usuario,puntajes)

    if puntajes["albot"] > puntajes[nombre_usuario]:
        imprimir_mensaje("Parece que te gané.")
        imprimir_bandera_victoria()
    else:
        imprimir_mensaje("Uf, me destrozaste.")
        imprimir_bandera_blanca()


def albot_adivina(puntajes,nombre_usuario):

    
    imprimir_mensaje(f"\n>>Voy a elegir un número del 0 al {albot_consts.MAX_ADIVINAR}. Vos tenés que tratar de adivinarlo.")
    numero = random.randrange(1,albot_consts.MAX_ADIVINAR+1)
    max_cant_intentos = albot_consts.MAX_ADIVINAR // 5
    imprimir_mensaje(f"Tenés {max_cant_intentos} intentos. Empecemos!")
    
    cant_intentos = 0

    intento = obtener_intento()
    while (not adivina_numero(numero,intento)):
        cant_intentos+=1
        imprimir_mensaje("\n>>" + random.choice(albot_consts.NO_ADIVINA))
        
        if cant_intentos == max_cant_intentos :
            break
        dar_pista(intento,numero)
        intento = obtener_intento()
        
    
    if cant_intentos == max_cant_intentos:
        imprimir_mensaje("Te quedaste sin intentos!")
        imprimir_mensaje(f"El número era {numero}.")
        sumar_punto(puntajes,"albot")
    else:
        imprimir_mensaje("\n>>Adivinaste!")
        sumar_punto(puntajes,nombre_usuario)


def crear_tabla_puntajes(nombre_usuario):
    tabla = {}
    tabla["albot"] = 0
    tabla[nombre_usuario] = 0
    return tabla

def obtener_intento():
    intento = input(">>")
    
    while not intento or not intento.isdigit():
        imprimir_mensaje("\n>>" + random.choice(albot_consts.NO_RESPONSE) + "¿Estás seguro/a que es un número?")
        intento = input("\n>>")
    
    return intento

def adivina_numero(numero,intento):
    return numero == int(intento)

def dar_pista(intento,numero):
    diferencia = int(intento) - int(numero)
    if diferencia > 0 :
        imprimir_mensaje(f"El número a adivinar es menor que {intento}.")
    else:
        imprimir_mensaje(f"El número es mayor que {intento}.")

def imprimir_puntaje(nombre_usuario, puntajes):

    puntos_albot = puntajes["albot"]
    puntos_usuario = puntajes[nombre_usuario]
    print(f"\n>> Albot: {puntos_albot} || {nombre_usuario}: {puntos_usuario}")


def sumar_punto(puntaje, ganador):


    puntaje[ganador] +=1


def imprimir_bandera_blanca():
    time.sleep(0.5)
    print("\nOO_____________\n||             |\n||   ME RINDO  |\n||_____________|\n||\n||\n||\n||\n||\n__________________\n")


def imprimir_bandera_victoria():
    time.sleep(0.5)
    print("\nOO_____________\n||    ALBOT    |\n||    ES EL    |\n||____MEJOR____|\n||\n||\n||\n||\n||\n__________________\n")

