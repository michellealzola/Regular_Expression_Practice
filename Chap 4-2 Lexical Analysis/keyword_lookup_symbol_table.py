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

# SYMBOL TABLE (seeded by the lexer when it sees new identifiers)
symbol_table = {}

def tokenize(code: str):  # code: str means this function expects code to be a string
    tokens = []
    for match_object in re.finditer(TOKEN_REGEX, code):
        kind = match_object.lastgroup
        lexeme = match_object.group()

        if kind == 'SKIP':
            continue

        if kind == 'MISMATCH':
            tokens.append(('ERROR', lexeme))
            continue

        if kind == 'ID':
            if lexeme in KEYWORDS:
                tokens.append((KEYWORDS[lexeme], lexeme))
            else:
                tokens.append(('IDENT', lexeme))
                # seed symbol table if first time we see this identifier
                symbol_table.setdefault(lexeme, {
                    'type': None,  # to be filled by later phases
                    'scope': None,  # to be filled by later phases
                    'attributes': {}  # extra info (e.g., line numbers) later
                })
        else:
            tokens.append((kind, lexeme))

    return tokens


code = '''
int total = value + 3;
if (total > 10) return total; else 0;
'''

tokens = tokenize(code)
print('TOKENS:')

for token in tokens:
    print(token)

print("\nSYMBOL TABLE (seeded by lexer):")
for name, info in symbol_table.items():
    print(name, "→", info)




