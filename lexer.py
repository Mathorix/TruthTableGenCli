import re
from typing import Iterator, Tuple

TOKEN_SPECS = [
    ('IFF',     r'<->'),
    ('IMPLIES', r'->'),
    ('OR',      r'\|'),
    ('AND',     r'&'),
    ('NOT',     r'~'),
    ('LPAREN',  r'\('),
    ('RPAREN',  r'\)'),
    ('VAR',     r'[A-Za-z][A-Za-z0-9_]*'),
    ('SKIP',    r'[ \t]+'),
    ('MISMATCH',r'.'),
]

def lex(code: str) -> Iterator[Tuple[str, str]]:
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECS)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        if kind == 'MISMATCH':
            raise ValueError(f'Unexpected char: {value}')
        yield kind, value