import lexico

RESERVADO = 'RESERVADO'
ASIGNACION = 'ASIGNACION'
OPERADOR = 'OPERADOR'
COMPARADOR = 'COMPARADOR'
STRING = 'STRING'
INT = 'INT'
ID = 'ID'
TIPO_VAR = 'TIPO_VARIABLE'

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
    (r'begin',                 RESERVADO),
    (r'else',                  RESERVADO),
    (r'for',                   RESERVADO),
    (r'end',                   RESERVADO),
    (r'main\(\)',              RESERVADO),
    (r'int',                   RESERVADO),
    (r'decimal',               RESERVADO),
    (r'char',                  RESERVADO),
    (r'string',                RESERVADO),
    (r'boolean',               RESERVADO),
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
