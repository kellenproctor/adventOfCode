def get_destination(seed, block):
    answer = seed
    for line in block[1:]:
        dest, start, length = line.split(" ")
        difference = int(dest) - int(start)
        if int(start) <= seed <= (int(start) + int(length)):
            answer = seed + difference
            break
        else:
            answer = seed
    return answer

def part1(data):
    blocks = [block for block in data.split("\n\n")]
    seeds = [int(seed) for seed in blocks[0].lstrip("seeds: ").split(" ")]
    mappings = [line.split("\n") for line in blocks[1:]]
    location = []
    for seed in seeds:
        for mapping in mappings:
            dest = get_destination(seed, mapping)
            seed = dest
        location.append(seed)
    return min(location)

def get_range_mappings(start, length, block):
    # Input range: [start, start+length)
    ranges_to_check = [(start, start + length)]
    mapped_ranges = []
    
    # Process each mapping rule
    for line in block[1:]:
        dest, source, map_len = map(int, line.split())
        source_end = source + map_len
        difference = dest - source
        
        remaining_ranges = []
        
        # Process each range against current mapping rule
        while ranges_to_check:
            range_start, range_end = ranges_to_check.pop()
            
            # Calculate overlap
            overlap_start = max(range_start, source)
            overlap_end = min(range_end, source_end)
            
            if overlap_start < overlap_end:
                # Map the overlapping portion
                mapped_ranges.append((overlap_start + difference, overlap_end + difference))
                
                # Keep the non-overlapping portions to check against other rules
                if range_start < overlap_start:
                    remaining_ranges.append((range_start, overlap_start))
                if overlap_end < range_end:
                    remaining_ranges.append((overlap_end, range_end))
            else:
                # No overlap, keep the range as is
                remaining_ranges.append((range_start, range_end))
                
        ranges_to_check = remaining_ranges
    
    # Any remaining ranges weren't mapped by any rule, so keep them as is
    return mapped_ranges + ranges_to_check


def part2(data):
    blocks = [block for block in data.split("\n\n")]
    seeds = [int(seed) for seed in blocks[0].lstrip("seeds: ").split(" ")]
    mappings = [line.split("\n") for line in blocks[1:]]

    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    
    # Process each mapping level
    for mapping in mappings:
        new_ranges = []
        for start, end in ranges:
            mapped = get_range_mappings(start, end - start, mapping)
            new_ranges.extend(mapped)
        ranges = new_ranges
    
    return min(start for start, _ in ranges)

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
