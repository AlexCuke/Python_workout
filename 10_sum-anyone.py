def arth_mean(*args):
    "Суммирует любые множества"
    if args:
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
    else:
        ValueError

    
print(arth_mean(5,4,6))
print(arth_mean())