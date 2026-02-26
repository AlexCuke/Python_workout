def strsort(input_string):
    """Сортирофка символов в строке"""
    sorted_string=sorted(input_string)
    sorted_string=''.join(sorted_string)
    return sorted_string
print(strsort('dfkgjadjkgkSBKFJS'))

def strsort_ver2(input_string):
    """Сортирофка символов в строке"""
    input_string=input_string.split(' ')    
    sorted_string=sorted(input_string)
    sorted_string=','.join(sorted_string)
    return sorted_string
print(strsort('dfkgjadjkgkSBKFJS'))
print(strsort_ver2('Tom Dick Harry'))
filename=''
def clean_text(content):
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