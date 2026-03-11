'''def get_final_line(filename):
    """вывод последней строки"""
    encodings = ['utf-8', 'cp1251', 'koi8-r', 'iso-8859-5']
    final_line=''
    with open(filename,encoding='utf-8') as f:
        for current_line in f:
            if current_line!='':
                final_line=current_line
    return final_line
    
a=get_final_line('tolstoy_voyna-i-mir.txt')
print(a)

import re

def sum_integers_in_file(filename):
    """Найдите все слова
        (без пробелов в записи слова и не окруженные пробелами),
        которые содержат только целые числа, и росуммируйте их."""   
    total_sum = 0
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Находим все последовательности цифр в строке
            numbers = re.findall(r'\d+', line)
            # Преобразуем в целые числа и суммируем
            total_sum += sum(int(num) for num in numbers)
    
    return total_sum

# Использование
result = sum_integers_in_file('tolstoy_voyna-i-mir.txt')
print(f"Сумма всех целых чисел в файле: {result}")'''
'''
def sum_in_file(filename):
    """Сумма перемноженных чисел в строке"""
    total_sum = 0
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
           line_tuple=line.split('  ')
           print(line_tuple)
           if len(line_tuple)>1:
               sum_1=int(line_tuple[0])*int(line_tuple[1])
               total_sum=total_sum+sum_1            
    return total_sum

# Использование
result = sum_in_file('math.txt')
print(f"Ответ: {result}")
'''
def sum_in_file_glas(filename):
    """С помощью словаря подсчитайте, сколько раз каждая гласная (a, e,
            i, o и u) встречается в файле. Распечатайте"""
    glassnie={'а':0,'е':0,'ы':0,'о':0,'я':0,'и':0,'ю':0}
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
           for keys in  glassnie:
               if keys in line:
                    glassnie[keys]=glassnie[keys]+1
    return glassnie

# Использование
filename1='tolstoy_voyna-i-mir.txt'
result = sum_in_file_glas(filename1)
print(f'Каждая буква встречается в тексте "{filename1.split('.')[0]}" раз:')
for items in result:
    print(f"{items[0]}: {result[items]}")