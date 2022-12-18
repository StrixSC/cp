calories, data_path = [], "./data/day1.txt"

with open(data_path, 'r') as f:
    lines = "".join(f.readlines()).split("\n\n")

for line in lines:
    calories_clean = line.replace('\n', ',').split(',')
    calories.append(sum(list(map(int, calories_clean))))

print(calories[max(range(len(calories)), key=calories.__getitem__)])
top3 = []
for i in range(3):
    index = max(range(len(calories)), key=calories.__getitem__)
    top3.append(calories[index])
    del calories[index]

print(sum(top3))