
def get_rainfall():
    """функцию get_rainfall, которая от-
слеживает количество дождевых осадков в ряде городов. Поль-
зователи вашей программы будут вводить название города, если
название города пустое, то функция распечатает отчет (который
я опишу) перед выходом.
    """
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

def get_rainfall_v2():
    """Вместо того чтобы печатать только общее количество осад-
ков для каждого города, напечатайте общее количество
осадков и среднее количество осадков за определенные
дни.
    """
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
get_rainfall_v2()

def apache_log_v2():
    """Откройте файл журнала из системы Unix/Linux, напри-
мер, из сервера Apache. Для каждого кода ответа (т.е.трехзначного кода, указывающего на успех или неудачу
HTTP-запроса) сохраните список IP-адресов, которые вы-
дали этот код.
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
apache_log_v2()



def apache_log_v3():
    """Откройте файл журнала из системы Unix/Linux, напри-
мер, из сервера Apache. Для каждого кода ответа (т.е.трехзначного кода, указывающего на успех или неудачу
HTTP-запроса) сохраните список IP-адресов, которые вы-
дали этот код.
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
apache_log_v3()

def file_open_str(filename):
    """ЧОткрытие файла и очистка его содержимого."""
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
    """Количество слов каждого типа в файле. Чтение через текстовый файл на диске. Используйте сло-
варь для отслеживания количества слов каждой длины
в файле — то есть, сколько трехбуквенных слов, четырех-
буквенных слов, пятибуквенных слов и так далее. Отобра-
зите результаты.""" 
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
BOOKNAME='Толстой Лев. Война и мир.txt'
words_in_text(BOOKNAME)
