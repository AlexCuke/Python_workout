def dictdiff(first,second):
    """Напишите функцию dictdiff , которая принимает два сло-
варя в качестве аргументов. Функция вернет новый словарь, ко-
торый будет представлять собой разницу между двумя слова-
рями."""
    
    all_keys=first.keys()|second.keys()
    return all_keys
a={'a':1, 'b':2, 'c':3}
b={'a':1, 'b':2, 'c':4}

result=dictdiff(a,b)
print(result)

def pr_type(a):
    print(type(a))
#НЕ ГОТОВО
'''def dict_plus_dict(*dicts):
    """Напишитефункцию, которая принимает любое количество словарей
и возвращает словарь, представляющий собой комбинацию из них
Получаем все ключи как
из первого, так и из вто-
рого, без повторений.
Используется тот факт, что
dict.get возвращает None,
если ключ не существует.
126 Лернер Реувен. Python-интенсив: 50 быстрых упражнений
цию из них. Если один и тот же ключ появляется более
чем в одном словаре, то в выходных данных должно по-
явиться значение самого последнего объединенного сло-
варя."""
    new_dict={}
    print(type(new_dict))
    for dict in dicts:
        
        pr_type(dict)
        print(dict)
        new_dict=new_dict.update(dict)
    return new_dict
a={'a':1, 'b':2, 'c':3}
b={'a':1, 'b':2, 'c':4}
result=dict_plus_dict(a,b)
print(result)
print(type(a))'''
#НЕ ГОТОВО

def dict_new_two(*args):
    """Напишите функцию, которая принимает любое четное
количество аргументов и возвращает на их основе сло-
варь. Аргументы с четным индексом становятся ключами
словаря, а аргументы с нечетным номером становятся
значениями словаря."""
    if len(args)%2==0:
        new_dict={}
        for i in range(len(args)):
            if i%2==0:
                new_dict1={args[i]:args[i+1]}
                new_dict.update(new_dict1)
    return new_dict
result=dict_new_two('a',3,'b',7,'c',8)
print(result)

def dict_partition(d, f):
    """
    Разделяет словарь на два в соответствии с результатом функции f.

    Args:
        d (dict): исходный словарь с парами ключ-значение.
        f (function): функция-предикат, принимающая ключ и значение
            и возвращающая True или False.

    Returns:
        tuple: кортеж из двух словарей:
            - первый словарь: пары, для которых f(key, value) == True;
            - второй словарь: пары, для которых f(key, value) == False.
    """
    true_dict = {}
    false_dict = {}

    for key, value in d.items():
        if f(key, value):
            true_dict[key] = value
        else:
            false_dict[key] = value

    return true_dict, false_dict
    
data = {'a': 5, 'b': 15, 'c': 8, 'd': 20}
result = dict_partition(data, lambda k, v: v > 10)
print(result)