from collections import defaultdict, deque
import validate_fasta as val
import read_fasta as read
import de_bruijn_graph as bg
import eulerian_path as ep
import can_build as cb

def assemble_genome(sequences, k):
    de_bruijn_graph = bg.build_de_bruijn_graph(sequences, k)
    return ep.find_eulerian_path(de_bruijn_graph)

file_path = 'example.fa'

k = 4
sequences = read.read_fasta(file_path)

valid, message = val.validate_fasta(sequences, k)
print(valid, message)

de_bruijn_graph = bg.build_de_bruijn_graph(sequences, k)

valid2 = False

if cb.can_build_de_bruijn_graph(de_bruijn_graph):
    print("Проверка возможности построения графа де Брейна пройдена успешно.")
    valid2 = True

else:
    print("Проверка возможности построения графа де Брейна не пройдена.")

if valid and valid2:
    assembled_genome = assemble_genome(sequences, k)
    with open('final.fa', 'w') as file:
        file.write('>\n' + assembled_genome)
