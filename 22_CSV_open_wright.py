import csv
def passwd_to_csv(passwd_filename, csv_filename):
    """функцию которая принимает в качестве аргументов два имени файлов:
первое — это файл в стиле passwd для чтения, а второе — имя
файла, в который нужно записать вывод."""
    with open (passwd_filename) as passwd,open (csv_filename, 'w') as output:
        infile = csv.reader(passwd,delimiter=':')
        outfile = csv.writer(output,delimiter='\t')
        for record in infile:
            if len (record) > 1:
                outfile.writerow((record[0],record[2]))
                
passwd_to_csv('passwd.txt','passwd.log')


def passwd_to_csv_v2(passwd_filename,csv_filename):
    """функцию копросив пользователя ввести
разделенный пробелами список целых чисел, указываю-
щих, какие поля должны быть записаны в выходной CSV-
файл. Также спросите пользователя, какой символ должен
использоваться в качестве разделителя в выходном файле.
Затем считайте данные из /etc/passwd, записывая выбран-
ные пользователем поля, разделенные выбранным пользо-
вателем разделителем., а второе — имя
файла, в который нужно записать вывод."""
    content=input("Введите список чисел разделенных пробелами ")
    delimiter_inp=input("Введите разделитель ")
    field_indices = list(map(int, content.split()))
    with open (passwd_filename) as passwd,open (csv_filename, 'w') as output:
        infile = csv.reader(passwd,delimiter=':')
        outfile = csv.writer(output,delimiter=delimiter_inp)
        for record in infile:
                # Проверяем, что запись не пустая и содержит запрашиваемые поля
                if record and all(idx < len(record) for idx in field_indices):
                    # Выбираем только указанные поля
                    selected_fields = [record[idx] for idx in field_indices]
                    outfile.writerow(selected_fields)
                
#passwd_to_csv_v2('passwd.txt','passwd-v2.log')


def dict_to_csv_file(dict,csv_filename):
    """функцию функцию, которая записывает словарь в CSV-
файл. Каждая строка CSV-файла должна содержать три
поля: (1) ключ, который мы будем считать строкой, (2) зна-
чение и (3) тип значения (например, str или int)."""
    with open (csv_filename, 'w',newline='', encoding='utf-8') as output:
        outfile = csv.writer(output,delimiter=';')
        for key,values in dict.items():
            outfile.writerow((key,values,type(values).__name__))

DICT_1={
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
dict_to_csv_file(DICT_1,'dict_to_csv_file.log')
import random
def random_numbers(csv_filename):
    """Создайте CSV-файл, в котором каждая строка содержит
10 случайных целых чисел от 10 до 100. Т."""
    NUM_ROWS = 100

    with open('random_numbers.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        for _ in range(NUM_ROWS):
            # Генерируем 10 случайных чисел от 10 до 100
            row = [random.randint(10, 100) for _ in range(10)]
            writer.writerow(row)

    print("CSV-файл 'random_numbers.csv' успешно создан!")
                
random_numbers('random.csv')


dict_to_csv_file(DICT_1,'dict_to_csv_file.log')

import random
def csv_read_plus(csv_filename_input,csv_filename_output):
    """ CSV-файл, в котором каждая строка содержит
10 случайных целых чисел от 10 до 100. Теперь считайте
файл и выведите сумму и среднее значение чисел в каж-
дой строке."""
    with open (csv_filename_input) as input,open (csv_filename_output, 'w') as output:
        infile = csv.reader(input,delimiter=',')
        outfile = csv.writer(output,delimiter='\t')
        for row in infile: 
            sum_row=0
            for int1 in row:
                sum_row=sum_row+int(int1)
            sred=sum_row/len(row)
            newrow=[sum_row,sred]
            outfile.writerow(newrow)

    print("CSV-файл 'random_numbers.csv' успешно создан!")
                
csv_read_plus('random_numbers.csv','random_plus.csv')