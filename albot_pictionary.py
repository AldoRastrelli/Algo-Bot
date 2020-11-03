from albot_auxiliares import imprimir_mensaje
from albot_auxiliares import imprimir_imagen
from albot_auxiliares import loading
import albot_consts
import albot_pictionary_imgs
import random

def pictionary(nombre_usuario):

    imprimir_mensaje("\n>>" + random.choice(albot_consts.OK) + " Juguemos al Pictionary.")
    loading()

    imprimir_mensaje("\n* P I C T I O N A R Y *")
    imprimir_mensaje("\n>> Yo voy a dibujar algo y, cuando termine, tenés que tratar de adivinarlo.\n Empecemos!")

    juego_nuevo = True
    imagenes = albot_pictionary_imgs.CLAVE
    dibujadas = set()

    while (juego_nuevo):
        adivino = jugar(imagenes,dibujadas)

        if adivino == None:
            return False
        
        if adivino:
            imprimir_mensaje(f"\n>>Adivinaste, {nombre_usuario}!")
        else:
            imprimir_mensaje(f"\n>>Mejor suerte la próxima, {nombre_usuario}.")

        imprimir_mensaje("\nGran partida!\nSi querés jugar de nuevo, apreta 'Y'. Sino, apretá cualquier tecla.")
        juego_nuevo = (input("\n>>").upper() == 'Y')

    imprimir_mensaje("\n>>Para volver al menú anterior, apretá 'M'. Para salir, apretá cualquier tecla.")
    salir = (input("\n>>").upper() != 'M')
    return salir

def jugar(imagenes,dibujadas):

    cant_intentos = 0
    imagen = random.choice(list(imagenes.keys()))
    
    while imagen in dibujadas:
        if len(dibujadas) == len(imagenes):
            imprimir_mensaje("Adivinaste todo!\nPor ahora no sé dibujar más cosas, nos vemos!")
            return None
        imagen = random.choice(list(imagenes.keys()))    
    
    dibujadas.add(imagen)
    imprimir_imagen(imagen)
    intento = (input("\n>>")).lower()
    cant_intentos = 1
    while (cant_intentos < 15):    
        if not imagenes[imagen] == intento:
            imprimir_mensaje("\n>>" + random.choice(albot_consts.NO_ADIVINA))
            if cant_intentos % 3 == 0:
                imprimir_mensaje("¿Te rendis? Si te querés rendir, apretá 0:")
            intento = input("\n>>")
            if intento == "0":
                imprimir_mensaje(f"La respuesta era {imagenes[imagen]}!")
                return False
            cant_intentos+=1
        else:
            break

    return cant_intentos < 15
