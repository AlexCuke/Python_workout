import json
import glob
def print_scores (dirname):
    """JSON оценки"""
    scores = {}
    for filename in glob.glob(f'{dirname} /*.json'):
        scores[filename] = {}
    with open (filename) as infile:
        for result in json.load(infile):
            for subject, score in result.items ():
                scores[filename].setdefault
                (subject, [])
                scores[filename][subject].append (score)
    for one_class in scores:
        print (one_class)
        for subject, subject_scores in scores[one_class].items ():
            min_score = min (subject_scores)
            max_score = max (subject_scores)
            average_score = (sum(subject_scores) / len (subject_scores))
            print (subject)
            print (f'\tmin {min_score}')
            print (f'\tmax {max_score}')
            print (f'\taverage {average_score}')
            
def csv_to_json(csv_filename_input,json_filename_output,delimiter_1):
    import csv
    """Преобразовать файл /etc/passwd из формата CSV
    в JSON. Файл JSON будет содержать эквивалент списка кор-
    тежей Python, причем каждый кортеж будет представлять
    одну строку из файла."""
    with open (csv_filename_input,'r', encoding='utf-8') as input:
        infile = csv.reader(input,delimiter=delimiter_1)
        big_open=[]
        for row in infile: 
            row_set=tuple(row)
            big_open.append(row_set)
    with open(json_filename_output, 'w', encoding='utf-8') as output_file:
        json.dump(big_open, output_file, ensure_ascii=False, indent=4)
csv_to_json('passwd.txt','passwd.json',':')

def json_to_dict(filename_input):
    import csv
    """Для решения несколько иной задачи превратите каждую
строку в файле в словарь Python. Для этого потребуется иден-
тифицировать каждое поле с уникальным именем столбца
или ключа. Если вы не уверены, что делает каждое поле в /
etc/passwd, вы можете выбрать ему произвольное имя."""
    with open(filename_input, 'r', encoding='utf-8') as input:
        rows=json.load(input)
    print(rows)
    output_dict={}
    names=['Username','Password','UID','GID','GECOS','Home directory','Login shell']
    transposed = [list(row) for row in zip(*rows)]          #Траспонирует матрицу
    print(len(transposed))
    for i,name in enumerate(names):     
        output_dict.setdefault(name,transposed[i])
        

    for keys,values in output_dict.items():
        print(f'key: {keys} : {values}')
        print('')    

json_to_dict('passwd.json')

def transpon(filename_input):
    """Трансопнирует матрицу"""
    output = [list(row) for row in zip(*filename_input)]
    return output

def open_json(filename_input):
    """Открывает файл JSON """
    with open(filename_input, 'r', encoding='utf-8') as input:
        output=json.load(input)
    return output

def print_ditc(input_dict):
    """Красивая печать словаря"""
    for keys,values in input_dict.items():
            print(f'{keys} : {values}')
            print('')   
    return True

def wright_to_json(input,json_filename_output):
    """Пишет данные словаря в json"""

    with open(json_filename_output, 'w', encoding='utf-8') as output_file:
        json.dump(input, output_file, ensure_ascii=False, indent=4)
    return True      
        
wright_to_json('passwd.txt','passwd.json',':') 
       
def catalog_info(catalog_name):
    """Данные о файлах в каталоге."""
    import os
    files=os.listdir(catalog_name)
    stat_dict={}
    for filename in files:
        if os.path.isdir(filename) is False:
            statis=os.stat(filename)
            stat_dict.setdefault(filename,[statis[6],statis[7:]])
    #print(stat_dict)
    filename='catalog_info.json'
    wright_to_json(stat_dict,'catalog_info.json')  
    return filename
#catalog_info(catalog_name)

def catalog__statistic(input_dict):
    """Данные о файлах в каталоге."""
    values_max={'biggest':['',0],'smallest':['',100000000],'newst':['',0],'oldest':['',1000000000000000]}
    
    for keys,values in input_dict.items():
        if int(values[0])>int(values_max['biggest'][1]):
            values_max['biggest'][0]=keys
            values_max['biggest'][1]=values[0]
        if int(values[0])<int(values_max['smallest'][1]):
            values_max['smallest'][0]=keys
            values_max['smallest'][1]=values[0]
        for value in values[1]:
            if int(value)>int(values_max['newst'][1]):
                values_max['newst'][0]=keys
                values_max['newst'][1]=value
            if int(value)<int(values_max['oldest'][1]):
                values_max['oldest'][0]=keys
                values_max['oldest'][1]=value
    print(values_max)

#catalog__statistic()

def statistica_catalog():
    import os
    """Спросите у пользователя имя каталога. Переберите все
файлы в этом каталоге (игнорируя подкаталоги), получите
(через os.stat) размер файла и время его последнего из-
менения. Создайте на диске файл в формате JSON, содер-
жащий имя каждого файла, его размер и временную метку
модификации. Затем снова прочитайте файл и определите,
какие файлы были изменены чаще всего и наименее не-
давно, а также какие файлы являются самыми большими
и самыми маленькими в этом каталоге.."""
    #catalog_name=input('Введите Имя каталога')
    #catalog_name = os.path.normpath(catalog_name)   
    catalog_name=r'C:/Users/Давыдов Александр/Desktop/REPO/Python_workout-1/'
    if os.path.exists(catalog_name) and os.path.isdir(catalog_name):
        print(f"Каталог '{catalog_name}' существует. Открываю...")
    json_stat_file=catalog_info(catalog_name)
    with open(json_stat_file, 'r', encoding='utf-8') as input_file:
        rows=json.load(input_file)
    output=catalog__statistic(rows)
    return output
output=statistica_catalog()
print(output)