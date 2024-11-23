def main(data):
    instructions, nodes = data.split("\n\n")
    nodes = nodes.strip().split("\n")

    start = "AAA"
    graph = {}
    for node in nodes:
        key, rest = node.split(" = ")
        n = tuple(item.strip() for item in rest.strip("()").split(","))
        graph[key] = n

    found = False
    count = 0
    while not found:
        for d in instructions:
            if start == "ZZZ":
                found = True
                break
            if d == "L":
                start = graph[start][0]
                count += 1
            else:
                start = graph[start][1]
                count += 1
    return count


if __name__ == "__main__":
    data = open(0).read()
    print(f"{main(data)}")
