def firstlast(input_data):
    """Первый и последний символ"""
    type1=type(input_data)
    output_data=input_data[:1]+input_data[-1:]
    print(output_data)
        
    
#firstlast('dfkgjadjkgkSBKFJS')
#firstlast(['1','1','2','1'])
#firstlast((1,2,3,4))
def  a2_2(input_data):
        return input_data*input_data
def  max_elem(input_data): 
    return  max(input_data, default=None)    
def  max_elem(input_data): 
    return  max(input_data, default=None)  
def even_odd_sums(input_data):
    """Слкдаывает четные и нечетные символы"""
    sums = [0, 0]
    # enumerate starts at 0 by default
    for index, elem in enumerate(input_data):
        # index % 2 will be 0 for even indices, 1 for odd indices
        sums[index % 2] += int(elem)
    
    print(sums)
    
#even_odd_sums(['1','1','2','1'])
#even_odd_sums((1,2,3,4))

def plus_minus(input_data):
    """Слкдаывает четные и нечетные символы"""
    sum=0
    # enumerate starts at 0 by default
    for index, elem in enumerate(input_data):
        # index % 2 will be 0 for even indices, 1 for odd indices
        if index % 2 == 0:
            sum=sum+int(elem)
        else:
            sum=sum-int(elem)
    
    print(sum)
    
#plus_minus(['1','1','2','1'])
#plus_minus((1,2,3,4))

def emul_zip(*input_data):
    """Эмулирует функцию ZIP"""
    #Создание пустых множеств
    words=input_data[0]
    sec_data=[]
    for i in range(len(words)):
        temp_data=[]
        sec_data.append(temp_data)
    #Преобразование в списки
    for index in range(len(input_data)):
        words=input_data[index]
        print(words)
        for i in range(len(words)):
            sec_data[i].append(words[i])
        print(sec_data)
    #Преобразуем в кортежи:
    output_data=[]
    for word in sec_data:
        output_data.append(tuple(word))
    print(output_data)

    
emul_zip([10, 20,30],'abc')
emul_zip([10, 20,30,40],'abcs',[10, 20,30,40])

def emul_zip(*input_data):
    """Эмулирует функцию ZIP (останавливается на кратчайшем списке)"""
    # Если на вход ничего не подали, возвращаем пустой список
    if not input_data:
        return []

    # Находим длину самого короткого списка, чтобы избежать IndexError
    min_len = min(len(item) for item in input_data)
    
    output_data = []
    
    # Итерируемся по индексам от 0 до min_len
    for i in range(min_len):
        # Создаем кортеж из i-тых элементов каждого списка
        temp_list = []
        for sequence in input_data:
            temp_list.append(sequence[i])
        
        output_data.append(tuple(temp_list))
        
    return output_data

# Проверка:
print(emul_zip([1, 2, 3], ['a', 'b', 'c', 'd'], [True, False]))
def emul_zip(*input_data):
    if not input_data: return []
    
    min_len = min(len(item) for item in input_data)
    
    # Генератор списка: берем i-й элемент из каждого seq для каждого i
    return [tuple(seq[i] for seq in input_data) for i in range(min_len)]