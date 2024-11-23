grid = list()

with open("test") as f:
    for line in f:
        grid.append(line.rstrip())
        
cs = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for cr in [r-1, r, r+1]:
            for cc in [c-1,c,c+1]:
                if 0 < cr >= len(grid) or 0 < cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                cs.add((cr, cc))

ns = []

for r, c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))