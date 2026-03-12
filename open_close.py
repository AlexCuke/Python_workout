def file_open(filename):
    """Открытие файла построчно
    """
    with open(filename, 'r', encoding='utf-8') as f:
        # readlines() читает все строки и возвращает их списком
        content = f.readlines() 
        return content   
     
def file_open_one(filename):
    """Открытие файла построчно
    """
    with open(filename, 'r', encoding='utf-8') as f:
        # readlines() читает все строки и возвращает их списком
        content=f.read()
        return content     
    
def write_to_file(filename, data_list):
    """Запись в файл
    """
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