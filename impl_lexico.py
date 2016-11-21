import lexico

RESERVADO = 'RESERVADO'
ASIGNACION = 'ASIGNACION'
OPERADOR = 'OPERADOR'
COMPARADOR = 'COMPARADOR'
STRING = 'STRING'
INT = 'INT'
ID = 'ID'
TIPO_VAR = 'TIPO_VARIABLE'
INICIO_BLOQUE = 'INICIO_BLOQUE'
FIN_BLOQUE = 'FIN_BLOQUE'

token_exprs = [
    # Espacios en blanco
    (r'[ \n\t]+',              None),
    (r'\:=',                   ASIGNACION),
    (r'\(',                    RESERVADO),
    (r'\)',                    RESERVADO),
    (r';',                     RESERVADO),
    (r'\+',                    OPERADOR),
    (r'-',                     OPERADOR),
    (r'\*',                    OPERADOR),
    (r'/',                     OPERADOR),
    (r'%',                     OPERADOR),
    (r'<=',                    COMPARADOR),
    (r'<',                     COMPARADOR),
    (r'>=',                    COMPARADOR),
    (r'>',                     COMPARADOR),
    (r'not=',                  COMPARADOR),
    (r'=',                     OPERADOR),
    (r'and',                   RESERVADO),
    (r'or',                    RESERVADO),
    (r'not',                   RESERVADO),
    (r'if',                    RESERVADO),
    (r'begin',                 INICIO_BLOQUE),
    (r'else',                  RESERVADO),
    (r'for',                   RESERVADO),
    (r'end',                   FIN_BLOQUE),
    (r'main\(\)',              RESERVADO),
    (r'int',                   RESERVADO),
    (r'decimal',               RESERVADO),
    (r'char',                  RESERVADO),
    (r'string',                RESERVADO),
    (r'boolean',               RESERVADO),
    (r'void',                  RESERVADO),
    (r'class',                 RESERVADO),
    (r'in',                    RESERVADO),
    (r'out',                   RESERVADO),
    # Strings
    (r'"(.*?)"',               STRING),
    (r',',                     RESERVADO),
    (r'[0-9]+',                INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]

def imp_lex(contenido):
    return lexico.lex(contenido, token_exprs)
