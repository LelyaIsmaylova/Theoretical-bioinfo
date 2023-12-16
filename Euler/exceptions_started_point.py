def can_build_de_bruijn_graph(edges):
    degrees = defaultdict(int)
    for (a, b), count in edges.items():
        degrees[a] -= count
        degrees[b] += count

    start_nodes = sum(1 for degree in degrees.values() if degree < 0)
    end_nodes = sum(1 for degree in degrees.values() if degree > 0)

    return start_nodes <= 1 and end_nodes <= 1
