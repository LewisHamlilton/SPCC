import re

expr = input("Enter expression:\n> ")

final_target = expr.split(":=")[0].strip() if ":=" in expr else "d"
subs = re.findall(r'\(([^)]+)\)', expr)

if len(subs) < 2:
    print("Need at least two expressions like (a-b)")
    exit()

steps = [
    ("t", subs[0]),
    ("u", subs[1]),
    ("v", "t + u"),
    (final_target, "v + u")
]

# Header
print("\n{:<15} {:<20} {:<25} {}".format(
    "Statements", "Code Generated", "Register descriptor", "Address descriptor"))
print("-" * 90)
print("{:<15} {:<20} {}".format("", "", "Register empty"))

r0, r1 = "", ""

for i, (target, exp) in enumerate(steps):
    stmt = f"{target} := {exp}"

    if "-" in exp:
        a, b = exp.split("-")
        reg = "R0" if i == 0 else "R1"

        if reg == "R0":
            r0 = target
        else:
            r1 = target

        # MOV line
        print(f"{stmt:<15} {'MOV ' + a.strip() + ', ' + reg:<20} "
              f"R0 contains {r0}" if r0 else "", end="")

        if reg == "R0":
            print(f"{'':<5} {target} in R0")
        else:
            print(f"{'':<5} {target} in R1")

        # SUB line
        print(f"{'':<15} {'SUB ' + b.strip() + ', ' + reg:<20} "
              f"{'R1 contains ' + r1 if r1 else 'R1 contains '}")

    elif "+" in exp:
        r0 = target

        print(f"{stmt:<15} {'ADD R1, R0':<20} R0 contains {r0:<10} u in R1")

        if i != len(steps) - 1:
            print(f"{'':<15} {'':<20} R1 contains u       v in R0")
        else:
            print(f"{'':<15} {'MOV R0, ' + target:<20} R1 contains u       {target} in R0 and memory")

    print()
