import os
from collections import Counter

INPUT_FILE = "input.txt"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode="r") as file:
    lines = [line.strip() for line in file.readlines() if line]


left, right = [], []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

right_counter = Counter(right)

answer = sum(l * right_counter[l] for l in left if l in right_counter)
print(answer)
