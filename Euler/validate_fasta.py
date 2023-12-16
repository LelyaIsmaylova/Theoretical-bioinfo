def validate_fasta(sequences, k):
    valid_nucleotides = {'A', 'T', 'G', 'C'}
    for seq in sequences:
        if len(seq) != k:
            return False, f"Последовательность '{seq}' не является строкой длины {k}."
        if not all(nucleotide in valid_nucleotides for nucleotide in seq):
            return False, f"Последовательность '{seq}' содержит недопустимые элементы (буквы)."
    return True, "Проверка прошла успешно."
