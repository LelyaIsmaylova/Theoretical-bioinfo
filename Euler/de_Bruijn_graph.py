def build_de_bruijn_graph(sequences, k):
    edges = defaultdict(int)
    for seq in sequences:
        for i in range(len(seq) - k + 1):
            kmer1 = seq[i:i+k-1]
            kmer2 = seq[i+1:i+k]
            edges[(kmer1, kmer2)] += 1
    return edges
