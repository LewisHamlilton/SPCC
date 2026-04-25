# Simplified Assembler with Symbol, Literal & Pool Tables

MOT = {"ADD":"01","SUB":"02","MUL":"03","MOVER":"04","MOVEM":"05",
       "COMP":"06","BC":"07","DIV":"08","READ":"09","PRINT":"10","STORE":"11"}

REG = {"AREG":"01","BREG":"02","CREG":"03","DREG":"04"}

LC, sym_idx = 0, 1
symtab, littab, pooltab = {}, [], [0]
rows = []

def get_sym(s):
    global sym_idx
    if s not in symtab:
        symtab[s] = LC
        sym_idx += 1
    return list(symtab).index(s)+1, symtab[s]

def get_lit(l):
    for i,(lit,addr) in enumerate(littab):
        if lit == l: return i+1, addr
    littab.append([l,None])
    return len(littab), None

def assign_lit():
    global LC
    for i in range(pooltab[-1], len(littab)):
        if littab[i][1] is None:
            littab[i][1] = LC; LC += 1
    pooltab.append(len(littab))

# read input
with open("input.txt") as f:
    prog = [l.strip() for l in f if l.strip()]

for line in prog:
    p = line.replace(",","").split()
    src, inter, mach = line, "", ""

    if p[0]=="START":
        LC=int(p[1]); inter=f"(AD,01) (C,{p[1]})"

    elif p[0]=="END":
        assign_lit(); inter="(AD,02)"

    elif p[0]=="LTORG":
        assign_lit(); inter="(AD,03)"

    else:
        if ":" in p[0]:
            symtab[p[0][:-1]] = LC
            p = p[1:]

        if p[0] in MOT:
            op = MOT[p[0]]

            if len(p)==3:
                r = REG.get(p[1],"00")
                if p[2].startswith("="):
                    i,a = get_lit(p[2]); a = a or 0
                    inter=f"{LC} (IS,{op}) {r} (L,{i})"
                else:
                    i,a = get_sym(p[2])
                    inter=f"{LC} (IS,{op}) {r} (S,{i})"
                mach=f"{LC:03} {op} {r} {a:03}"

            elif len(p)==2:
                i,a = get_sym(p[1])
                inter=f"{LC} (IS,{op}) (S,{i})"
                mach=f"{LC:03} {op} 00 {a:03}"

            LC+=1

        elif len(p)>1 and p[1]=="DS":
            symtab[p[0]]=LC; size=int(p[2])
            inter=f"{LC} (DL,02) {size}"
            mach=f"{LC:03} -- -- ---"
            LC+=size

        elif len(p)>1 and p[1]=="DC":
            symtab[p[0]]=LC
            inter=f"{LC} (DL,01) {p[2]}"
            mach=f"{LC:03} 00 00 {p[2]}"
            LC+=1

    rows.append((src,inter,mach))

# output
print(f"{'SOURCE':<25}{'INTERMEDIATE':<30}{'MACHINE'}")
print("-"*80)
for r in rows:
    print(f"{r[0]:<25}{r[1]:<30}{r[2]}")

print("\nSYMBOL TABLE")
for i,(s,a) in enumerate(symtab.items(),1):
    print(i,s,a)

print("\nLITERAL TABLE")
for i,(l,a) in enumerate(littab,1):
    print(i,l,a)

print("\nPOOL TABLE")
for i,p in enumerate(pooltab):
    print(i,p)
