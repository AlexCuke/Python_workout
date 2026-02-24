import os
from datetime import datetime
import types
def logger(old_function):
    def new_function(*args, **kwargs):
        # Вызываем оригинальную функцию и получаем результат
        result = old_function(*args, **kwargs)
        
        # Получаем текущую дату и время
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Формируем строку лога
        # Мы записываем: дата/время, имя функции, аргументы и результат
        log_entry = (
            f"{timestamp} | Function: {old_function.__name__} | "
            f"Args: {args} | Kwargs: {kwargs} | Result: {result}\n"
        )
        
        # Записываем в файл 'main.log' в режиме дополнения ('a')
        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(log_entry)
            
        return result

    return new_function
#Функция из второго задания про итераторы
@logger
def flat_generator(list_of_lists):
    # Проходим по каждому вложенному списку во внешнем списке
    for sublist in list_of_lists:
       for item in sublist:
            # Возвращаем элемент по одному
            yield item
            
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print("Тест пройден успешно!")

if __name__ == '__main__':
    test_2()