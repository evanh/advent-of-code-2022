import sys

def readfile():
    filename = "test.input"
    if "-a" in sys.argv:
        filename = "actual.input"

    for line in open(filename, "r"):
        yield line.strip()