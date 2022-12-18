calories, data_path = [], "./data/day2.txt"

# A: Opponent chose rock
# B: Opponent chose paper
# C: Opponent chose scissors
# X: chose rock
# Y: chose paper
# Z: chose scissors

# Part 1:
rps = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'W': 6,
    'D': 3,
    'L': 0,
    'A X': 'D',
    'A Y': 'W',
    'A Z': 'L',
    'B X': 'L',
    'B Y': 'D',
    'B Z': 'W',
    'C X': 'W',
    'C Y': 'L',
    'C Z': 'D'
}

with open(data_path, 'r') as f:
    lines = "".join(f.readlines()).split("\n")

total = 0
for line in lines:
    picks = line.split(' ')
    total += rps[picks[1]]
    total += rps[rps[line]]
print(total)

rps = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'W': 6,
    'D': 3,
    'L': 0,
}

# Part 2:
# A: Opponent chose rock
# B: Opponent chose paper
# C: Opponent chose scissors
# X: Need to lose
# Y: Need to draw
# Z: Need to win
strategy = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
    'A X': 'Z', # If opponent chose rock, and I need to lose, then I have to choose scissors
    'A Y': 'X', # If opponent chose rock, and I need to draw, then I have to choose rock
    'A Z': 'Y', # If opponent chose rock, and I need to win, then I have to choose paper
    'B X': 'X', # If opponent chose paper, and I need to lose, then I have to choose rock
    'B Y': 'Y', # If opponent chose paper, and I need to draw, then I have to choose paper
    'B Z': 'Z', # If opponent chose paper, and I need to win, then I have to choose scissors
    'C X': 'Y', # If opponent chose scissors, and I need to lose, then I have to choose paper
    'C Y': 'Z', # If opponent chose scissors, and I need to draw, then I have to choose scissors
    'C Z': 'X', # If opponent chose scissors, and I need to win, then I have to choose rock
}

total = 0
for line in lines:
    picks = line.split(' ')
    total += rps[strategy[picks[1]]]
    total += rps[strategy[line]]