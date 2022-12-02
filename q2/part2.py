import sys
sys.path.append("..")

from lineparser import readfile

# scores for lose/draw/win
scores = {"X": 0, "Y": 3, "Z": 6}
# score for the shape we need to throw in order to match the strategy
shape_scores = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}

def round_score(opp, me):
    return shape_scores[opp][me]

score = 0
for line in readfile():
    opp, me = line.split()
    score += scores[me] + round_score(opp, me)

print(score)