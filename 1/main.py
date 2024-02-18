import os


def copy_line(source_file, dest_file, line_number):

    if not os.path.exists(source_file):
        print(f"Ошибка: файл '{source_file}' не найден.")
        return
    if not os.path.exists(dest_file):
        print(f"Ошибка: файл '{dest_file}' не найден.")
        return

    with open(source_file, 'r') as f:
        lines = f.readlines()
    if line_number > len(lines):
        print(f"Ошибка: номер строки '{line_number}' больше, чем количество строк в файле.")
        return
    line = lines[line_number - 1]

    with open(dest_file, 'a') as f:
        f.write(line)

    print(f"Строка {line_number} из '{source_file}' успешно скопирована в '{dest_file}'.")


source_file = "source.txt"
dest_file = "destination.txt"
line_number = int(input('Введите номер строки, которую нужно скопировать: '))

copy_line(source_file, dest_file, line_number)
