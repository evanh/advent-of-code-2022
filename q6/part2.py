import sys
sys.path.append("..")

from lineparser import readfile


test_inputs = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]

"""
Maintain a 14 char buffer, do a set cast/length check
"""

def find_marker(signal):
    buffer = list(signal[:14]) # initialize buffer
    idx = 14
    for symbol in signal[14:]:
        if len(set(buffer)) == 14:
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