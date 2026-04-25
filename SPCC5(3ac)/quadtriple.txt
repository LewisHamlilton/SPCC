# Read 3AC from user
print("Enter Three Address Code (type 'END' to stop):")
code = []
while True:
    line = input()
    if line.strip() == "END":
        break
    code.append(line)

# Generate Quadruples
quadruples = []
for line in code:
    left, expr = line.split('=')
    left = left.strip()
    a, op, b = expr.strip().split()
    quadruples.append((op, a, b, left))

# Generate Triples
triples = []
index_map = {}

for i, line in enumerate(code):
    left, expr = line.split('=')
    left = left.strip()
    a, op, b = expr.strip().split()

    if a in index_map:
        a = f"({index_map[a]})"
    if b in index_map:
        b = f"({index_map[b]})"

    triples.append((op, a, b))
    index_map[left] = i


# OUTPUT
print("\nThree Address Code:")
for line in code:
    print(line)

print("\nQuadruples:")
print("Index\tOp\tArg1\tArg2\tResult")
for i, q in enumerate(quadruples):
    print(f"{i}\t{q[0]}\t{q[1]}\t{q[2]}\t{q[3]}")

print("\nTriples:")
print("Index\tOp\tArg1\tArg2")
for i, t in enumerate(triples):
    print(f"{i}\t{t[0]}\t{t[1]}\t{t[2]}")
