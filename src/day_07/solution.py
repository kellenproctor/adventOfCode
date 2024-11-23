strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def compare_hands(hand1, hand2):
    for i in range(len(hand1)):
        if strength.index(hand1[i]) < strength.index(hand2[i]):
            return 1
        elif strength.index(hand1[i]) > strength.index(hand2[i]):
            return -1
        else:
            continue
    return 0

def get_type(hand):
    pass

def part1(data):
    hands = [line for line in data.split("\n")]
    for x in range(len(hands)-1):
        print(compare_hands(hands[x], hands[x+1]))


def part2(data):
    pass

def main():
    # Test data
    with open("test", "r") as f:
        test_data = f.read().strip()
    
    # Real data
    # with open("input", "r") as f:
    #     data = f.read().strip()
    
    print("Part 1 (test):", part1(test_data))
    # print("Part 1:", part1(data))
    # print("Part 2 (test):", part2(test_data))
    # print("Part 2:", part2(data))

if __name__ == "__main__":
    main()
