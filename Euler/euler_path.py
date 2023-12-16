def find_eulerian_path(edges):
    graph = defaultdict(list)
    degrees = defaultdict(int)
    for (a, b), count in edges.items():
        graph[a].append(b)
        degrees[a] -= count
        degrees[b] += count

    start = next(node for node, degree in degrees.items() if degree < 0)
    end = next(node for node, degree in degrees.items() if degree > 0)

    stack = [start]
    path = deque()
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            path.appendleft(stack.pop())

    return ''.join([path[0]] + [node[-1] for node in list(path)[1:]])
