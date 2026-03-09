import operator
PEOPLE = [('Donald', 'Trump', 7.85),('Vladimir', 'Putin', 3.626),('Jinping', 'Xi', 10.603)]
def format_sort_records(list_of_tuples):
    
    output=[]
    template="{1:10}{0:10}{2:5.2f}" #форматировани
    for person in sorted(list_of_tuples, key=operator.itemgetter(1,0)):
        output.append(template.format(*person))
    return output


    
print('\n'.join(format_sort_records(PEOPLE)))
import collections
PEOPLE = [('Donald', 'Trump', 7.85),('Vladimir', 'Putin', 3.626),('Jinping', 'Xi', 10.603)]
def format_sort_records(list_of_tuples):
    Person = collections.namedtuple('Person', 'first_name last_name time')
    people = [Person(*t) for t in list_of_tuples]
    sorted_people = sorted(people, key=lambda p: (p.last_name, p.first_name))

    result_lines = []
    for person in sorted_people:
        line = f"{person.last_name:10} {person.first_name:10}{person.time:8.2f}"
        result_lines.append(line)

    return '\n'.join(result_lines)

# Использование
output = format_sort_records(PEOPLE)
print(output)

OSCAR_NOMINATIONS_2024 = [
    ("Оппенгеймер", 180, "Кристофер Нолан"),
    ("Барби", 114, "Грета Гервиг"),
    ("Убийцы цветочной луны", 206, "Мартин Скорсезе"),
    ("Бедные‑несчастные", 141, "Йоргос Лантимос"),
    ("Оставленные", 139, "Александр Пэйн"),
    ("Маэстро", 129, "Брэдли Купер"),
    ("Зона интересов", 105, "Джонатан Глейзер"),
    ("Анатомия падения", 151, "Жюстин Трие"),
    ("Прошлым летом", 116, "Мишель Франко"),
    ("Американское чтиво", 111, "Корд Джефферсон")
]
'''
def format_sort_films(list_of_tuples):
    Films = collections.namedtuple('Films', 'name time director')
    film = [Films(*t) for t in list_of_tuples]
    sort_type=1
    while sort_type>0 :     
        sort_type=int(input("Введите тип сортировки: 1 - Film, 2- Time, 3 - Director, 0- выхода: "))
        print(sort_type)
        if sort_type == 1:
            sorted_films = sorted(film, key=lambda p: (p.name))
            sort_type=0

        elif sort_type==2:
            sorted_films = sorted(film, key=lambda p: (p.time))
            sort_type=0
        elif sort_type==3:
            sorted_films = sorted(film, key=lambda p: (p.director)) 
            sort_type=0  
    print(sorted_films)   
    result_lines_films = []
    for films in sorted_films:
        line = f"{films.name:25} {films.time:10} {films.director:20}"
        result_lines_films.append(line)

    return '\n'.join(result_lines_films)
output = format_sort_films(OSCAR_NOMINATIONS_2024)
print(output)
'''
def format_sort_films_new(list_of_tuples):
    Films = collections.namedtuple('Films', 'name time director')
    film = [Films(*t) for t in list_of_tuples]
    sort_types = ['name', 'time', 'director']

    while True:
        sort_type = input("Введите тип сортировки (через запятую можно ввести несколько видов сортировки): 1 — Name, 2 — Time, 3 — Director, 0 — выход: ")
        if sort_type == '0':
            break

        # Преобразуем ввод в список индексов и проверяем корректность
        try:
            sort_indices = list(map(int, sort_type.split(',')))
            # Проверяем, что все индексы в допустимом диапазоне
            if not all(0 < idx <= 3 for idx in sort_indices):
                print("Ошибка: допустимые значения — 1, 2, 3.")
                continue
            # Преобразуем индексы в названия атрибутов (вычитаем 1 для соответствия индексам списка)
            attributes = [sort_types[idx - 1] for idx in sort_indices]
        except ValueError:
            print("Ошибка: введите числа через запятую.")
            continue

        # Сортируем по указанным атрибутам
        sorted_films = sorted(film, key=lambda p: tuple(getattr(p, attr) for attr in attributes))
        break

    result_lines_films = []
    for films in sorted_films:
        line = f"{films.name:25} {films.time:10} {films.director:20}"
        result_lines_films.append(line)

    return '\n'.join(result_lines_films)
output = format_sort_films_new(OSCAR_NOMINATIONS_2024)
print(output)

