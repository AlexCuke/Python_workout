import json
import glob


'''



def reverting_file (first_filename,second_filename):
    """В этой функции мы реализуем
базовую версию этой идеи. Функция принимает два аргумента:
имена входного файла (который будет считан из файла) и выход-
ного файла (который будет создан)."""
    with open (first_filename) as infile, open(second_filename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]} \n')
                
reverting_file('first_string.txt','revert_string.txt')



def secret_file(first_filename, second_filename, third_filename):
    """Эта функция реализует преобразование текста в коды символов
    и обратное восстановление. Функция принимает три аргумента:
    имена входного файла, промежуточного файла и выходного файла."""
    
    # Первый этап: преобразование текста в коды символов
    with open(first_filename, 'r', encoding='utf-8') as infile, \
         open(second_filename, 'w', encoding='utf-8') as outfile:
        for one_line in infile:
            codes = []
            for symbol in one_line:
                if symbol != '\n':  # Не кодируем символ новой строки
                    codes.append(str(ord(symbol)))
            # Записываем коды через пробел
            outfile.write(' '.join(codes) + '\n')
    
    # Второй этап: восстановление текста из кодов символов
    with open(second_filename, 'r', encoding='utf-8') as infile, \
         open(third_filename, 'w', encoding='utf-8') as outfile:
        for one_line in infile:
            if one_line.strip():  # Проверяем, не пустая ли строка
                # Разделяем строку на отдельные коды символов (теперь пробелы есть!)
                codes = one_line.strip().split()
                new_line = ''
                for code in codes:
                    new_line = new_line + chr(int(code))
                outfile.write(new_line + '\n')
            else:
                outfile.write('\n')
                
secret_file('english_text.txt','revert_string_eng.txt','revert_revert_string_eng.txt')


def sogl_glas_file(first_filename, second_filename, third_filename):
    """На основе существующего текстового файла создайте два
новых текстовых файла. Каждый из новых файлов бу-
дет содержать столько же строк, сколько и входной файл.
В один выходной файл вы запишите все гласные (a, e, i, o
и u) из входного файла. В другом — все согласные. (Вы мо-
жете игнорировать пунктуацию и пробелы.)."""
    
    # Первый этап: преобразование текста в коды символов
    with open(first_filename, 'r', encoding='utf-8') as infile, \
         open(second_filename, 'w', encoding='utf-8') as outfile, \
         open(third_filename, 'w', encoding='utf-8') as outfile_2:
        glas='aeiou'
        soglas='bcdfghjklmnpqrstvwxyz'
        for one_line in infile:
            newline_one =''
            newline_two=''
            for symbol in one_line:
                if symbol in glas:  # Не кодируем символ новой строки
                    newline_one=newline_one+symbol
                if symbol in soglas:  # Не кодируем символ новой строки
                    newline_two=newline_two+symbol
            outfile.write(newline_one)
            outfile_2.write(newline_two)

                
sogl_glas_file('english_text.txt','english_text_glas.txt','english_text_soglas.txt')


'''



def unix_log(first_filename, second_filename):
    """Последнее поле в /etc/passwd — это shell, командный
интерпретатор Unix, который вызывается при входе поль-
зователя в систему. Создайте файл, содержащий одну строку
для каждой оболочки, в которой будет записано имя обо-
лочки, а затем все имена пользователей, которые исполь-
зуют эту оболочку,"""
    
    # Первый этап: преобразование текста в коды символов
    with open(first_filename, 'r', encoding='utf-8') as infile, \
        open(second_filename, 'w', encoding='utf-8') as outfile:
        dict_out={}
        for one_line in infile:
            print(one_line)
            if one_line.strip():  # Проверяем, не пустая ли строка
                codes=one_line.split(':')
                print(codes)
                # ИСПРАВЛЕНО: ключ - shell (последнее поле), значение - список пользователей
                shell = codes[-1].strip()  # shell - последнее поле
                username = codes[0]        # имя пользователя - первое поле
                
                if shell in dict_out:
                    dict_out[shell].append(username)
                else:
                    dict_out[shell] = [username]
        
        # ИСПРАВЛЕНО: записываем результат правильно
        for shell in dict_out:
            # shell: пользователь1, пользователь2, пользователь3
            outfile.write(f"{shell}: {', '.join(dict_out[shell])}\n")
        print(dict_out)

                
unix_log('passwd.txt','passwd_out.txt')              

