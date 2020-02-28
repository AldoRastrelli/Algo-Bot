import random
import albot_consts
import albot_buscaminas
import albot_intercambio
from albot_auxiliares import imprimir_mensaje
MAX_INTENTOS = 3

def main():

    imprimir_mensaje(">>Hola! Soy Algo Bot, me dicen Albot.\n¿Cómo es tu nombre?")
    nombre = input(">>")
    intentos = 1
    while (not nombre):

        if intentos == MAX_INTENTOS:
            nombre = random.choice(albot_consts.NAMES)
            imprimir_mensaje(f"\n>>Bueno, te voy a llamar {nombre}.")
            break

        imprimir_mensaje("\n>> " + random.choice(albot_consts.NO_RESPONSE) + " ¿Cómo es tu nombre?")
        nombre = input(">>")

        intentos+=1;
    
    
    albot_intercambio.iniciar_intercambio(nombre)

    imprimir_mensaje(f">>Volvé a visitarme pronto, {nombre}! Nos vemos!")

main()