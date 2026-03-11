def ubbi_dubbi(word):
    """Убби-Дубби"""
    #word = input('Введите слово: ')
    symbols='aiou'   
    for letter in word:
        if letter in symbols:
            word=word.replace(letter, 'ub'+letter)

    print(word)
    return word
ubbi_dubbi('word')

def ubbi_dubbi_ver_2(word):
    """Работа словами, написанными с заглавной буквы. Если слово
написано с заглавной буквы (т.е. первая буква заглавная,
а остальная часть слова — нет), то перевод на Убби-Дубби
должен быть написан с такой же заглавной буквы."""
    
    symbols='aeiou' 
    output=[]  
    for letter in word:
        if letter in symbols:
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    word=''.join(output)
    print(word)
    return word

ubbi_dubbi_ver_2('wofgihfsehd')   

        
def ubbi_dubbi_ver_3(word):
    """Работа словами, написанными с заглавной буквы. Если слово
написано с заглавной буквы (т.е. первая буква заглавная,
а остальная часть слова — нет), то перевод на Убби-Дубби
должен быть написан с такой же заглавной буквы."""
    first_letter=word[0]
    word=word.lower()
    symbols='aeiou' 
    output=[]  
    for letter in word:
        if letter in symbols:
            output.append(f'ub{letter}')
        else:
            output.append(letter)            
    word=''.join(output)
    if first_letter.isupper() is True:
        word=word.capitalize()
    print(word)
    return word

ubbi_dubbi_ver_3('Awofgihfsehd') 
ubbi_dubbi_ver_3('ewofgihfsehd') 


def delete_authors(string_authors: str):
    """Удаление имен авторов. В научных кругах принято удалять
имена авторов из статьи, представленной на рецензирова-
ние. Получив строку со статьей и отдельный список строк
с именами авторов, замените все имена в статье симво-
лами _""" 
    string_authors=string_authors.split('-')
    filetext_new=[]
    alpabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open('6.txt', 'r') as f:
        number=0
        for line in f:    
            if number >= (int(string_authors[0])-1) and number <= (int(string_authors[1])-1):   
                new_line=[]
                for symbol in line:
                    if symbol in alpabet:
                        new_line.append('_')
                    else:
                        new_line.append(symbol)  
                new_line=''.join(new_line)
                filetext_new.append(new_line)                     
            else:
                filetext_new.append(line)  
            number +=1
    print (filetext_new)
    with open('7.txt', 'w') as f:        
        f.writelines(filetext_new)
#delete_authors('1-2')

def file_open(filename):
    """Открытие файла построчно"""
    with open(filename, 'r', encoding='utf-8') as f:
        # readlines() читает все строки и возвращает их списком
        content = f.readlines() 
        return content    
    
    
def write_to_file(filename, data_list):
    # 'w' - перезапишет файл, 'a' - добавит в конец
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(data_list) 
        # Обычно здесь ничего не возвращают, 
        # либо возвращают True как признак успеха
        return True
# Использование:
# my_data = ["Первая строка\n", "Вторая строка\n"]
# write_to_file('output.txt', my_data)    
#print(file_open('6.txt'))
#write_to_file('8.txt', data_list)
            
def del_authors(line):
    """Удаление имен авторов. В научных кругах принято удалять
имена авторов из статьи, представленной на рецензирова-
ние. Получив строку со статьей и отдельный список строк
с именами авторов, замените все имена в статье симво-
лами _
    """
    alpabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_line=[]
    for symbol in line:
        if symbol in alpabet:
            new_line.append('_')
        else:
            new_line.append(symbol)  
    new_line=''.join(new_line)
    return new_line       

def delete_authors_ver_2(string_authors: str,filename: str):
    """Удаление имен авторов. В научных кругах принято удалять
имена авторов из статьи, представленной на рецензирова-
ние. Получив строку со статьей и отдельный список строк
с именами авторов, замените все имена в статье симво-
лами _""" 
    file_text=file_open(filename)
    print(file_text)
    filetext_new=[]
    number=0
    for line in file_text:
        if '-' in string_authors:
            string_authors=string_authors.split('-')
            if number >= (int(string_authors[0])-1) and number <= (int(string_authors[1])-1):  
                line=del_authors(line)    
        elif ',' in string_authors:
            if number in string_authors:  
                line=del_authors(line)
        filetext_new.append(line) 
        number+=1
    write_to_file('8.txt', filetext_new)
def string_authors_edit(string_authors):
    """Удаление имен авторов. В научных кругах принято удалять
имена авторов из статьи, представленной на рецензирова-
ние. Получив строку со статьей и отдельный список строк
с именами авторов, замените все имена в статье симво-
лами _""" 
    string_authors_final = [] # Инициализируем список
    
    if '-' in string_authors:
        parts = string_authors.split('-')
        # Превращаем в числа и создаем диапазон (минус 1 для индексов Python)
        for num in range(int(parts[0]), int(parts[1]) + 1):
            string_authors_final.append(num - 1)
            
    elif ',' in string_authors:
        parts = string_authors.split(',')
        for num in parts:
            string_authors_final.append(int(num) - 1)
    else:
        # Если введено одно число
        string_authors_final.append(int(string_authors) - 1)
        
    return string_authors_final
def delete_authors_ver_3(string_authors: str,filename: str):
    """Удаление имен авторов. В научных кругах принято удалять
имена авторов из статьи, представленной на рецензирова-
ние. Получив строку со статьей и отдельный список строк
с именами авторов, замените все имена в статье симво-
лами _""" 
    file_text=file_open(filename)
    print(file_text)
    filetext_new=[]
    number=0
    string_authors_final=string_authors_edit(string_authors)
    for line in file_text: 
        if number in string_authors_final:  
                line=del_authors(line)    
        filetext_new.append(line) 
        number+=1
    write_to_file('8.txt', filetext_new)
    print("Готово. Результат в 8.txt")
string_authors='1-2'
filename='6.txt'
delete_authors_ver_3(string_authors,filename)
string_authors='5,7,8'
delete_authors_ver_3(string_authors,filename)
