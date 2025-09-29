"""
Tokens we want to recognize:

- identifiers --> Variable names that start with a letter, can include letters or digits after that

- integer literals --> One or more digits

- operators --> +-*/

- assignment operator (=)
"""

def tokenize(expr):
    tokens = []
    i = 0

    while i < len(expr):
        ch = expr[i]

        # ignore white space
        if ch.isspace():
            i += 1
            continue

        # Identifiers (start with letter)
        if ch.isalpha():
            lexeme = ch
            i += 1
            while i < len(expr) and expr[i].isalnum():
                lexeme += expr[i]
                i += 1
            tokens.append(("IDENT", lexeme))

        # Integer Literals
        elif ch.isdigit():
            lexeme = ch
            i += 1
            while i < len(expr) and expr[i].isdigit():
                lexeme += expr[i]
                i += 1
            tokens.append(("INT_LIT", int(lexeme)))

        elif ch == '=':
            tokens.append(("ASSIGN_OP", ch))
            i += 1

        # Operators
        elif ch in "+-*/":
            tokens.append(("OP", ch))
            i += 1

        # Anything else = error
        else:
            tokens.append(("ERROR", ch))
            i += 1

    return tokens

def make_table(tokenize_result):
    token_header = 'Token'
    lexeme_header = 'Lexeme'
    print(f'{token_header:<10}{lexeme_header}')
    print('-----------------------')
    for token, lexeme in tokenize_result:
        print(f'{token:<10}{lexeme}')


def main():
    expression = 'result1 = value2 + 100 / x3'
    result = tokenize(expression)
    make_table(result)


if __name__ == "__main__":
    main()
