import sys
from impl_lexico import *
from analisis import *

if __name__ == '__main__':
    file_name = sys.argv[1]
    file = open(file_name)
    contenido = file.read()
    file.close()
    tokens = imp_lex(contenido)
    validar_bloques(tokens)
    clase = validar_clase(tokens)


