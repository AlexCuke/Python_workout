from operator import itemgetter
from collections import Counter

PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
            {'first':'Donald', 'last':'Trump',
                'email':'president@whitehouse.gov'},
            {'first':'Vladimir', 'last':'Putin',
                'email':'president@kremvax.ru'}
            ]

WORDS=['this','is','elementary','test','example']
def most_repeating_letter_count(word):
    """Функция должна возвращать строку, содержащую наибольшее количество повторяющихся букв
    """
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(words):
    """Функция должна возвращать строку, содержащую наибольшее количество повторяющихся слов
    """
    return max(words,key=most_repeating_letter_count)

result = most_repeating_word(WORDS)
print(result)

def most_repeating_vowel_count(word):
    """Вместо того, чтобы искать слово с наибольшим количе-
ством повторяющихся букв, найдите слово с наибольшим
количеством повторяющихся гласных. Поиск в слове
    """
    # Определяем множество гласных (английских), включая заглавные и строчные
    vowels = set('aeiouAEIOU')
    # Оставляем только гласные из слова
    vowel_letters = [letter for letter in word if letter in vowels]
    # Если гласных нет, возвращаем 0
    if not vowel_letters:
        return 0
    # Считаем частоту каждой гласной и возвращаем максимальную
    return Counter(vowel_letters).most_common(1)[0][1]

def most_repeating_vowel_word_v2(words):
    """Вместо того, чтобы искать слово с наибольшим количе-
ством повторяющихся букв, найдите слово с наибольшим
количеством повторяющихся гласных.
    """
    
    return max(words, key=most_repeating_vowel_count)

# Пример использования
WORDS = ['beautiful', 'queue', 'strength', 'aardvark', 'rhythm']
result = most_repeating_vowel_word_v2(WORDS)
print(result)  # Вывод: 'queue' (в этом слове буква 'u' повторяется 3 раза)
from collections import Counter

def analyze_passwd():
    """Напишите программу для чтения /etc/passwd на компью-
тере Unix. Первое поле содержит имя пользователя, а по-
следнее — оболочку пользователя, командный интерпрета-
тор. Выведите оболочки в порядке убывания популярности
Какая буква встречается
чаще всего и сколько раз?
Counter.most_common возвращает список двухэлемент-
ных кортежей (value и count) в порядке убывания.
Точно так же, как вы можете передать ключ
в sorted, вы можете передать его в max и ис-
пользовать другой метод сортировки.
96 Лернер Реувен. Python-интенсив: 50 быстрых упражнений
так, чтобы самая популярная оболочка была показана пер-
вой, вторая по популярности — второй, и так далее
    """
    # Словарь для группировки пользователей по оболочкам
    shell_to_users = {}

    try:
        with open('/etc/passwd', 'r') as file:
            for line in file:
                # Пропускаем пустые строки и комментарии
                if not line.strip() or line.startswith('#'):
                    continue

                # Разделяем строку на поля по двоеточию
                fields = line.strip().split(':')

                # Первое поле — имя пользователя
                username = fields[0]
                # Последнее поле — оболочка
                shell = fields[-1]

                # Группируем пользователей по оболочкам
                if shell not in shell_to_users:
                    shell_to_users[shell] = []
                shell_to_users[shell].append(username)

        # Сортируем имена пользователей в каждой группе по алфавиту
        for shell in shell_to_users:
            shell_to_users[shell].sort()

        # Подсчитываем популярность оболочек
        shell_counter = Counter(shell_to_users.keys())

        # Выводим результаты в порядке убывания популярности
        print("Оболочки в порядке убывания популярности:")
        print("-" * 50)

        for shell, count in shell_counter.most_common():
            users = shell_to_users[shell]
            print(f"Оболочка: {shell}")
            print(f"Количество пользователей: {count}")
            print(f"Пользователи: {', '.join(users)}")
            print("-" * 50)

    except FileNotFoundError:
        print("Ошибка: файл /etc/passwd не найден.")
    except PermissionError:
        print("Ошибка: нет прав доступа к файлу /etc/passwd.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск анализа
analyze_passwd()

def analyze_passwd_v2():
    """НЕ ГОТОВО Для дополнительной сложности после отображения каж-
    дой оболочки также покажите имена пользователей (от-
    сортированные по алфавиту), которые используют каждую
    из этих оболочек"""