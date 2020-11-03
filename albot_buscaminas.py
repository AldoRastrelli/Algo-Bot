import random
import buscaminas_main
from albot_auxiliares import imprimir_mensaje
from albot_auxiliares import loading

def buscaminas():
    imprimir_mensaje("\n>>Excelente! Qué empiece el juego...")

    juego_nuevo = True

    while (juego_nuevo):
        loading()
        buscaminas_main.buscaminas_main()
        imprimir_mensaje("\n>>Gran partida!\nSi querés jugar de nuevo, apreta 'Y'. Sino, apretá cualquier tecla.")
        juego_nuevo = (input("\n>>").upper() == 'Y')

    imprimir_mensaje("\n>>Para volver al menú anterior, apretá 'M'. Para salir, apretá cualquier tecla.")
    salir = (input("\n>>").upper() != 'M')

    return salir