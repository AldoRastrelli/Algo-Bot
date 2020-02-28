import matriz
import minas
import flags_or_look
import entradas
import cons
import sys

def buscaminas_main():

    mapa_minas = minas.ubicar_minas() # ubica las minas en lugares random del tablero
    M = matriz.crear_matriz() # Crea una matriz vacía y numerada en los márgenes
    
    print('\n*BUSCAMINAS*\n')
    entradas.imprimir_comandos()
    print(f'Cantidad de minas: {cons.MINAS}\n')
    while not matriz.es_matriz_ganadora(M,mapa_minas):
        accion, posicion = entradas.recibir_entrada(M)
        if accion == cons.FLAG.lower():
            M = flags_or_look.colocar_quitar_bandera(M,posicion)
        elif accion == cons.LOOK.lower():
            M = flags_or_look.look(M,posicion,mapa_minas)
            if (not M): return
         
    minas.agregar_minas_en_tablero(M,mapa_minas)
    print('\n¡FELICIDADES! FIN DEL JUEGO')

