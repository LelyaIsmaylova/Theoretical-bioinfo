def safe_fasta(file_name, seq_dict):               # функция записывает идентификатор и последовательность каждого элемента из словаря в файл
    with open(file_name, 'w') as file:
        for seq_id, seq in seq_dict.items():
            file.write('>' + seq_id + '\n')           # элемент начнется с символа >, один на строку
            file.write(seq + '\n')
