'''import operator
MENU = {
    "Брускетта с томатами и базиликом": 350,
    "Тартар из лосося": 680,
    "Сырная тарелка с мёдом": 520,
    "Цезарь с курицей": 420,
    "Греческий салат": 380,
    "Салат с рукколой и пармской ветчиной": 490,
    "Луковый суп с гренками": 290,
    "Борщ с говядиной и сметаной": 320,
    "Тыквенный крем‑суп": 280,
    "Стейк Рибай с картофелем": 1200,
    "Лосось на гриле с овощами": 890,
    "Паста Карбонара": 550,
    "Тирамису": 360,
    "Шоколадный фондан": 390,
    "Чизкейк Нью‑Йорк": 370,
    "Американо": 180,
    "Латте": 220,
    "Морс клюквенный": 150,
    "Лимонад малиновый": 250
}
def restoraunt(menu):
    for dish in menu:
        print(f"{dish:30}: {menu[dish]:4} руб.")
    zakaz=0
    while True: 
        dish = input("Введите названпие блюда: ")
        if not dish:
            print(f"Общая сумма заказа: {zakaz} руб.")
            break
        else:
            if dish in menu.keys():
                zakaz=zakaz+menu[dish]
                print(f"Цена на {dish}: {menu[dish]} руб. Общая сумма заказа: {zakaz} руб.")
            elif dish not in menu.keys():
                print("Такого блюда нет в меню")
restoraunt(MENU)'''

'''USERS = {
    "ivan": "qwerty123",
    "maria": "password456",
    "alex": "mypass789",
    "olga": "secure000"
}

def descript(users):
    zakaz=0
    while True: 
        userpass = input("Введите имя пользователя и пароль через запятую ")
        userpass=userpass.split(",")
        if userpass[0] in users.keys() and users[userpass[0]]==userpass[1]:
            return "Доступ разрешен"
        else:
            return "Доступ запрещен"
print(descript(USERS))
'''
WEATHER_DATA = {
    '2026-02-25': -5,
    '2026-02-26': -3,
    '2026-02-27': 0,
    '2026-02-28': 2,
    '2026-02-29': 1,
    '2026-03-01': -2,
    '2026-03-02': -1
}
from datetime import datetime
def weather(data):
    
    while True: 
        day = input("Введите дату для прогноза погоды в формате месяц/день ")
        day=day.split("/")
        print(day[1])
        full_day='2026-'+day[0]+'-'+day[1]
        print(full_day)
        if full_day in data.keys():
                if datetime(full_day-1) is not None:
                    full_day_before=datetime(full_day)
                full_day_after=datetime(full_day+1)
        print(full_day_before,full_day,full_day_after)
        if full_day_before not in data.keys():
            print("Погоды на день ДО не было")
        else:
            print(f"Погода на {full_day_before}: {data[full_day_before]}")
        if full_day_after not in data.keys():
            print("Погоды на день ПОСЛЕ не было")
        else:
            print(f"Погода на {full_day_after}: {data[full_day_after]}")
        print(f"Погода на {full_day}: {data[full_day]}")
weather(WEATHER_DATA)