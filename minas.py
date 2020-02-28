from random import randint
from random import choice
import cons
import matriz

def ubicar_minas():
    "Ubica las minas en lugares random del tablero"
    
    mapa_minas = []
    cont = 0
   
    while cont < cons.MINAS:
        
        tupla = choice(cons.ABC[:cons.DIM_VERTICAL]),randint(1,cons.DIM_HORIZONTAL)
        if not tupla in mapa_minas: #evita que se repitan las ubicaciones
            mapa_minas.append(tupla)
            cont +=1
        
    return mapa_minas

def contiene_mina(posicion,mapa_minas):
    "indica si la ubicación elegida por el usuario contiene o no una mina"

    return posicion in mapa_minas

def minas_limitrofes(posicion,mapa_minas):
    "indica para la ubicación elegida cuántas minas tiene cerca"

    y = cons.ABC.index(posicion[0])+1 #pasa a número la fila elegida alfabeticamente
    x = posicion[1]
    minas_cercanas = 0 

    for i in range(y-1,y+2): #i pertenece a [y-1, y+1]
        for j in range(x-1,x+2): #j pertenece a [x-1,x+1]
            """Sé que tamb verifica mi posicion actual pero considero que,
            sabiendo que está vacia, es mejor que la verifique igual a extender mi código 
            tratando de que no la verifique, cuando en sí no me cambia nada"""
            borde = cons.ABC[i-1],j
            
            if contiene_mina(borde,mapa_minas):
                minas_cercanas +=1
            
    return minas_cercanas

def agregar_minas_en_tablero(M,mapa_minas):
    "devuelve la matriz con las minas agregadas en sus respectivas posiciones"

    for mina in mapa_minas:
        M[cons.ABC.index(mina[0])+1][mina[1]] = "M"
    matriz.imprimir_tablero(M)
