import sys
sys.path.append("..")

from lineparser import readfile
from dataclasses import dataclass

@dataclass
class Interval():
    left: int
    right: int

    def is_inside(self, other):
        return self.left >= other.left and self.right <= other.right


def parse_sections(line):
    l, r = line.split(",")
    lmin, lmax = l.split("-")
    rmin, rmax = r.split("-")
    return (Interval(int(lmin), int(lmax)), Interval(int(rmin), int(rmax)))


def intersect(left, right):
    return left.is_inside(right) or right.is_inside(left)


contained = 0
for line in readfile():
    left, right = parse_sections(line)
    if intersect(left, right):
        contained += 1

print("MAX:", contained)