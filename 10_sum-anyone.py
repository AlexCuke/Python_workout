def mysum(*items):
    "Суммирует любые множества"
    
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
    """Суммирует любые множества, bigger - в сумму попадают значения меньше bigger"""  
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
    """Суммирует любые множества,преобразуя строки в числа"""
    
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
    """Суммирует любые количество словарей в один"""
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

