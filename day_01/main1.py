import os

INPUT_FILE = "input.txt"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode="r") as file:
    lines = [line.strip() for line in file.readlines() if line]


left, right = [], []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))
left.sort()
right.sort()

answer = sum(abs(l - r) for l, r in zip(left, right))
print(answer)
