#targetcode generation

with open("in.txt", "r") as f1, open("out.txt", "w") as f2:
    lines = f1.readlines()
    for i, line in enumerate(lines):
        s = line.split()
        if "=" in s:
            f2.write(f"\nLDA\t{s[s.index('=') + 1]}")
            if "+" in s:
                f2.write(f"\nADD\t{s[s.index('+') + 1]}")
            if "-" in s:
                f2.write(f"\nSUB\t{s[s.index('-') + 1]}")
            f2.write(f"\nSTA\t{s[s.index('=') - 1]}")

