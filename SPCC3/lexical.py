import re

def lexical(expr):
    tokens, sym, count = [], {}, 1

    for m in re.finditer(r'[a-zA-Z_]\w*|\d+|[=+\-*()]', expr):
        lex = m.group()

        if lex[0].isalpha():
            if lex not in sym:
                sym[lex] = count
                count += 1
            tokens.append(('ID', lex))
        elif lex.isdigit():
            tokens.append(('NUM', lex))
        else:
            tokens.append(('OP', lex))

    return tokens, sym


# MAIN
expr = input("Enter the input expression: ")
tokens, sym = lexical(expr)

print("\nLexical Analysis\n")
print(f"{'Lexeme':<8} | Token")
print("-" * 20)

for t, lex in tokens:
    out = f"<id,{sym[lex]}>" if t == 'ID' else f"<{lex}>"
    print(f"{lex:^8} |  {out}")
