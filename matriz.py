import cons
import minas


def crear_matriz():
    "Crea una matriz vacía"

    M = [[cons.VACIO for _ in range(cons.DIM_HORIZONTAL+1)]for _ in range(cons.DIM_VERTICAL+1)]
    list(cons.ABC)
    M[0][0] = " "
    for i in range(1,cons.DIM_HORIZONTAL+1):
        M[0][i] = i
    for i in range (1,cons.DIM_VERTICAL+1):
        M[i][0] = cons.ABC[i-1]
    return M

#M = crear_matriz()
#Hasta acá: Matriz Blanqueada.
#Márgenes superior e izquierdo numerado (num y letras respectivamente).

def imprimir_tablero(M):
    "imprime la matriz en forma de tablero"
    
    
    for i in range(cons.DIM_VERTICAL+1):
        lista = []
        for j in range(cons.DIM_HORIZONTAL+1):
            lista.append(str(M[i][j]))
        print(" | ".join(lista))

def es_matriz_ganadora(M,mapa_minas):
    """indica si todas las ubicaciones de la matriz
    han sido descubiertas exceptuando aquellas que contienen mina"""

    for i in range(1,cons.DIM_VERTICAL+1):
        for j in range(1,cons.DIM_HORIZONTAL+1):
            if M[i][j] == cons.VACIO and not (cons.ABC[i-1],j) in mapa_minas:
                return False
            elif M[i][j] == cons.FLAG and (cons.ABC[i-1],j) in mapa_minas:
                continue
    return True
                
