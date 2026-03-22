import os
def count_lines_in_file(file_path):
    """Подсчитывает количество строк в файле."""
    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for line in f)

def merge_files(file_names, output_file_name):
    
    files_info = []
    for file_name in file_names:
        line_count = count_lines_in_file(file_name)
        files_info.append((file_name, line_count))

    files_info.sort(key=lambda x: x[1])

    with open(output_file_name, "w", encoding="utf-8") as output_file:
        for file_name, line_count in files_info:
            output_file.write(f"{file_name}\n")
            output_file.write(f"{line_count}\n")
            with open(file_name, "r", encoding="utf-8") as input_file:
                for line in input_file:
                    output_file.write(line)

if __name__ == "__main__":
    files = ["1.txt", "2.txt", "3.txt"]
    output_file = "result.txt"

    merge_files(files, output_file)
    print(f"Файлы объединены в {output_file}")
