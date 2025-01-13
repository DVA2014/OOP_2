import os

def rewriting(file_list, outut_file):
    file_info = []
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            file_info.append((file_name, len(lines), lines))

    file_info.sort(key=lambda x: x[1])
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, lines in file_info:
            out_file.write(f"{file_name}\n{line_count}\n")
            out_file.writelines(lines)
            if not lines[-1].endswith('\n'):
                out_file.write('\n')

file_list = ['1.txt', '2.txt', '3.txt']
output_file = 'result.txt'
rewriting(file_list, output_file)