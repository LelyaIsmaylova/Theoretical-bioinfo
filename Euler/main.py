print('Enter title \n >')
title = str(input())

print('Enter file name ')
file_name = str(input())

if file_name == '': 
    file_name = 'New file'
  
if title == '': 
    title = head + ' assembled '

create_fasta(file_name, genome, title )
