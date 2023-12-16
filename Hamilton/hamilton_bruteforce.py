import itertools

class HamiltonPathImpossible(Exception):
    pass

def hamilton_bruteforce(nodes, links):
    n = len(nodes)
    path_options = list(itertools.permutations(nodes, n))
    path = 'No path'
    choice_count = 0
    for i in range(len(path_options)):
        curr_path = path_options[i]
        choice_count = 0
        #print(curr_path)
        for j in range(n-1):
            if (curr_path[j], curr_path[j+1]) in links:
                pass
                #print(curr_path[j], curr_path[j+1])
                choice_count +=1
            else:
                break
            #print('choice_count =',  choice_count)
            if choice_count == n-1:
                path = curr_path
    if path == 'No path':
        raise HamiltonPathImpossible
    return(path)
