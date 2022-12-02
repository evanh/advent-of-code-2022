import sys
sys.path.append("..")

from lineparser import readfile

# scores for throwing a certain shape
shape_scores = {"X": 1, "Y": 2, "Z": 3}
# matrix of lose/draw/win scores based on possible combinations
scores = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

def round_score(opp, me):
    return scores[opp][me]

score = 0
for line in readfile():
    opp, me = line.split()
    score += shape_scores[me] + round_score(opp, me)

print(score)