from collections import defaultdict, deque

def validate_fasta(sequences, k):
    valid_nucleotides = {'A', 'T', 'G', 'C'}
    for seq in sequences:
        if not all(nucleotide in valid_nucleotides for nucleotide in seq) and len(seq) != k:
            return False, f"Последовательность '{seq}' совсем плоха (содержит недопустимые элементы И не является строкой длины {k})."
        if not all(nucleotide in valid_nucleotides for nucleotide in seq):
            return False, f"Последовательность '{seq}' содержит недопустимые элементы (буквы)."
        if len(seq) != k:
            return False, f"Последовательность '{seq}' не является строкой длины {k}."
    return True, "Проверка прошла успешно."


def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

def build_de_bruijn_graph(sequences, k):
    edges = defaultdict(int)
    for seq in sequences:
        for i in range(len(seq) - k + 1):
            kmer1 = seq[i:i+k-1]
            kmer2 = seq[i+1:i+k]
            edges[(kmer1, kmer2)] += 1
    return edges

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


def assemble_genome(sequences, k):
    de_bruijn_graph = build_de_bruijn_graph(sequences, k)
    return find_eulerian_path(de_bruijn_graph)

def can_build_de_bruijn_graph(edges):
    degrees = defaultdict(int)
    for (a, b), count in edges.items():
        degrees[a] -= count
        degrees[b] += count

    start_nodes = sum(1 for degree in degrees.values() if degree < 0)
    end_nodes = sum(1 for degree in degrees.values() if degree > 0)

    return start_nodes <= 1 and end_nodes <= 1

file_path = 'example.fa'

k = 4
sequences = read_fasta(file_path)

valid, message = validate_fasta(sequences, k)
print(valid, message)

de_bruijn_graph = build_de_bruijn_graph(sequences, k)

valid2 = False

if can_build_de_bruijn_graph(de_bruijn_graph):
    print("Проверка возможности построения графа де Брейна пройдена успешно.")
    valid2 = True
    
else:
    print("Проверка возможности построения графа де Брейна не пройдена.")

if valid and valid2:
    assembled_genome = assemble_genome(sequences, k)
    with open('final.fa', 'w') as file:
        file.write('>out\n' + assembled_genome)
