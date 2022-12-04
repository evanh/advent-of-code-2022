import sys
sys.path.append("..")

from lineparser import readfile


def priority(a_char):
    if a_char.isupper():
        return ord(a_char) - 38
    else:
        return ord(a_char) - 96

shared = []
for line in readfile():
    midpoint = (len(line) / 2) # length 10 -> index 5
    comp1 = set()
    idx = 0
    for a_char in line:
        if idx < midpoint:
            comp1.add(a_char)
        else:
            if a_char in comp1:
                shared.append(a_char)
                break

        idx += 1

print(shared)
print(sum([priority(s) for s in shared]))