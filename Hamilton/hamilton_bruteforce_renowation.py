class HamiltonPathImpossible(Exception):
    pass

def hamilton_dynamic(nodes, links):
    n = len(nodes)
    path_cost = {}
    path = 'No path'
    for node in nodes:
        path_cost[(node,)] = 0
    for i in range(1, n):
        next_path_cost = {}
        for subset in itertools.permutations(nodes, i+1):
            for node in nodes:
                if node not in subset:
                    continue
                prev_subset = tuple([x for x in subset if x != node])
                min_cost = float('inf')
                for j in prev_subset:
                    if (j, node) in links and prev_subset in path_cost:
                        min_cost = min(min_cost, path_cost[prev_subset])
                if min_cost != float('inf'):
                    next_path_cost[subset] = min_cost + 1
        path_cost = next_path_cost
    for subset in itertools.permutations(nodes, n):
        if subset in path_cost and (subset[-1], subset[0]) in links:
            path = subset
            break
    if path == 'No path':
        raise HamiltonPathImpossible
    return path
