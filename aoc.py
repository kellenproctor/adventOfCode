import os
import sys
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from colorama import init, Fore, Style
import argparse

load_dotenv()

# Initialize colorama
init()

def log_success(msg: str):
    print(f"{Fore.GREEN}✓{Style.RESET_ALL} {msg}")

def log_info(msg: str):
    print(f"{Fore.BLUE}ℹ{Style.RESET_ALL} {msg}")

def log_error(msg: str):
    print(f"{Fore.RED}✗{Style.RESET_ALL} {msg}")

# Store session cookie in environment variable or in a .env file
AOC_SESSION = os.getenv('AOC_SESSION')

def main():
    parser = argparse.ArgumentParser(description='Setup Advent of Code day')
    parser.add_argument('--day', type=str, help='Day number (1-25)', default='1')
    parser.add_argument('--next', action='store_true', default=False, help='Next day')
    parser.add_argument('--year', '-y', type=int, default=datetime.now().year,
                       help='Year of puzzle (defaults to current year)')
    
    args = parser.parse_args()
    day = args.day
    year = args.year

    if args.next:
        highest_day = max(int(day.strip('day_')) for day in os.listdir('src') if day.startswith('day_'))
        day = str(highest_day + 1)
    
    log_info(f"Setting up Advent of Code {year} - Day {day}")
    setup_day(day, year)
    log_success(f"Setup complete for Advent of Code {year} - Day {day}")
    

def get_input(day: str, year: int) -> str:
    """Download input for given day from Advent of Code"""
    if not AOC_SESSION:
        log_error("Please set AOC_SESSION environment variable with your session cookie")
        sys.exit(1)

    url = f"https://adventofcode.com/{year}/day/{int(day)}/input"
    headers = {'Cookie': f'session={AOC_SESSION}'}
    
    log_info(f"Downloading from: {url}")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        log_error(f"Error downloading input: {response.status_code}")
        log_error(response.text)
        sys.exit(1)
    
    return response.text.rstrip()  # Remove trailing newlines

solution_template = '''def part1(data):
    pass

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
'''

def setup_day(day: str, year: int):
    # Create directory structure
    day_dir = Path(f"src/day_{day.zfill(2)}")
    day_dir.mkdir(exist_ok=True)
    log_info(f"Created directory: {day_dir}")
    
    # Download and save input
    input_file = day_dir / "input"
    if not input_file.exists():
        log_info(f"Downloading input for day {day} ({year})...")
        input_data = get_input(day, year)
        input_file.write_text(input_data)
        log_success(f"Saved input to {input_file}")
    else:
        log_info(f"Input file already exists: {input_file}")

    # Create test file if it doesn't exist
    test_file = day_dir / "test"
    if not test_file.exists():
        test_file.touch()
        log_success(f"Created test file: {test_file}")
    else:
        log_info(f"Test file already exists: {test_file}")
    
    # Create solution file if it doesn't exist
    solution_file = day_dir / "main.py"
    if not solution_file.exists():
        log_info(f"Creating solution file: {solution_file}")
        solution_file.write_text(solution_template)
        log_success(f"Created solution file: {solution_file}")
    else:
        log_info(f"Solution file already exists: {solution_file}")

if __name__ == "__main__":
    main()
