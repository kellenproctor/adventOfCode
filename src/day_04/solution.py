def part1(data):
    pass

def part2(data):
    pass

def main():
    # Test data
    with open("test", "r") as f:
        test_data = f.read().strip()
    
    # Real data
    #with open("input", "r") as f:
    #    data = f.read().strip()
    
    print("Part 1 (test):", part1(test_data))
    #print("Part 1:", part1(data))
    print("Part 2 (test):", part2(test_data))
    #print("Part 2:", part2(data))

if __name__ == "__main__":
    main()
