import sys
from error import *


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


def stament(list_tokens):
    try:
        str = ''
        stop = False
        i = 0
        while not stop:
            if len(list_tokens) == i:
                stop = False

            tokens = list_tokens[i]
            lex, token = tokens

            # Creacion de variables
            if token == 'RESERVADO':
                str, next, i = validar_asignacion(list_tokens, i, str)
                if next:
                    i += 1
                    continue
                else:
                    if lex == 'void':
                        bloque = extraer_bloque(list_tokens, i)
                        str += stament(bloque)

            elif token == 'ID':
                str += lex
            elif token == 'ASIGNACION':
                str += '='
            elif token == 'COMPARADOR':
                str += lex
            elif token == 'OPERADOR':
                str += lex
            else:
                str += lex
        return str

    except Exception as e:
        print(e)

def tipo_var(str):
    variables = ('int', 'decimal', 'char', 'string', 'boolean')
    return any(v for v in variables if v == str)


def validar_fin_de_linea(list_tokens, index, str):
    lex, token = list_tokens[index]
    if lex == ';':
        str += '\n'
        return str, True
    return str, False


def validar_asignacion(list_tokens, index, str):
    lex, token = list_tokens[index]
    if lex == 'void':
        return validar_metodo(list_tokens, index, str)
    index += 1
    if list_tokens[index][1] == 'ID':
        str += list_tokens[index][0] if tipo_var(lex) else lex + ' '
    index += 1
    if list_tokens[index][1] == 'RESERVADO':
        result = validar_fin_de_linea(list_tokens, index, str)
        if result[1]:
            str += ':=None'
            str += result[0]
            return str, True, index

def validar_metodo(list_tokens, index, str):
    index += 1
    if list_tokens[index][1] == 'RESERVADO' and list_tokens[index][0] == 'main()':
        main = 'if __name__ == \'__main__\':\n\t'
        index += 1
        bloque, index = extraer_bloque(list_tokens, index)
        str += main + stament(bloque)
    return str, False, index

def extraer_bloque(list_tokens, index):
    abre = 0
    cierra = 0
    lista_bloque = []
    index_final = 0
    for i, token in enumerate(list_tokens[index:]):
        lex, tok = token
        if abre != 0 and abre == cierra:
            index_final = i
            break
        if tok != 'INICIO_BLOQUE':
            lista_bloque.append(token)
        if tok == 'FIN_BLOQUE':
            cierra += 1
        if tok == 'INICIO_BLOQUE':
            abre += 1
    return lista_bloque, index_final+index





