import re
expr = {}
copy = {}
values = {}
opt = []

for line in open("input.txt"):
    line=line.strip()
    if not line or line.startswith("//"):
        continue

    left,right=line.split("=")
    left,right=left.strip(),right.strip()

    # constant folding
    if re.fullmatch(r'[0-9+\-*/ ]+',right):
        right=str(eval(right))
        values[left]=right

    # copy propagation
    for v in copy:
        right=right.replace(v,copy[v])

    if re.fullmatch(r'T\d+',right):
        copy[left]=right
        continue

    # common subexpression elimination
    for e in expr:
        if e in right:
            right=right.replace(e,expr[e])

    expr[right]=left
    opt.append([left,right])

# -------- final cleanup pass --------
final=[]
copies={}

for l,r in opt:
    if re.fullmatch(r'T\d+',r):
        copies[l]=r
    else:
        for v in copies:
            r=r.replace(v,copies[v])
        final.append([l,r])

# -------- constant propagation pass --------
for i in range(len(final)):
    for v in values:
        final[i][1]=final[i][1].replace(v,values[v])

print("Optimized Code:")
for l,r in final:
    print(f"{l}={r}")

