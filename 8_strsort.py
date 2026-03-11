def strsort(input_string):
    """Сортирофка символов в строкею Функ-
цию strsort, которая принимает на вход строку и возвращает
строку. Возвращаемая строка должна содержать те же символы,
что и входная, за исключением того, что ее символы должны
быть отсортированы в порядке от наименьшего значения к наи-
большему Unicode."""
    sorted_string=sorted(input_string)
    sorted_string=''.join(sorted_string)
    return sorted_string
print(strsort('dfkgjadjkgkSBKFJS'))

def strsort_ver2(input_string):
    """Возьмите строку  и разбейте ее на отдель-
ные слова, а затем отсортируйте эти слова по алфавиту.
После сортировки напечатайте их с запятыми (,) между
именами."""
    input_string=input_string.split(' ')    
    sorted_string=sorted(input_string)
    sorted_string=','.join(sorted_string)
    return sorted_string
print(strsort('dfkgjadjkgkSBKFJS'))
print(strsort_ver2('Tom Dick Harry'))
filename=''
def clean_text(content):
    """Очистка строки от лишнего
    """
    words=content.split(' ')
    words = [word.strip('.,!?;:"()') for word in content.split()]
    return words
import open_close
def biggest_word():
    """Нахождение самого длинного слова"""
    filename='6.txt'
    content=open_close.file_open_one(filename)
    words=clean_text(content)
    longest = max(words, key=len)
    print(longest)
biggest_word()


def last_word():
    """Нахождение последнего слова"""
    filename='6.txt'
    content=open_close.file_open_one(filename)
    words=clean_text(content)
    print(words[-1])
last_word()