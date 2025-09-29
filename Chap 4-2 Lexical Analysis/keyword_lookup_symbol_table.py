"""
•	Names (identifiers) and reserved words (keywords) look the same: letters/digits/underscores,
    starting with a letter (e.g., if, while, total, return).
•	Instead of building a huge state diagram for every keyword, we:
    1.	Recognize all of them with the same pattern (e.g., [A-Za-z_][A-Za-z0-9_]*),
    2.	Then do a table lookup:
        	If the lexeme is in the keywords table, tag it as a keyword token (e.g., IF, ELSE, RETURN).
        	Otherwise, tag it as an IDENT (identifier).
•	The symbol table is the compiler’s “database of names.” The lexer usually:
    o	Creates an entry the first time it sees a new identifier (e.g., total),
    o	Leaves attributes like type, scope, etc., unset (to be filled by later phases such as the
        parser/semantic analyzer).
"""
import re

# KEYWORDS table (lookup) - exact matches only
KEYWORDS = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "return": "RETURN",
    "int": "TYPE_INT",
    "float": "TYPE_FLOAT",
    "bool": "TYPE_BOOL",
    "true": "BOOL_TRUE",
    "false": "BOOL_FALSE",
}

# TOKEN SPEC (single regex with named groups)
TOKEN_SPEC = [
    ("NUMBER",   r"\d+"),
    ("ID",       r"[A-Za-z_][A-Za-z0-9_]*"),
    ("OP",       r"[+\-*/=<>]"),
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("LBRACE",   r"\{"),
    ("RBRACE",   r"\}"),
    ("SEMICOLON",r";"),
    ("COMMA",    r","),
    ("SKIP",     r"[ \t\n]+"),
    ("MISMATCH", r"."),
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

print(TOKEN_REGEX)