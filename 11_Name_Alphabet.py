from operator import itemgetter
PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
            {'first':'Donald', 'last':'Trump',
                'email':'president@whitehouse.gov'},
            {'first':'Vladimir', 'last':'Putin',
                'email':'president@kremvax.ru'}
            ]
def person_dict_to_list (d):
    """Словарь в список
    """
    return [d['last'], d['first']]
def alphabetize_names(list_of_dict):
    """Телефонная книмга по алфавиту. функцию alphabetize_names,
которая предполагает существование константы PEOPLE, опре-
деленной, как показано в коде. Функция должна возвращать спи-
сок словарей, отсортированных по фамилии и имени"""
    for p in sorted(list_of_dict,key=lambda x: [x ['last'], x ['first']]):
            print(f'{p['last']},{p['first']}:{p['email']}')


alphabetize_names(PEOPLE)

def alphabetize_names_new(list_of_dict):
    """Телефонная книмга по алфавиту. функцию alphabetize_names,
которая предполагает существование константы PEOPLE, опре-
деленной, как показано в коде. Функция должна возвращать спи-
сок словарей, отсортированных по фамилии и имени"""
    for p in sorted(list_of_dict,key=itemgetter ('last','first') ):
            print(f'{p['last']},{p['first']}:{p['email']}')


alphabetize_names_new(PEOPLE)

def sort_absolute(list_1):
    """Сортировка по абсолютной величине.Учитывая последовательность положительных и отрица-
тельных чисел, отсортируйте их по абсолютной величине."""
    print(sorted(list_1,key=abs))


sort_absolute([5,7,-1,3,-4])

def sort_absolute(list_1):
    """Сортировка по количеству гласных (убывание).Задав список строк, отсортируйте их по количеству содер-
жащихся в них гласных."""
    vowels = 'aeiouAEIOU'

    def count_vowels(word):
        return sum(1 for char in word if char in vowels)

    return sorted(list_1, key=count_vowels, reverse=True)
result = sort_absolute(['sfsdaaaf', 'dfa', 'erdfwwa'])
print(result)



def sort_list(*list_1):
    """Сортировка сумме чисел вложенных списков. Если дан список списков, каждый из которых содержит
ноль или более чисел, отсортируйте его по сумме чисел
каждого внутреннего списка."""

    def sum_list(list_2):
        output=0
        if len(list_2)==0:
            output=0
        else:
            for item in list_2:
                output+=item
        return output


    return sorted(list_1, key=sum_list, reverse=True)
result = sort_list([10, 20, 30], [40, 50, 60], [70, 80])
print(result)
