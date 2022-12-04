import sys
sys.path.append("..")

from lineparser import readfile


def priority(a_char):
    if a_char.isupper():
        return ord(a_char) - 38
    else:
        return ord(a_char) - 96

shared = []
cur_group = []
for line in readfile():
    if len(cur_group) < 3:
        cur_group.append(set(line))
        continue

    badge = cur_group[0] & cur_group[1] & cur_group[2]
    shared.append(badge.pop())
    cur_group = [set(line)]

badge = cur_group[0] & cur_group[1] & cur_group[2]
shared.append(badge.pop())

print(shared)
print(sum([priority(s) for s in shared]))