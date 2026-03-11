
def mysum(*args):
    """Суммирует аргументы
    """
    output=0
    print(type(args))
    for arg in args:
        output=output+arg
    return output

    
print(mysum(5,4,6))

def mysum2(*args):
    """Суммирует аргументы c вложенными кортежами
    """
    output=0
    for arg in args:
        if isinstance(arg, (list, tuple)):
            for arg1 in arg:
                output += arg1 # Используем встроенную сумму для списка
        else:
            output += arg
    return output
    
print(mysum2([5,4,6],3))

def arth_mean(*args):
    """Среднее арифметическое
    """
    output=0
    space=0
    for arg in args:
        space=len(args)
        if isinstance(arg, (list, tuple)):
            space=space+len(arg)-1
            for arg1 in arg:
                output += arg1 # Используем встроенную сумму для списка
        else:
            output += arg
    output=output/space
    return output

    
print(arth_mean(5,4,6))