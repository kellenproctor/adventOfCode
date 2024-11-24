from functools import reduce

def part1(data):
    time, records = data.split("\n")
    time = [int(t) for t in time.split()[1:]]
    records = [int(d) for d in records.split()[1:]]

    ways = [0 for _ in range(len(time))]
    for x, time in enumerate(time):
        record = records[x]
        ways[x] = 0
        for i in range(1, time):
            distance = i * (time - i)
            if distance > record:
                ways[x] += 1
    return reduce(lambda acc, cur: acc * cur, ways)

def part2(data):
    time, records = data.split("\n")
    time = int(time.split(":")[1].replace(" ", ""))
    record = int(records.split(":")[1].replace(" ", ""))
    # print("Time:", time)
    # print("Records:", record)

    ways = 0
    for i in range(time):
        distance = i * (time - i)
        if distance > record:
            ways += 1
    return ways

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
