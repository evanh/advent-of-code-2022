import sys
sys.path.append("..")

from lineparser import readfile


def sorttrim(cal_list, new_val):
    cal_list.append(new_val)
    cal_list = sorted(cal_list, reverse=True)
    return cal_list[:3]

max_cals = [0, 0, 0]
cur_sum = 0
for line in readfile():
    if line == "":
        max_cals = sorttrim(max_cals, cur_sum)
        cur_sum = 0
        continue

    cur_sum += int(line)

max_cals = sorttrim(max_cals, cur_sum)

print(max_cals)
print("MAX:", sum(max_cals))