import sys
sys.path.append("..")

from lineparser import readfile
from dataclasses import dataclass

"""
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
"""
test_input = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"],
]
"""
[T]             [P]     [J]
[F]     [S]     [T]     [R]     [B]
[V]     [M] [H] [S]     [F]     [R]
[Z]     [P] [Q] [B]     [S] [W] [P]
[C]     [Q] [R] [D] [Z] [N] [H] [Q]
[W] [B] [T] [F] [L] [T] [M] [F] [T]
[S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
[Q] [Q] [B] [D] [J] [W] [H] [R] [J]
 1   2   3   4   5   6   7   8   9
"""
actual_input = [
    ["Q", "S", "W", "C", "Z", "V", "F", "T"],
    ["Q", "R", "B"],
    ["B", "Z", "T", "Q", "P", "M", "S"],
    ["D", "V", "F", "R", "Q", "H"],
    ["J", "G", "L", "D", "B", "S", "T", "P"],
    ["W", "R", "T", "Z"],
    ["H", "Q", "M", "N", "S", "F", "R", "J"],
    ["R", "N", "F", "H", "W"],
    ["J", "Z", "T", "Q", "P", "R" ,"B"],
]



@dataclass
class Move:
    start: int
    end: int
    quantity: int


def parse_move(line):
    # move 1 from 2 to 1
    parts = line.split(" ")
    quantity = int(parts[1])
    start = int(parts[3]) - 1
    end = int(parts[5]) - 1
    return Move(start, end, quantity)


def move(move, stacks):
    for i in range(move.quantity):
        box = stacks[move.start].pop()
        stacks[move.end].append(box)


stacks = actual_input if "-a" in sys.argv else test_input
for line in readfile():
    to_move = parse_move(line)
    move(to_move, stacks)

chars = [s[-1] for s in stacks]
print(''.join(chars))
# print(stacks)