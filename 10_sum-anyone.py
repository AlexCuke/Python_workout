def mysum_v2(*items):
    """Суммирует любые множества.  Эта задача просит вас переопределить функцию mysum
из главы 1 так, чтобы она могла принимать любое количество ар-
гументов. Все аргументы должны быть одного типа и подходить
под работу с оператором +. (Таким образом, функция должна
работать с числами, строками, списками и кортежами, но не
с множествами и словарями.)"""
    
    if not items:
            print('Аргументы не заданы')
            ValueError 
    else:
        #print(f'{type(items)} - {items}\n') #Тип аргументов котрые заданы
        output=items[0]
        for item in items[1:]:            
             output += item
        #print(f'{type(arg)} - {arg}') #Тип аргументов котрые заданы
        return output
'''
print(mysum())    
print(mysum(5,4,6)) 
print(mysum('abc','def'))
print(mysum([1,2,3],[4,5,6]))
print(mysum(10, 20, 30, 40)) 
print(mysum('a','b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))
'''
def mysum_bigger_than(bigger,*items):
    """Суммирует любые множества, bigger - в сумму попадают значения меньше bigger. Напишите функцию mysum_bigger_than, которая ра-
ботает так же, как mysum, за исключением того, что она
принимает первый аргумент, предшествующий *args.
Этот аргумент задает максимальное значение аргумента,
которое можно добавить в сумму. Таким образом, вызов
В Python все считается True в
if, кроме None, False, 0 и пустых
коллекций. Поэтому если кор-
теж items пуст, мы просто вер-
нем пустой кортеж.
Мы предполагаем, что
элементы items могут быть сложены вместе. mysum_bigger _than (10, 5, 20, 30, 6) вернет
50 — потому что 5 и 6 не больше, чем 10. Эта функция
аналогично работает с любым типом и предполагает, что
все аргументы имеют одинаковый тип. Обратите внима-
ние, что > и < работают с различными типами в Python,
а не только с числами. Для строк, списков и кортежей это
относится к их порядку сортировки."""  
    #print(bigger)
    #print(*items)
    if not items:
            print('Аргументы не заданы')
            ValueError 
    else:
        #print(f'{type(items)} - {items}\n') #Тип аргументов котрые заданы
            if min(items) > bigger:
                output ='Все аргументы больше большего'
            else:
                if isinstance(items[0],(str)):
                    output=''
                elif isinstance(items[0],(int)):
                    output=0
                elif isinstance(items[0],(list)):
                    output=[]
                for item in items:                 
                    if item<bigger:
                        output+=item
            return output
            
''' 
print(mysum_bigger_than(1,5,4,6))
print(mysum_bigger_than(5,5,4,6))
print(mysum_bigger_than(7,5,4,6))
print(mysum_bigger_than('cdef','abc','def'))
print(mysum_bigger_than([1,2,3],[4,5,6]))
print(mysum_bigger_than(40, 20, 30, 40)) 
print(mysum_bigger_than('aa','b', 'c', 'd'))
print(mysum_bigger_than([10, 20, 30,40], [40, 50, 60], [70, 80]))
'''


def sum_numeric(*items):
    """Суммирует любые множества,преобразуя строки в числа. Напишите функцию sum_numeric, которая принимает
любое количество аргументов. Если аргумент является це-
лым числом или может быть преобразован в целое число,
то он должен быть добавлен к сумме. Аргументы, кото-
рые не могут быть преобразованы в целые числа, должны
быть проигнорированы. Результатом является сумма чисел.
Соответственно, sum_numeric (10, 20, ‘a’, ‘30’,
‘bcd’) вернет 60. Обратите внимание, что даже если
строка 30 является элементом списка, она преобразуется
в целое число и добавится к сумме."""
    
    if not items:
            print('Аргументы не заданы')
            ValueError 
    else:
        #print(f'{type(items)} - {items}\n') #Тип аргументов котрые заданы
        output=0
        for item in items: 
            if isinstance(item,(str)):
                if item.isdigit():
                    output+=int(item)
            else:
                output+=item

        #print(f'{type(arg)} - {arg}') #Тип аргументов котрые заданы
        return output
    
print(sum_numeric(10,20,'a','30','bcd'))

def sum_numeric_refact(*items):
    """Суммирует любые множества,преобразуя строки в числа"""
    
    if not items:
            print('Аргументы не заданы')
            ValueError 
    else:
        #print(f'{type(items)} - {items}\n') #Тип аргументов котрые заданы
        output=0
        for item in items: 
            if str(item).isdigit():
                output+=int(item)
        return output
print(sum_numeric_refact(10,20,'a','30','bcd'))


def sum_dict(*list_dict):
    """Суммирует любые количество словарей в один.Напишите функцию, которая принимает список слова-
рей и возвращает один словарь, объединяющий все ключи
и значения. Если ключ встречается в более чем одном аргу-
менте, то значением должен быть список, содержащий все
значения из аргументов."""
    newdict={}
    for dict in list_dict:
        for key in dict:
            if key in newdict:
                value_newdict=newdict[key]
                del newdict[key]
                if not isinstance (value_newdict,list):
                    value_newdict=[]
                value_newdict.append(dict[key])   
                newdict.setdefault(key,value_newdict)        
            else:
                newdict[key]=dict[key]

    return newdict

print(sum_dict({'a':1,'b':2},{'a':3,'c':4},{'a':5,'d':6},{'a':7,'e':8},{'a':9,'f':10},))

