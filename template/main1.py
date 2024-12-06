import os

INPUT_FILE = "test_input.txt"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode="r") as file:
    lines = [line.strip() for line in file.readlines() if line]


for lines in lines:
    print(lines)
