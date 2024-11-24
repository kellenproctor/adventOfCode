from typing import List

def get_sequence(numbers: List[int]) -> List[int]:
    """Calculate the differences between consecutive numbers in a sequence."""
    return [b - a for a, b in zip(numbers, numbers[1:])]

def extrapolate_sequence(numbers: List[int], forward: bool = True) -> int:
    """
    Extrapolate the next value in a sequence.
    
    Args:
        numbers: Initial sequence of numbers
        forward: If True, extrapolate forward (right), if False extrapolate backward (left)
    
    Returns:
        The extrapolated value
    """
    sequences = [numbers]
    current = numbers
    
    # Generate sequences until we get all zeros
    while any(current):
        current = get_sequence(current)
        sequences.append(current)
    
    if forward:
        # Forward extrapolation: add up the last numbers
        return sum(seq[-1] for seq in sequences)
    else:
        # Backward extrapolation: alternate subtraction from left
        result = 0
        for seq in sequences[::-1]:
            result = seq[0] - result
        return result

def solve_puzzle(data: str, forward: bool = True) -> int:
    """
    Solve the puzzle for either part 1 or 2.
    
    Args:
        data: Input data as string
        forward: If True, solve part 1, if False solve part 2
    
    Returns:
        Sum of all extrapolated values
    """
    return sum(
        extrapolate_sequence([int(x) for x in line.split()], forward)
        for line in data.splitlines()
    )

def part1(data: str) -> int:
    """Solve part 1: extrapolate forward."""
    return solve_puzzle(data, forward=True)

def part2(data: str) -> int:
    """Solve part 2: extrapolate backward."""
    return solve_puzzle(data, forward=False)

def main():
    # Test data
    with open("test", "r") as f:
        test_data = f.read().strip()
    
    # Real data
    with open("input", "r") as f:
        data = f.read().strip()
    
    print("Part 1 (test):", part1(test_data))
    print("Part 1:", part1(data))
    print("Part 2 (test):", part2(test_data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()

###
# This is a more elegant solution that Claude came up with after the fact.
# It's more readable and easier to understand.
###

"""
I'll suggest some improvements to make the code more efficient and readable.
Here are the main changes:
1. Combine similar logic between part1 and part2 into a single helper function
2. Use more descriptive variable names
3. Add type hints for better code clarity
4. Add docstrings for better documentation
5. Optimize the sequence generation logic


Key improvements:
1. Created a unified extrapolate_sequence function that handles both
   forward and backward extrapolation using a boolean parameter
2. Added type hints to make the code more maintainable and catch potential type errors
3. Added docstrings to explain what each function does
4. Created a solve_puzzle function to remove duplicate code between part1 and part2
5. Used more descriptive variable names (e.g., numbers instead of data for sequences)
6. Used splitlines() instead of split("\n") for better readability
7. Simplified the sequence generation logic by storing all sequences in a list
8. Made the code more functional by using list comprehensions and generator expressions


The improved code is more maintainable, easier to understand, and follows Python
best practices better. The logic is also more consolidated, reducing the chance
of bugs when making changes to either part of the solution.
"""