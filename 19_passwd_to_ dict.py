def passwd_to_dict(filename):
    """Преобразует файл passwd в словарь, где ключ — имя пользователя,
    а значение — словарь с информацией о пользователе."""
    users = {}
    with open(filename, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            # Пропускаем комментарии (начинаются с #) и пустые строки
            line = line.strip()  # Убираем пробелы и символы переноса в начале/конце
            if not line or line.startswith('#'):
                continue

            # Разделяем строку по символу :
            user_info = line.split(':')

            # Проверяем, что строка содержит достаточно полей (минимум 3)
            if len(user_info) < 3:
                continue  # Пропускаем некорректные строки

            username = user_info[0]
            userid = user_info[2]

            # Сохраняем в словарь: ключ — имя пользователя, значение — ID пользователя
            users[username] = userid

    return users

# Использование
filename1 = 'passwd.txt'
result = passwd_to_dict(filename1)
print(result)

def passwd_to_dict_ver_2(filename):
    """Преобразует файл passwd в словарь, где ключ — имя пользователя,
    а значение — словарь с информацией о пользователе."""
    users = {}
    with open(filename, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            # Пропускаем комментарии (начинаются с #) и пустые строки
            line = line.strip()  # Убираем пробелы и символы переноса в начале/конце
            if not line or line.startswith('#'):
                continue

            # Разделяем строку по символу :
            user_info = line.split(':')

            # Проверяем, что строка содержит достаточно полей (минимум 3)
            if len(user_info) < 3:
                continue  # Пропускаем некорректные строки

            username = str(user_info[-1:])
            print(username)
            userid = user_info[0]

            # Сохраняем в словарь: ключ — имя пользователя, значение — ID пользователя
            value=users.get(username,[])
            value.append(userid)
            users[username] = value

    return users

# Использование
filename1 = 'passwd.txt'
result = passwd_to_dict_ver_2(filename1)
print(result)

def chisla_probel():
    """Прочитайте текстовый файл, строка за строкой С помо-
щью словаря подсчитайте, сколько раз каждая гласная (a, e,
i, o и u) встречается в файле. Распечатайте полученную та-
блицу."""
    # Шаг 1: Получаем ввод от пользователя
    user_input = input("Введите целые числа, разделённые пробелами: ")

    # Шаг 2: Преобразуем ввод в список целых чисел
    numbers = list(map(int, user_input.split()))

    # Проверяем, что ввод не пустой
    if not numbers:
        print("Вы не ввели ни одного числа.")
    else:
        # Шаг 3: Определяем диапазон коэффициентов (от 2 до max(numbers))
        max_num = max(numbers)
        coefficients = range(2, max_num + 1)

        # Шаг 4–5: Создаём словарь с коэффициентами и списками кратных чисел
        result_dict = {}
        for coeff in coefficients:
            multiples = [num for num in numbers if num % coeff == 0]
            # Добавляем в словарь только если есть кратные числа
            if multiples:
                result_dict[coeff] = multiples

        # Шаг 6: Выводим результат
        if result_dict:
            print("\nСловарь коэффициентов и кратных им чисел:")
            for coeff, multiples in sorted(result_dict.items()):
                print(f"Коэффициент {coeff}: {multiples}")
        else:
            print("Среди введённых чисел нет кратных ни одному коэффициенту (от 2 до максимального числа).")
            
        
        
def passwd_to_dict(filename):
    """Из /etc/passwd создайте словарь, в котором ключами
будут имена пользователей (как в основном упражнении),
а значениями — сами словари с ключами (и соответствую-
щими значениями) для ID пользователя, домашнего ката-
лога и оболочки."""
    users = {}
    with open(filename, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            # Пропускаем комментарии (начинаются с #) и пустые строки
            line = line.strip()  # Убираем пробелы и символы переноса в начале/конце
            if not line or line.startswith('#'):
                continue

            # Разделяем строку по символу :
            user_info = line.split(':')

            # Проверяем, что строка содержит достаточно полей (минимум 3)
            if len(user_info) < 3:
                continue  # Пропускаем некорректные строки

            username = user_info[0]
            userid = user_info[2]

            # Сохраняем в словарь: ключ — имя пользователя, значение — ID пользователя
            users[username] = userid

    return users
