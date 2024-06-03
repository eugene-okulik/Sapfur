import os


def main():
    file_path = input('Введите полный путь к папке, в которой лежат файлы с логами: ')

    if not os.path.isdir(file_path):
        print(f"Error: '{file_path}' is not a valid directory.")
        return

    dir_list = os.listdir(file_path)
    if not dir_list:
        print(f"No files found in directory '{file_path}'.")
        return

    print(dir_list)
    text_to_find = input('Введите текст который нужно найти в файлах: ')

    for file_name in dir_list:
        file_text = os.path.join(file_path, file_name)

        if not os.path.isfile(file_text):
            continue

        try:
            with open(file_text, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, 1):
                    if text_to_find in line:
                        print(f'Найдено в файле: {file_name}. Порядковый номер строки файла: {line_number}')
                        index = line.find(text_to_find)
                        start = max(0, index - 5)
                        end = min(len(line), index + len(text_to_find) + 5)
                        print(line[start:end].strip())
        except Exception as e:
            print(f"Error reading file '{file_text}': {e}")


if __name__ == "__main__":
    main()