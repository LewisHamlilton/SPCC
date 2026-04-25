import re

temp_count = 1
seen = {}

def new_temp():
    global temp_count
    t = f"t{temp_count}"
    temp_count += 1
    return t

def infix_to_postfix(expr):
    prec = {'=':0, '+':1, '-':1, '*':2, '/':2}
    stack, output = [], []

    for t in re.findall(r'\w+|[=+\-*/();]', expr):
        if t == ';':
            continue
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

def generate_3ac(expr):
    global temp_count, seen
    temp_count = 1
    seen.clear()

    stack, code = [], []

    for t in infix_to_postfix(expr):
        if t.isalnum():
            stack.append(t)
        else:
            b, a = stack.pop(), stack.pop()

            if t == '=':
                code.append(f"{a} = {b}")
                stack.append(a)
            else:
                key = a + t + b
                rev = b + t + a

                # CSE logic
                if key in seen:
                    temp = seen[key]
                elif t in "+*" and rev in seen:
                    temp = seen[rev]
                else:
                    temp = new_temp()
                    seen[key] = temp
                    code.append(f"{temp} = {a} {t} {b}")

                stack.append(temp)

    return code

# Main
expr = input("Enter expression: ")
for line in generate_3ac(expr):
    print(line)
