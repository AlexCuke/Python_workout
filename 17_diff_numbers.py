def how_many_different_numbers(numbers):
    unique_numbers = set (numbers)
    return len(unique_numbers)
    
numbers = [1, 2, 3, 1, 2, 3, 4, 1]
a=how_many_different_numbers(numbers)
print(a)
def file_open(filename):
    """открывает файл код апача
    """
    import os
    with open(filename, 'r') as f:
        content=f.read()
    return content
def file_open_lines(filename):
    """открывает файл код апача
    """
    import os
    content=[]
    with open(filename, 'r') as f:
        for line in f:
            content.append(line)
    return content
#print(file_open_lines('apache.log'))

print('')
def apache_log_ip(filename):
    """Просмотрите файл журнала сервера (например, Apache
или nginx). Какие различные IP-адреса пытались полу-
чить доступ к вашему серверу?
    """
    content=file_open_lines(filename)
    #print(type[content])
    apache_tuple={}
    all_ip=[]
    for line in content:  
        words=line.split(' ') 
        print(words)
        print(len(words))
        apache_tuple.update({words[0]:'IP'})
    print(apache_tuple)

apache_log_ip('apache.log')


def apache_log_cod(filename):
    """Просматривая тот же журнал сервера, постарайтесь от-
ветить, какие коды ответов были возвращены пользовате-
лям? Код 200 означает «ОК», но есть также ошибки 403,
404 и 500. (Регулярные выражения здесь необязательны,
но, возможно, помогут.)
    """
    content=file_open_lines(filename)
    apache_tuple={}
    all_ip=[]
    print(apache_tuple)
    for line in content:  
        words=line.split(' ')      

        print(f'код  {words[8]}  {words[0]}') 
        if words[8] in apache_tuple:
            value=apache_tuple[words[8]]    
        else:
            value=[]
        print(value)
        value.append(words[0])
        print(value)
        apache_tuple.update({words[8]:value})
    print(apache_tuple)

apache_log_cod('apache.log')

def catalog_find():
    """Используйте os.listdir, чтобы получить имена файлов
в текущем каталоге. Какие расширения файлов (т.е. суф-
фиксы, следующие за конечным символом «.») находятся
в этом каталоге? Вероятно, будет полезно использовать
os.path.splitext.
    """
    import os
    files=os.listdir()
    f=os.path.splitext('.')
    file_rash=[]
    for file in files:
        f=os.path.splitext(file)
        file_rash.append(f[1])
    file_rash=set(file_rash)
        
    return file_rash

   
a=catalog_find()
print(a)

def dict_create(stroka):
    """создает словарь и проверяет
    """
    dict_out={}
    stroka=stroka.splite(',')
    for symb in stroka:
        if symb[0] in dict_out:
            value=dict_out[symb[1]]    
        else:
            value=[]
        value.append(symb[1])
        dict_out.update({symb[0]:value})
    return dict_out