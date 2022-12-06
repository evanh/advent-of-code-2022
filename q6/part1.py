import sys
sys.path.append("..")

from lineparser import readfile


test_inputs = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]

"""
Maintain a 4 char buffer, do a set cast/length check
"""

def find_marker(signal):
    buffer = list(signal[:4]) # initialize buffer
    idx = 4
    for symbol in signal[4:]:
        if len(set(buffer)) == 4:
            return idx

        buffer.pop(0)
        buffer.append(symbol)
        idx += 1

for testi, expected in test_inputs:
    output = find_marker(testi)
    assert find_marker(testi) == expected, f"{testi}: {output}"

parse_input = list(readfile())[0]
marker = find_marker(parse_input)
print("MARKER: ", marker)