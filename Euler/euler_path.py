def euler_path(nodes, links):
adj_list  = {}

for node, link in nodes, links:
    if node in adj_list:
        adj_list[node].append(link)
    else:
        adj_list[node] = [link]

in_degree = {}
out_degree = {}

for node in adj_list:
    out_degree[node] = len(adj_list[node])
    
    for dest in adj_list[node]:
        if dest in in_degree:
            in_degree[dest] += 1
        else:
            in_degree[dest] = 1

start = nodes[0] 

count_of_start = 0
count_of_end = 0

for node in nodes:
    if node in out_degree:
        if out_degree[node] - in_degree[node] > 0:
            start = node
            count_of_start += 1
        elif out_degree[node] - in_degree[node] < 0:
            end = node
            count_of_end += 1

if count_of_start != 1 or count_of_end != 1:
    return "Euler path does not exist"

current_node = start 
stack = []
path = []

while len(path) != len(links):
    if current_node not in adj_list or len(adj_list[current_node]) == 0:
        path.append(current_node)
        current_node = stack.pop()
    else:
        stack.append(current_node)
        next_node = adj_list[current_node].pop()
        current_node = next_node

path.append(current_node)

return path[::-1]
