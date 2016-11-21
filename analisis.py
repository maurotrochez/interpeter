import sys
from error import *


class Conversion:
    pass


def validar_bloques(tokens):
    cont = 0
    for lex, token in tokens:
        if lex == 'begin':
            cont += 1
        elif lex == 'end':
            cont -= 1
    if cont == 0:
        return True
    else:
        sys.stderr.write('Bloque incompleto (falta un begin o un end)')
        sys.exit(1)


def validar_clase(tokens):
    pos = 0
    while pos <= len(tokens):
        lex, token = tokens[pos]
        id = tokens[pos+1][1]
        begin = tokens[pos+2][0]
        print(lex, id, begin)
        if lex == 'class':
            if id == 'ID':
                if begin == 'begin':
                    return "{lex} {id} {begin} \n\t".format(lex=lex, id=id, begin=':')
        error('Error en estructura de clase')


def expresiones(tokens):
    tokens = tokens[3:]
    st = stament(tokens)


def stament(tokens):
    str = ''
    for lex, token in tokens:
        if token == 'RESERVADO':
            str += '' if tipo_var(lex) else lex
        if token == 'ID':
            str += lex
        if lex == ';':
            str += "\n"
    print(str)


def tipo_var(str):
    variables = ('int', 'decimal', 'char', 'string', 'boolean')
    return any(v for v in variables if v == str)





