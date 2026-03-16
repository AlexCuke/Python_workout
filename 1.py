import random
def hello():
    """Функция приветствия"""
    name=input("Введите Ваше Имя ")
    print(f"Добро пожаловать, {name}!")

def number_sistems(sis,number):
    """Номер"""
    if sis==0:
        number=int(number*2/10)
    elif sis==1:
        number=int(number*10/10)      
    elif sis==2:
        number=int(number*16/10)
    return number  
def quessing_hame():
    """Игра в вопросы"""
    number_challange=3
    coorect_number=random.randint(0,100)
    sis=random.randint(0,2)
    if number_challange != 0:
        number=int(input("Введите число от 1 до 100 ")) 
        number=number_sistems(sis,number)
        while number != coorect_number:   
            if number_challange != 0:          
                if number > coorect_number:
                    print("Слишком большое")
                else:
                    print("Слишком маленькое") 
                number=int(input("Введите число от 1 до 100 ")) 
                number=number_sistems(sis,number)
                number_challange=number_challange-1
                print(f'Осталось попыток:{number_challange}')  
            else:
                print("Вы проиграли")  
                break        
        if number == coorect_number: 
            print("То что надо!")

    
hello()
quessing_hame()