import os

def process_text():
    input_file = "input.txt"
    output_file = "result.txt"

    # Создаем файл, если его нет
    if not os.path.exists(input_file):
        with open(input_file, "w", encoding="utf-8") as f:
            f.write("Hello world! This is a test file for Git lab.")

    # Читаем и считаем слова
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
            words = content.split()
            word_count = len(words)

        # Записываем результат
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Words count: {word_count}")
        
        print(f"Обработка завершена. Найдено слов: {word_count}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    process_text()