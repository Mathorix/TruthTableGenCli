import re
from typing import Iterator, Tuple, List

Token = Tuple[str, str]
TOKEN_SPECS: List[Token] = [
    ("SKIP", r"[ \t]+"),
    ("TURNSTILE", r"\|-"),
    ("IFF", r"<->"),
    ("IMPLIES", r"->"),
    ("OR", r"\|"),
    ("AND", r"&"),
    ("NOT", r"~"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("FORALL", r"forall\b"),
    ("EXISTS", r"exists\b"),
    ("VAR", r"[A-Za-z][A-Za-z0-9_]*"),
    ("MISMATCH", r"."),
]


def lex(code: str) -> Iterator[Tuple[str, str]]:

    # -- This has nothing to do with your input, it's the logic langauge itself --
    parts: List[str] = []
    for pair in TOKEN_SPECS:
        name: str = pair[0]  # The label (e.g., 'AND')
        pattern: str = pair[1]  # The regex (e.g., '&')

        # Create the 'Named Group' string
        labeled_pattern: str = "(?P<" + name + ">" + pattern + ")"
        parts.append(labeled_pattern)
    # 3. Join all rules into one 'Master Rule' string
    tok_regex: str = "|".join(parts)


    # Take the Master Rule we just built and slide it over the User's Input to see what fits
    scanner = re.finditer(tok_regex, code)
    for mo in scanner:
        # Grab the label from the match (the 'P' name we gave it)
        kind:str = mo.lastgroup
        # Grab the actual text found in the string
        value:str = mo.group()
        # If it's a space, discard it and move to the next loop
        if kind == "SKIP":
            continue
        # If nothing else matched, it hits the MISMATCH rule
        if kind == "MISMATCH":
            error_msg = "Unexpected character: " + value
            raise ValueError(error_msg)
        token:Token = (kind, value)
        yield token

# Output sample (It's a generator so it yields one by one):
# ("VAR", "A")
# ("AND", "&")
# ("VAR", "B")