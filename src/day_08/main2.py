from math import lcm

def main(data):
    instructions, nodes = data.split("\n\n")
    nodes = nodes.strip().split("\n")

    start = []
    cycle = []
    graph = {}
    for node in nodes:
        key, rest = node.split(" = ")
        n = tuple(item.strip() for item in rest.strip("()").split(","))
        graph[key] = n
        if key[2] == "A":
            start.append(key)
    print(start)

    count = 0
    while start:
        for d in instructions:
            if d == "L":
                start = [graph[k][0] for k in start]
            else:
                start = [graph[k][1] for k in start]
            count += 1
            for k in start:
                if k[2] == "Z":
                    start.remove(k)
                    cycle.append(count)
    return lcm(*cycle)


if __name__ == "__main__":
    data = open(0).read()
    print(f"{main(data)}")
