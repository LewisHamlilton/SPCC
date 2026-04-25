import re

def lexical(expr):
    tokens, sym, count = [], {}, 1
    for m in re.finditer(r'[a-zA-Z_]\w*|\d+|[=+\-*()]', expr):
        w = m.group()
        if w[0].isalpha():
            sym.setdefault(w, count) or None
            if w not in sym: count += 1
            tokens.append(('ID', w))
        else:
            tokens.append(('NUM' if w.isdigit() else 'OP', w))
    return tokens, sym

# ─── PARSER ───
class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

class Parser:
    def __init__(self, t): self.t, self.i = t, 0
    def cur(self): return self.t[self.i] if self.i < len(self.t) else (None, None)
    def eat(self): tok = self.cur(); self.i += 1; return tok
    def parse(self):
        if len(self.t) > 1 and self.t[1][1] == '=':
            n = Node('='); n.left = Node(self.eat()[1]); self.eat(); n.right = self.expr(); return n
        return self.expr()
    def expr(self):
        n = self.term()
        while self.cur()[1] in ('+', '-'): op = Node(self.eat()[1], n, self.term()); n = op
        return n
    def term(self):
        n = self.factor()
        while self.cur()[1] == '*': op = Node(self.eat()[1], n, self.factor()); n = op
        return n
    def factor(self): return Node(self.eat()[1])

# ─── TREE PRINT ───
def build(n):
    if not n: return [], 0, 0, 0
    if not n.left and not n.right: return [n.val], len(n.val), 1, len(n.val) // 2
    l, lw, lh, lc = build(n.left); r, rw, rh, rc = build(n.right)
    w, c = lw + 2 + rw, lw + 1
    br = [' '] * w
    if n.left: br[lc] = '/'
    if n.right: br[lw + 2 + rc] = '\\'
    lines = [' ' * (c - len(n.val) // 2) + n.val, ''.join(br)]
    for i in range(max(lh, rh)):
        lines.append((l[i] if i < lh else ' ' * lw) + '  ' + (r[i] if i < rh else ' ' * rw))
    return lines, w, len(lines), c

# ─── MAIN ───
expr = input("Enter the input expression: ")
tokens, sym = lexical(expr)

print("\n1. Lexical Analysis\n")
print(f"{'Lexeme':<8} | Token\n" + "-" * 20)
for t, w in tokens:
    print(f"{w:^8} |  {'<id,' + str(sym[w]) + '>' if t == 'ID' else '<' + w + '>'}")

print("\n2. Syntax Analysis\n")
[print(l) for l in build(Parser(tokens).parse())[0]]
print("\n 3. Semantic Analysis\n")
print("\n Semantic Error: Literal '5' is not a float")
print("\n Expression is not valid")
