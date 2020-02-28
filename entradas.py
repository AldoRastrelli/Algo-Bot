import matriz
import cons

def imprimir_comandos():
    "imprime los comandos del juego"
    
    print(f'{cons.MENSAJE_HELP}')

def recibir_entrada(M):
    "recibe la entrada del usuario: acción, fila y columna" 

    while True:
        
        matriz.imprimir_tablero(M)
        entrada = str(input(f"{cons.MENSAJE_INPUT}").lower())
        
        if entrada == 'h':
            imprimir_comandos()
        elif validar_entrada(entrada):
            break
    
    lista_de_entradas = entrada.split('-')

    return lista_de_entradas[0], (lista_de_entradas[1],int(lista_de_entradas[2]))
# lista_de_entradas[0] es la acción y (lista_de_entradas[1],lista_de_entradas[2]) es tupla de las coordenadas de la ubicación
    
def validar_entrada(entrada):
    """Valida que la posicion esté dentro del tablero y que la acción
  corresponda a las indicaciones dadas (que sea F o X)"""
    
    if '-' not in entrada:
        print("\n>El formato de entrada no es válido<\n")
        return False
    
    lista_de_entradas = entrada.split("-")
    if not (lista_de_entradas[0] == cons.FLAG.lower() or lista_de_entradas[0] == cons.LOOK.lower()):
        print("\n>La acción ingresada no es válida<\n")
    elif not (str(lista_de_entradas[1]) in cons.ABC[:cons.DIM_VERTICAL] and (1 <= int(lista_de_entradas[2]) <= cons.DIM_HORIZONTAL)):
        #verifica que la fila esté entre mis letras usadas en el margen izquierdo
        #verifica que la columna esté entre mi rango usado en el margen superior
        print("\n>La posición ingresada no está dentro de los límites del tablero<\n")
    else:
        return True
    return False
 