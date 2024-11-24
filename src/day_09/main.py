def get_sequence(data):
    return [int(y) - int(x) for x, y in zip(data[0:], data[1:])]

def part1(data):
    total = 0
    for line in data.split("\n"):
        answer = [int(x) for x in line.split()]
        last = [answer[-1]]
        while sum(answer) != 0:
            answer = get_sequence(answer)
            last.append(answer[-1])
        total += sum(last)  
    return total

def get_next(s):
    val = 0
    for x in range(len(s)-2, -1, -1):
        val = s[x] - val
    return val

def part2(data):
    total = 0
    for line in data.split("\n"):
        answer = [int(x) for x in line.split()]
        last = [answer[0]]
        while sum(answer) != 0:
            answer = get_sequence(answer)
            last.append(answer[0])
        total += get_next(last)
    return total

def main():
    # Test data
    with open("test", "r") as f:
        test_data = f.read().strip()
    
    # Real data
    with open("input", "r") as f:
        data = f.read().strip()
    
    # print("Part 1 (test):", part1(test_data))
    # print("Part 1:", part1(data))
    print("Part 2 (test):", part2(test_data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()
