import sys
sys.path.append("..")

from lineparser import readfile

max_cals = 0
cur_sum = 0
for line in readfile():
    if line == "":
        max_cals = max(cur_sum, max_cals)
        cur_sum = 0
        continue

    cur_sum += int(line)

max_cals = max(cur_sum, max_cals)
print("MAX:", max_cals)