import sys
import minas
import matriz
import cons

def traducir_fila_columna(posicion):
    "traduce la fila y la columna en la matriz a partir de la posicion ingresada por el usuario"

    return cons.ABC.index(posicion[0])+1, posicion[1]

def colocar_quitar_bandera(M,posicion):
    "coloca o quita una bandera en la posicion"
    fila, columna = traducir_fila_columna(posicion)
    posicion_matriz = M[fila][columna]

    if posicion_matriz == cons.VACIO:
        M[fila][columna] = cons.FLAG
    elif posicion_matriz != cons.FLAG:
        return M
    else: # la posicion contiene una bandera
        M[fila][columna] = cons.VACIO
    return M

def look(M,posicion,mapa_minas):
    "devela el contenido de la posición: mina o cantidad de minas limítrofes"
    fila, columna = traducir_fila_columna(posicion)
    posicion_matriz = M[fila][columna]

    if posicion_matriz == cons.FLAG:
        print("\n>Se debe quitar una bandera antes de poder develar una posición<")
    elif minas.contiene_mina(posicion,mapa_minas):
            minas.agregar_minas_en_tablero(M,mapa_minas)
            print('\nPerdiste :(\n*FIN DEL JUEGO*')
            return None
    else: 
        M[fila][columna] = minas.minas_limitrofes(posicion,mapa_minas)
    return M

        