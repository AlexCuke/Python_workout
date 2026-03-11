def hex_output():
    """Шестнадцатеричное в десятичное
    """
    decnum = 0
    hexnum = input('Введите шестнадцатеричное число для преобразования:')
    for power, digit in enumerate (reversed(hexnum)):
        print (power, digit)
        decnum += int (digit, 16)* (16 ** power)
    print (decnum)
#hex_output()
def manual_hex_to_dec(hex_string):
    """Шестьнадцатеричное в десятичное вариант
    """
    decimal_value = 0
    # Убираем префикс 0x, если он есть, и переводим в верхний регистр
    hex_string = hex_string.lower().replace("0x", "")
    
    for char in hex_string:
        code = ord(char)
        
        if ord('0') <= code <= ord('9'):
            # Для цифр 0-9: код '0' это 48. ord('5') - 48 = 5
            digit = code - ord('0')
        elif ord('a') <= code <= ord('f'):
            # Для букв a-f: код 'a' это 97. ord('a') - 97 + 10 = 10
            digit = code - ord('a') + 10
        else:
            raise ValueError(f"Недопустимый символ для 16-ричной системы: {char}")
        
        # Сдвигаем разряд (умножаем на 10 в 16-ричной, то есть на 16)
        decimal_value = decimal_value * 16 + digit
        
    return decimal_value

# Проверка:
print(manual_hex_to_dec("1A"))   # 26 (1*16 + 10)
print(manual_hex_to_dec("FF"))   # 255 (15*16 + 15)
print(manual_hex_to_dec("0xabc")) # 2748

def triangle_name():
    """Треугольник имени
    """
    name = input('Введите имя: ')
    new_name=''
    for power, digit in enumerate (name):
        new_name += digit
        print (new_name)
triangle_name()
help(triangle_name)