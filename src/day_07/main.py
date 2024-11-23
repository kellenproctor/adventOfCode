from collections import Counter
from functools import cmp_to_key

cards1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def check_hands(hand1, hand2, cards):
    for x in range(len(hand1)):
        if cards.index(hand1[x]) < cards.index(hand2[x]):
            return 1
        elif cards.index(hand1[x]) > cards.index(hand2[x]):
            return -1
        else:
            continue
    return 0

def get_type(hand):
    # Count the frequency of each character
    freq = Counter(hand)

    # Get the frequency values (how many times each character appears)
    counts = sorted(freq.values(), reverse=True)

    # Check the hand classification based on counts
    if counts == [5]:  # Five of a kind
        return 6 # "Five of a kind"
    elif counts == [4, 1]:  # Four of a kind
        return 5 # "Four of a kind"
    elif counts == [3, 2]:  # Full house
        return 4 # "Full house"
    elif counts == [3, 1, 1]:  # Three of a kind
        return 3 # "Three of a kind"
    elif counts == [2, 2, 1]:  # Two pair
        return 2 # "Two pair"
    elif counts == [2, 1, 1, 1]:  # One pair
        return 1 # "One pair"
    else:
        return 0 # "High card"

def sort_by_hands(tuple1, tuple2):
    # First, compare by the first item (hand identifier integer)
    if tuple1[0] < tuple2[0]:
        return -1
    elif tuple1[0] > tuple2[0]:
        return 1
    # If the first items are equal, compare the hands using check_hands
    return check_hands(tuple1[1], tuple2[1], cards1)

def part1(data):
    hands = []
    for line in data:
        hand, bet = line.strip().split(" ")
        type = get_type(hand)
        hands.append((type, hand, int(bet)))
    new_hands = sorted(hands, key=cmp_to_key(sort_by_hands))
    return sum((x + 1) * item[2] for x, item in enumerate(new_hands))

def get_type_joker(hand):
    # Count the frequency of each character
    freq = Counter(hand)
    jokers = freq.get("J", 0)

    # Get the frequency values (how many times each character appears)
    counts = sorted(freq.values(), reverse=True)

    # Check the hand classification based on counts
    if counts == [5]:  # Five of a kind
        return 6 # "Five of a kind"
    elif counts == [4, 1]:  # Four of a kind
        return 6 if jokers else 5 # "Four of a kind"
    elif counts == [3, 2]:  # Full house
        return 6 if jokers else 4 # "Full house"
    elif counts == [3, 1, 1]:  # Three of a kind
        return 5 if jokers else 3 # "Three of a kind"
    elif counts == [2, 2, 1]:  # Two pair
        if jokers == 2:
            return 5
        elif jokers == 1:
            return 4
        else:
            return 2 # "Two pair"
    elif counts == [2, 1, 1, 1]:  # One pair
        if jokers:
            return 3
        else:
            return 1 # "One pair"
    else:
        if jokers:
            return 1
        else:
            return 0 # "High card"

def sort_by_hands_joker(tuple1, tuple2):
    # First, compare by the first item (hand identifier integer)
    if tuple1[0] < tuple2[0]:
        return -1
    elif tuple1[0] > tuple2[0]:
        return 1
    # If the first items are equal, compare the hands using check_hands
    return check_hands(tuple1[1], tuple2[1], cards2)

def part2(data):
    hands = []
    for line in data:
        hand, bet = line.strip().split(" ")
        type = get_type_joker(hand)
        hands.append((type, hand, int(bet)))
    new_hands = sorted(hands, key=cmp_to_key(sort_by_hands_joker))
    return sum((x + 1) * item[2] for x, item in enumerate(new_hands))



if __name__ == "__main__":
    test = []
    input = []

    with open("test") as file:
        for line in file:
            test.append(line)

    with open("input") as file:
        for line in file:
            input.append(line)

    # print(f"Part 1 (test): {str(part1(test))}")
    # print(f"Part 1: {str(part1(input))}")
    print(f"Part 2 (test): {str(part2(test))}")
    print(f"Part 2: {str(part2(input))}")
