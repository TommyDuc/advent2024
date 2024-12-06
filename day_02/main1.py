import os
from collections.abc import Sequence
from itertools import pairwise

INPUT_FILE = "input.txt"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode="r") as file:
    lines = [line.strip() for line in file.readlines() if line]

arrays = [[int(n) for n in l.split()] for l in lines]


def is_safe(array: Sequence[int]) -> bool:
    is_increasing = True
    is_decreasing = True
    for n0, n1 in pairwise(array):
        d = n1 - n0
        is_increasing &= d > 0
        is_decreasing &= d < 0
        if not (1 <= abs(d) <= 3):
            return False
    return is_increasing or is_decreasing


answer = len(list(filter(is_safe, arrays)))
print(answer)
