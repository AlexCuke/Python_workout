def file_open_str(filename):
    """Открытие файла построчно"""
    import re
    with open(filename, 'r',  encoding='windows-1251') as f:
        # readlines() читает все строки и возвращает их списком
        content = f.read() 
        # Удаляем все числовые HTML-сущности
        cleaned = re.sub(r'&#\d+;', '', content)
        # Удаляем спецсимволы, сохраняя буквы, цифры, пробелы и дефисы
        cleaned = re.sub(r'[^\w\s-]', '', cleaned)
        # Нормализуем пробелы: несколько → один
        cleaned = re.sub(r'\s+', ' ', cleaned)
        
        # Убираем пробелы по краям и разбиваем на слова
        content_list = cleaned.strip().split(' ')
        return content_list

import os       

def find_longest_word(filename):
    """функции. find_longest_
word принимает в качестве аргумента имя файла и возвращает
самое длинное слово, найденное в файл""" 
    import operator
    content=file_open_str(filename)
    longest_word=''
    for word in content:
        if 'http' not in word:
            if len(word) > len (longest_word):
                longest_word = word
            
    return longest_word   

BOOKNAME='Толстой Лев. Война и мир.txt'
print(f'Самое длинное сллово - {find_longest_word(BOOKNAME)}')

def find_all_longest_words(dirname):
    """функция, fi nd_
all_longest_words, принимает имя каталога и возвращает
словарь, в котором ключами являются имена файлов, а значени-
ями — самые длинные слова из каждого файла."""
    return {filename: find_longest_word(os.path.join(dirname, filename))
    for filename in os.listdir(dirname)
    if os.path.isfile(os.path.join (dirname, filename))}
print(find_all_longest_words('.'))