import re
from functools import reduce

grid = list()

with open("input") as f:
    for line in f:
        grid.append(line.rstrip())

kernel = [
    [-1, -1], [-1, 0], [ -1, 1],
    [ 0, -1],          [ 0,  1],
    [1,  -1], [1,  0], [ 1,  1],
]

def checkAround(row, col):
    for [rowx, coly] in kernel:
        rowc = row + rowx
        colc = col + coly
        if not (rowc < 0 or rowc >= len(grid) or colc < 0 or colc >= len(grid[row])):
            value = grid[rowc][colc]
            if value not in "0123456789.":
                return True
                break
    return False

def part1():
    numbers = []
    for row, line in enumerate(grid):
        matches = re.finditer(r"\d+", line)

        for match in matches:
            number = int(match.group())
            start = match.start()
            end = match.end()

            for col in range(start, end):
                if checkAround(row, col):
                    numbers.append(number)
                    break

    return reduce(lambda acc, cur: acc + cur, numbers)

def get_num(row, col):
    matches = re.finditer(r"\d+", grid[row])
    for match in matches:
        number = int(match.group())
        start = match.start()
        end = match.end()
        if col in range(start, end):
            return number

def find_nums(row, col):
    nums = []
    ratio = 0
    for row_d, col_d in kernel:
        row_c = row + row_d
        col_c = col + col_d
        if (0 <= row_c < len(grid) and 0 <= col_c < len(grid[row])):
            value = grid[row_c][col_c]
            if value in "0123456789":
                # Check if the new number overlaps with an already added one
                if not any(
                    existing_row == row_c and abs(existing_col - col_c) == 1
                    for existing_row, existing_col in nums
                ):
                    nums.append([row_c, col_c])

    gear_nums = list(map(lambda num: get_num(*num), nums))
    if len(gear_nums) == 2:
        ratio = reduce(lambda acc, cur: acc * cur, gear_nums)
    return ratio


def part2():
    answer = 0
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "*":
                ratio = find_nums(row, col)
                if ratio:
                    answer += ratio
    return answer

print(f"Part 1: {str(part1())}")
print(f"Part 2: {str(part2())}")