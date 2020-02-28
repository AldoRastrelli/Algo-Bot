import string
VACIO = "."
ABC = string.ascii_lowercase

# MODIFICABLES:
DIM_HORIZONTAL = 4
DIM_VERTICAL = 4
FLAG = 'F'
LOOK = 'X'
MINAS = 3
MENSAJE_HELP = f"\nCOMANDOS\n-Con el caracter {FLAG} se indica que se desea colocar o quitar una bandera.\n-Con el caracter {LOOK} se descubre una posición.\n-Con las letras del abecedario (a,b,c..) se indican las filas.\n-Con los números naturales se indican las columnas (1,2,3..).\n"
MENSAJE_INPUT = f"\nIngresar la acción deseada y la fila y la columna a seleccionar, separado con guiones (por ej, {FLAG}-B-3 coloca o quita una bandera en B3). Inserte H para ver los comandos nuevamente: "
