data_path = "./data/day3.txt"
test_path = "./data/test.txt"
use_test = False

with open(data_path if not use_test else test_path, 'r') as f:
    lines = "".join(f.readlines()).split("\n")

def get_priority(letter):
    # Use character's ascii code to find the priority of each object.
    return ord(letter) - ord('a') + 1 if letter.islower() else ord(letter) - ord('A') + 27

total = 0
for line in lines:
    fc,sc = line[:len(line)//2], line[len(line)//2:] # Split data in two compartments
    intersection = "".join(set(fc).intersection(set(sc))) # Checks common elements between both compartments
    total += get_priority(intersection) 

print(total)


# Part 2:
total = 0
groups = [[lines[i], lines[i+1], lines[i+2]] for i in range(0, len(lines), 3)]
for g in groups:
    intersection = "".join(set(g[0]).intersection(set(set(g[1]).intersection(set(g[2])))))
    total += get_priority(intersection)

print(total)