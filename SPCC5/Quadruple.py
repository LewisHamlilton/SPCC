import re

temp_count = 1
three_ac, quadruples, seen = [], [], {}

def new_temp():
    global temp_count
    t = f"t{temp_count}"
    temp_count += 1
    return t

def infix_to_postfix(expr):
    prec = {'=':0, '+':1, '-':1, '*':2, '/':2}
    stack, output = [], []
    tokens = re.findall(r'\w+|[=+\-*/()]', expr)

    for t in tokens:
        if t.isalnum():
            output.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[t]:
                output.append(stack.pop())
            stack.append(t)

    return output + stack[::-1]

def generate(expr):
    global temp_count
    temp_count = 1
    three_ac.clear()
    quadruples.clear()
    seen.clear()

    stack = []

    for t in infix_to_postfix(expr):
        if t.isalnum():
            stack.append(t)
        else:
            b, a = stack.pop(), stack.pop()

            if t == '=':
                three_ac.append(f"{a} = {b}")
                quadruples.append((t, b, "", a))
                stack.append(a)
                continue

            key = a+t+b
            rev = b+t+a

            if key in seen:
                temp = seen[key]
            elif t in "+*" and rev in seen:
                temp = seen[rev]
            else:
                temp = new_temp()
                seen[key] = temp
                three_ac.append(f"{temp} = {a} {t} {b}")
                quadruples.append((t, a, b, temp))

            stack.append(temp)

# Main
expr = input("Enter expression: ")
generate(expr)

print("\nThree Address Code:")
for line in three_ac:
    print(line)

print("\nQuadruples:")
print("Index\tOp\tArg1\tArg2\tResult")
for i, (op,a,b,res) in enumerate(quadruples):
    print(f"{i}\t{op}\t{a}\t{b}\t{res}")
