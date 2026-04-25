rules, terminals, precedence = [], [], {}

# ─── EXTRACT TERMINALS ───
def extract_terminals():
    t = []
    for r in rules:
        for c in r.split("->")[1]:
            if not c.isupper() and c != '|' and c not in t:
                t.append(c)
    terminals[:] = t + ['$']

# ─── CHECK OPG ───
def is_opg():
    return all(not (rhs[i].isupper() and rhs[i+1].isupper())
               for r in rules for rhs in [r.split("->")[1]]
               for i in range(len(rhs)-1))

# ─── PRIORITY ───
def pr(c): return 3 if c=='/' else 2 if c=='*' else 1 if c in '+-' else 0

# ─── BUILD TABLE (UNCHANGED LOGIC) ───
def build_table():
    for a in terminals:
        precedence[a] = {}
        for b in terminals:
            a_op, b_op = a in "+-*/", b in "+-*/"
            a_id, b_id = a.islower(), b.islower()

            if a=='(' and b==')': rel="="
            elif a=='(' and b=='(': rel="<"
            elif a==')' and b==')': rel=">"
            elif a=='(' and b_id: rel="<"
            elif a_id and b==')': rel=">"
            elif a_id and b_id: rel="-"
            elif a=='(' and b=='$': rel=">"
            elif a=='$' and b_id: rel="<"
            elif a_id and b=='$': rel=">"
            elif a=='$' and b=='(': rel="<"
            elif a==')' and b=='$': rel=">"
            elif a_op and b_id: rel="<"
            elif a_id and b_op: rel=">"
            elif a=='$' and b_op: rel="<"
            elif a_op and b=='$': rel=">"
            elif a==')' and b_op: rel=">"
            elif a_op and b==')': rel=">"
            elif a=='(' and b_op: rel="<"
            elif a_op and b=='(': rel="<"
            elif a_op and b_op: rel=">" if pr(a)>=pr(b) else "<"
            elif a=='$' and b=='$': rel="Accept"
            else: rel="E"

            precedence[a][b] = rel

# ─── DISPLAY TABLE ───
def display():
    print("    ", *terminals)
    for a in terminals:
        print(a, "  ", *[precedence[a][b] for b in terminals])

# ─── MATCH ───
def match(stack, prod):
    if len(stack) < len(prod): return False
    for s, p in zip(stack[-len(prod):], prod):
        if (p.isupper() and not s.isupper()) or \
           (p=='i' and not s.islower()) or \
           (p not in "iABCDEFGHIJKLMNOPQRSTUVWXYZ" and s!=p):
            return False
    return True

# ─── PARSE ───
def parse(inp):
    stack = "$"
    print("Stack\t\tSign\tInput\t\tAction")
    print("-"*50)

    while True:
        i = len(stack)-1
        while stack[i].isupper(): i -= 1
        top, nxt = stack[i], inp[0]

        if top=='$' and nxt=='$':
            print(f"{stack:<15} {'':<7} {inp:<15} Accept")
            break

        rel = precedence[top][nxt]
        action = "Shift" if rel in "<=" else "Reduce" if rel==">" else "Error"

        print(f"{stack:<15} {rel:<7} {inp:<15} {action}")
        if action=="Error": break

        if action=="Shift":
            stack += nxt; inp = inp[1:]
        else:
            for r in rules:
                A, rhs = r.split("->")
                for p in rhs.split("|"):
                    if match(stack, p):
                        stack = stack[:-len(p)] + A
                        break
                else: continue
                break

# ─── MAIN ───
print("Reading Grammar From File...")
with open("grammar.txt") as f:
    rules = [l.strip().replace(" ","") for l in f if l.strip()]

inp = input("Enter your Input String : ")

print("\nSTEP 1 : Checking Grammar is Operator Precedence or not")
extract_terminals()

if not is_opg():
    print("Given grammar is NOT an Operator Precedence Grammar")
    exit()

print("Given grammar IS an Operator Precedence Grammar")

print("\nSTEP 2 : Create and Display Operator Precedence Table")
build_table()
display()

print("\nSTEP 3 : Append $ to End of Input String")
inp += "$"
print("After appending $ :", inp)

print("\nSTEP 4 : Parsing Table")
parse(inp)
