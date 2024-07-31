class WordsFinder:
    def __init__(self, *file_names):
        # Сохранение имён файлов в атрибут
        self.file_names = file_names

    def get_all_words(self):
        # Пустой словарь для хранения всех слов
        all_words = {}

        # Перебор всех переданных файлов
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Чтение содержимого файла и всё в нижний регистр
                    content = file.read().lower()

                    # Удаление пунктуации
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, '')

                    # Разделение строк на слова
                    words = content.split()

                    # Полученные слова пишем в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                # Если файл не найден - пустой список
                all_words[file_name] = []

        return all_words

    def find(self, word):
        word = word.lower()  # Найденное слово в нижний регистр
        word_positions = {}
        all_words = self.get_all_words()  # Все слова из файлов

        for file_name, words in all_words.items():
            try:
                # Позиция первого слова из списка слов
                position = words.index(word)
            except ValueError:
                # Если слово не найдено - None
                position = None

            word_positions[file_name] = position

        return word_positions

    def count(self, word):
        word = word.lower()  # Переводим искомое слово в нижний регистр
        word_count = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            # Подсчёт количества слов в списке слов
            count = words.count(word)
            word_count[file_name] = count

        return word_count


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
