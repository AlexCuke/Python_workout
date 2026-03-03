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
        return Counter(word).most_common(1)[0][1]

def most_repeating_word(words):
    return max(words,key=most_repeating_letter_count)

result = most_repeating_word(WORDS)
print(result)

def most_repeating_vowel_count(word):
    # Определяем множество гласных (английских), включая заглавные и строчные
    vowels = set('aeiouAEIOU')
    # Оставляем только гласные из слова
    vowel_letters = [letter for letter in word if letter in vowels]
    # Если гласных нет, возвращаем 0
    if not vowel_letters:
        return 0
    # Считаем частоту каждой гласной и возвращаем максимальную
    return Counter(vowel_letters).most_common(1)[0][1]

def most_repeating_vowel_word(words):
    # Находим слово с максимальным количеством повторяющихся гласных
    return max(words, key=most_repeating_vowel_count)

# Пример использования
WORDS = ['beautiful', 'queue', 'strength', 'aardvark', 'rhythm']
result = most_repeating_vowel_word(WORDS)
print(result)  # Вывод: 'queue' (в этом слове буква 'u' повторяется 3 раза)
from collections import Counter

def analyze_passwd():
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