from decimal import *

def run_timing():    
    """Определение среднего временниго интервала"""
    numbers_of_runs=0
    total_run=0
    while True:
        one_run=input("Введите время забега 1 км: (или Enter для выхода)")
        if not one_run:
            break
        try:
            one_run=float(one_run)
            total_run+=one_run
            numbers_of_runs+=1
        except ValueError:
            print("Неверное значение")
    if numbers_of_runs>0: 
        average=total_run/numbers_of_runs
        print(f"Среднее время забега {average:.2f} для {numbers_of_runs} забегов")
    else:
        print("Вы не ввели ни одного значения")
#run_timing()

def float_share(float_number : float, before:int ,after:int ):
    """Функция для разделения числа и склеивания"""
    try:    
        s_num = "{:.10f}".format(float_number).rstrip('0').rstrip('.')
        
        if '.' in s_num:
            part_before, part_after = s_num.split('.')
        else:
            part_before, part_after = s_num, ""

        # Правильный срез для before (если 0, то пустая строка)
        new_before = part_before[-before:] if before > 0 else ""
        # Срез для after
        new_after = part_after[:after] if after > 0 else ""
        
        # Склеиваем. Если до точки пусто, добавим 0 для корректности float
        res_str = f"{new_before or '0'}.{new_after or '0'}"
        
        return float(res_str)
        
    except (ValueError, IndexError, TypeError):
        return "Неверное значение"
    
print(float_share(111234.567891, 2, 5))  # 34.56789
print(float_share(100, 2, 2))            # 0.0 (обработка целого числа)
print(float_share(123.456, 0, 2))        # 0.45 (обработка before=0)

class Deciamal
getcontext().prec = 6
Decimal(1) / Decimal(7)
Decimal('0.142857')
getcontext().prec = 28
print(Decimal(1) / Decimal(7))