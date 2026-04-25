class MacroProcessor:
    def __init__(self):
        self.MNT = []
        self.MDT = []
        self.ALA = []

    # ---------------- PASS 1 ----------------
    def pass1(self, lines):
        i = 0
        mdtc = 1
        mntc = 1
        ala_index = 1

        while i < len(lines):
            line = lines[i].strip()

            if line == "":
                i += 1
                continue

            # detect macro header
            if "&" in line and "," in line:
                header = line
                parts = header.split()

                name = parts[0]
                args = parts[1].split(',')

                self.MNT.append((mntc, name, mdtc))
                mntc += 1

                local_map = {}
                for idx, arg in enumerate(args, 1):
                    arg = arg.strip()
                    local_map[arg] = f"#{idx}"
                    self.ALA.append((ala_index, arg))
                    ala_index += 1

                self.MDT.append((mdtc, header))
                mdtc += 1

                i += 1
                while i < len(lines) and lines[i].strip() != "MEND":
                    line = lines[i].strip()
                    for arg, rep in local_map.items():
                        line = line.replace(arg, rep)
                    self.MDT.append((mdtc, line))
                    mdtc += 1
                    i += 1

                self.MDT.append((mdtc, "MEND"))
                mdtc += 1

            i += 1

    # ---------------- PASS 2 ----------------
    def pass2(self, lines):
        MDT2 = []
        ALA2 = []

        i = 0
        mdtc = 1

        while i < len(lines):
            line = lines[i].strip()

            # skip macro definitions
            if "&" in line and "," in line:
                i += 1
                while i < len(lines) and lines[i].strip() != "MEND":
                    i += 1
                i += 1
                continue

            parts = line.split()

            # check for macro call
            if parts and any(m[1] == parts[0] for m in self.MNT):
                name = parts[0]

                # get actual arguments
                args = parts[1].split(",") if len(parts) > 1 else []

                # build ALA2
                for val in args:
                    ALA2.append((len(ALA2)+1, val.strip()))

                mdt_index = next(m[2] for m in self.MNT if m[1] == name)

                j = mdt_index
                while self.MDT[j-1][1] != "MEND":
                    line = self.MDT[j-1][1]

                    # skip prototype line
                    if "&" in line:
                        j += 1
                        continue

                    # replace parameters
                    for idx, val in enumerate(args, 1):
                        line = line.replace(f"#{idx}", val.strip())

                    MDT2.append((mdtc, line))
                    mdtc += 1
                    j += 1

                MDT2.append((mdtc, "MEND"))
                mdtc += 1

            i += 1

        return MDT2, ALA2


# ---------------- PRINT PASS 1 ----------------
def print_pass1(mp):
    print("Output:")
    print("Pass 1\n")

    print("MNT")
    print("MNTC      Macro Name      MDT")
    for m in mp.MNT:
        print(f"{m[0]:<10}{m[1]:<15}{m[2]}")

    print("\nALA")
    print("Index            Argument")
    for a in mp.ALA:
        print(f"{a[0]:<18}{a[1]}")

    print("\nMDT")
    print("MDTC      Macro Definition")
    for m in mp.MDT:
        print(f"{m[0]:<10}{m[1]}")


# ---------------- PRINT PASS 2 ----------------
def print_pass2(MDT2, ALA2):
    print("\nPass 2\n")

    print("MDT")
    print("MDTC      Macro Definition")
    for m in MDT2:
        print(f"{m[0]:<10}{m[1]}")

    print("\nALA")
    print("Index            Arguments")
    for a in ALA2:
        print(f"{a[0]:<18}{a[1]}")


# ---------------- MAIN ----------------
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    mp = MacroProcessor()
    mp.pass1(lines)
    print_pass1(mp)

    MDT2, ALA2 = mp.pass2(lines)
    print_pass2(MDT2, ALA2)


if __name__ == "__main__":
    main()
