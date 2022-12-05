import sys
sys.path.append("..")

from lineparser import readfile
from dataclasses import dataclass

@dataclass
class Interval():
    left: int
    right: int

    def overlaps(self, other):
        return ((self.left >= other.left and self.left <= other.right) or
        (self.right >= other.left and self.right <= other.right))


def parse_sections(line):
    l, r = line.split(",")
    lmin, lmax = l.split("-")
    rmin, rmax = r.split("-")
    return (Interval(int(lmin), int(lmax)), Interval(int(rmin), int(rmax)))


def intersect(left, right):
    return left.overlaps(right) or right.overlaps(left)


contained = 0
for line in readfile():
    left, right = parse_sections(line)
    if intersect(left, right):
        contained += 1

print("MAX:", contained)