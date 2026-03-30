file_names = ["1.txt", "2.txt", "3.txt"]

output_file = "result.txt"

print("=== НАЧИНАЕМ ОБЪЕДИНЕНИЕ ФАЙЛОВ ===")
print(f"Найдено файлов: {len(file_names)}")
print(f"Список файлов: {file_names}")
print()

files_info = []

for name in file_names:
    try:
        file = open(name, "r", encoding="utf-8")

        line_count = 0
        for line in file:
            line_count = line_count + 1

        file.close()
        files_info.append([name, line_count])
        print(f"✓ Файл {name} содержит {line_count} строк(и)")

    except FileNotFoundError:
        print(f"✗ ОШИБКА: Файл {name} не найден!")
        print(f"  Убедитесь, что файл {name} находится в той же папке.")

print()
print(f"Обработано файлов: {len(files_info)}")
print()

for i in range(len(files_info)):
    for j in range(len(files_info) - 1 - i):
        if files_info[j][1] > files_info[j + 1][1]:
            temp = files_info[j]
            files_info[j] = files_info[j + 1]
            files_info[j + 1] = temp

print("Файлы после сортировки (от меньшего к большему):")
for name, count in files_info:
    print(f"  {name} - {count} строк(и)")
print()

output = open(output_file, "w", encoding="utf-8")
written_count = 0

for name, count in files_info:
    output.write(name + "\n")
    output.write(str(count) + "\n")
    input_file = open(name, "r", encoding="utf-8")

    for line in input_file:
        output.write(line)

    input_file.close()

    written_count = written_count + 1
    print(
        f"✓ Файл {name} добавлен в результат "
        f"(записано {written_count} из {len(files_info)})"
    )
output.close()

print()
print("=== ГОТОВО! ===")
print(f"Все {written_count} файлов объединены в {output_file}")

print()
print("--- СОДЕРЖИМОЕ ИТОГОВОГО ФАЙЛА ---")

try:
    rezult_file = open(output_file, "r", encoding="utf-8")
    line_number = 1
    for line in rezult_file:
        print(f"{line_number:2}. {line}", end="")
        line_number = line_number + 1
    rezult_file.close()
except FileNotFoundError:
    print(f"Файл {output_file} не создан, возможно произошла ошибка.")
