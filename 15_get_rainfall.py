'''import operator
MENU = {
    "Брускетта с томатами и базиликом": 350,
    "Тартар из лосося": 680,
    "Сырная тарелка с мёдом": 520,
    "Цезарь с курицей": 420,
    "Греческий салат": 380,
    "Салат с рукколой и пармской ветчиной": 490,
    "Луковый суп с гренками": 290,
    "Борщ с говядиной и сметаной": 320,
    "Тыквенный крем‑суп": 280,
    "Стейк Рибай с картофелем": 1200,
    "Лосось на гриле с овощами": 890,
    "Паста Карбонара": 550,
    "Тирамису": 360,
    "Шоколадный фондан": 390,
    "Чизкейк Нью‑Йорк": 370,
    "Американо": 180,
    "Латте": 220,
    "Морс клюквенный": 150,
    "Лимонад малиновый": 250
}
def restoraunt(menu):
    for dish in menu:
        print(f"{dish:30}: {menu[dish]:4} руб.")
    zakaz=0
    while True: 
        dish = input("Введите названпие блюда: ")
        if not dish:
            print(f"Общая сумма заказа: {zakaz} руб.")
            break
        else:
            if dish in menu.keys():
                zakaz=zakaz+menu[dish]
                print(f"Цена на {dish}: {menu[dish]} руб. Общая сумма заказа: {zakaz} руб.")
            elif dish not in menu.keys():
                print("Такого блюда нет в меню")
restoraunt(MENU)'''

'''USERS = {
    "ivan": "qwerty123",
    "maria": "password456",
    "alex": "mypass789",
    "olga": "secure000"
}

def descript(users):
    zakaz=0
    while True: 
        userpass = input("Введите имя пользователя и пароль через запятую ")
        userpass=userpass.split(",")
        if userpass[0] in users.keys() and users[userpass[0]]==userpass[1]:
            return "Доступ разрешен"
        else:
            return "Доступ запрещен"
print(descript(USERS))
'''
'''
def get_rainfall():
    weather_data={}
    city=''
    while True: 
        city = input("Введите название города: ")
        if not city:
            break    
        try:
            rain =int(input("Введите количество осадков в города: "))
        except ValueError:
            print('Ошибка ввода данных')
            continue
        weather_data[city]=weather_data.get(city,0)+rain
    for town in weather_data:
        print(f"{town:10}: {weather_data[town]:4} мм.")
get_rainfall()
'''

'''
def get_rainfall():
    weather_data={}
    all_rain=[]
    while True: 
        city = input("Введите название города: ")
        if not city:
            break    
        try:
            rain =int(input("Введите количество осадков в города: "))
        except ValueError:
            print('Ошибка ввода данных')
            continue
        all_rain=weather_data.get(city,[])
        all_rain.append(rain)
        weather_data[city]=all_rain
    for town in weather_data:
        weather_data[town]=sum(weather_data[town])/len(weather_data[town])
        print(f"{town:10}: {weather_data[town]:4.1f} мм.")
get_rainfall()
'''

'''
def apache_log():
    """Читает код апача
    """
    import os
    apache_tuple={}
    all_ip=[]
    with open('apache.log', 'r') as f:
        for line in f:    
            words=line.split(' ') 
            print(all_ip)
            print(words[8])
            all_ip=apache_tuple.get(words[8],[])
            all_ip.append(words[0])
            print(all_ip)
            apache_tuple.setdefault(words[8],all_ip)  
        for cod in apache_tuple:
            all_ip=str(apache_tuple[cod])
            print(f"Код ответа: {cod:4}, ip-address: {''.join(all_ip)[1:-1]}")
apache_log()
'''

'''
def apache_log():
    """Читает код апача
    """
    import os
    apache_tuple={}
    all_ip=[]
    with open('apache.log', 'r') as f:
        for line in f:    
            words=line.split(' ') 
            print(all_ip)
            print(words[8])
            all_ip=apache_tuple.get(words[8],[])
            all_ip.append(words[0])
            print(all_ip)
            apache_tuple.setdefault(words[8],all_ip)  
        for cod in apache_tuple:
            all_ip=str(apache_tuple[cod])
            print(f"Код ответа: {cod:4}, ip-address: {''.join(all_ip)[1:-1]}")
apache_log()
'''
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

       
def words_in_text(filename):
    """Количество слов каждого типа в файле""" 
    import operator
    content=file_open_str(filename)
    words={}
    num_words=0
    big_words=[]
    big_words_wo=[]
    big_word_tuple={}
    for word in content:
        len_word=len(word)
        if 'http' not in word:
            num_words=words.get(len_word,0)+1
            words[len_word]=num_words
            if len_word > 25:
                big_words.append(word) 
            if len_word > 15 and '-' not in word:
                big_words_wo.append(word) 
                word_b=big_word_tuple.get(len_word,[])
                word_b.append(word)
                big_word_tuple.setdefault(len_word,word_b) 
    words=dict(sorted(words.items()))
    sum_word=0
    for word in words:
        sum_word=sum_word+words[word]
    print(f'Всего слов в файле  {filename} {sum_word}, в том числе:')
    for len_word in words:
        print(f"Слова с количеством букв: {len_word:2} - {words[len_word]:3}.")
    big_words=sorted(big_words,key=len,reverse=True)
    big_words_set=set(big_words)
    print(f'Больше 25 символов: {len(big_words_set)} слов: {big_words_set}')
    big_words_wo=sorted(big_words_wo,key=len,reverse=True)
    big_words_wo_set=set(big_words_wo)
    print(f'Больше 17 символов: {len(big_words_wo_set)} слов: {big_words_wo_set}')
    
    print(f'Больше 15 символов: {len(big_words_wo_set)} слов: {big_words_wo_set}')
    big_word_tuple=dict(sorted(big_word_tuple.items()))
    for len_word in big_word_tuple:
        big_word_set=set(big_word_tuple[len_word])
        big_word_set=sorted(big_word_set)
        finish_word=str(big_word_set)
        print(f"Слова с количеством букв: {len_word:2} - {finish_word:3}.")
BOOKNAME='Толстой Лев. Война и мир. Книга 1.txt'
words_in_text(BOOKNAME)
