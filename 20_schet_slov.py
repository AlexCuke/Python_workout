def wordcount(filename):
    """Функция будет принимать
на вход имя файла и печатать четыре строки вывода:
1 Количество символов (включая пробельные символы).
2 Количество слов (разделенных пробелами).
3 Количество линий.
4 Количество уникальных слов ("""
    
    counts = {'characters': 0,
    'words': 0,
    'lines': 0}
    unique_words = set()
    for one_line in open(filename):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_words.update(one_line.split())
    counts['unique_words'] = len(unique_words)
    for key, value in counts.items ():
       print(f'{key}: {value}')
wordcount('wcfile.txt')

def wordcount_v2():
    """Попросите пользователя ввести имя текстового файла, а за-
тем (в одной строке, разделенной пробелами) слова, ча-
стота которых должна быть подсчитана в этом файле. Под-
считайте, сколько раз эти слова встречаются в словаре,
используя введенные пользователем слова в качестве клю-
чей, а подсчеты (counts) — в качестве значений."""
    #input_str=input("Введите имя файла и слово, частота которое должно быть посчитано ")
    input_str='Толстой Лев. Война и мир.txt мир'
    medium_str=input_str.split(' ')
    word=medium_str[-1]
    filename=input_str[:-len(word)]
    word=medium_str[-1]
    print(word)
    count={word:0}
    for one_line in open(filename):
        if word in one_line:
            count[word] += len(one_line.split())
    print(f'{count}')
wordcount_v2()
import os

def stat_file(catalog):
    """
    Создайте словарь, в котором ключами будут имена файлов
    в вашей системе, а значениями — размеры этих файлов.
    Для вычисления размера можно использовать os.stat.
    """
    file_sizes = {}
    
    # Проверяем, существует ли каталог и является ли он каталогом
    if not os.path.exists(catalog):
        print(f"Каталог '{catalog}' не существует.")
        return file_sizes
    if not os.path.isdir(catalog):
        print(f"'{catalog}' не является каталогом.")
        return file_sizes

    try:
        # Перебираем все элементы в каталоге
        for filename in os.listdir(catalog):
            # Создаём полный путь к файлу/каталогу
            filepath = os.path.join(catalog, filename)
            
            # Проверяем, что это файл (а не подкаталог)
            if os.path.isfile(filepath):
                # Получаем размер файла через os.stat
                file_stat = os.stat(filepath)
                file_sizes[filename] = file_stat.st_size
    except PermissionError:
        print(f"Нет доступа к каталогу '{catalog}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    return file_sizes

# Исправленный путь — используем сырую строку
catalog = r'C:\Users\Alex\Desktop\!REPOSITORIES\Python_workout-1'
result = stat_file(catalog)
print(result)
print('')
print('')
import re
import sys
import os
def stat_file_keys(catalog):
    """В заданном каталоге прочитайте каждый файл и подсчи-
тайте частоту встречаемости каждой буквы. (Сделайте
буквы строчными и игнорируйте небуквенные символы.)
Используйте словарь для отслеживания частоты букв. Ка-
кие пять букв наиболее часто встречаются во всех этих
файлах?"""
    file_sizes = {}
    #keys='абвгдеёжзиклмнопрстуфхцчшщэюяabcdefghiklmnopqrstuvwxyz'
    keys='абвгдеёжзиклмнопрстуфхцчшщэюя'

    keys_dict=[]
    for key in keys:
        keys_dict.append(key)    
    count=dict.fromkeys(keys_dict,0)
    # Проверяем, существует ли каталог и является ли он каталогом
    if not os.path.exists(catalog):
        print(f"Каталог '{catalog}' не существует.")
        return file_sizes
    if not os.path.isdir(catalog):
        print(f"'{catalog}' не является каталогом.")
        return file_sizes

    try:
        # Перебираем все элементы в каталоге
        for filename in os.listdir(catalog):
            # Создаём полный путь к файлу/каталогу
            filepath = os.path.join(catalog, filename) 
            # Проверяем, что это файл (а не подкаталог)
            if os.path.isfile(filepath):
                with open(filename, 'r',encoding='utf-8',errors='ignore') as file:
                    content=file.read()
                    content=content.lower()
                    for symbols in content:
                        if symbols in keys:
                            count[symbols]+=1
        
    except PermissionError:
        print(f"Нет доступа к каталогу '{catalog}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e} {filename}")
    sorted_dict_desc = dict(sorted(count.items(), key=lambda x: x[1], reverse=True)[:5])

    return sorted_dict_desc

# Исправленный путь — используем сырую строку
catalog =r'C:\Users\Alex\Desktop\!REPOSITORIES\Python_workout-1'
result = stat_file_keys(catalog)
print(result)