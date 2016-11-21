import sys
import re

def lex(contenido, token_exprs):
    pos = 0
    tokens = []
    while pos < len(contenido):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(contenido, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Caracter desconocido: %s\n' % contenido[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens