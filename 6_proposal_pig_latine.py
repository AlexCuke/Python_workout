def pig_latine_ver2 (word):
    """Пиг-Латин"""
    #word = input('Введите слово: ')
    symbols='aiou'
    symbols_new=['a','i','o','u']
    symbols_two='!,.:;-'
    first_letter=word[0] 
    last_letter=word[-1]   
    if last_letter in symbols_two:
        word=word[:-1]        
    if word[0] in symbols:
        num_of_symb=0
        for symbol in symbols_new:
            if symbol in word:
                num_of_symb+=1
                continue
        if num_of_symb > 1:
            word=word[:-1]+'way' 
        else:
            word=word[1:]+word[0]+'ay'
    else:
        word=word[1:]+word[0]+'ay'
    if last_letter in symbols_two:
        word=word+last_letter
    if first_letter.isupper() is True:
        word=word.capitalize()
    return word

def pl_sentence(sentence):
    print(sentence)
    """Пиг-Латин"""
    #word = input('Введите слово: ')
    sentence_split=sentence.split(' ')
    sentence_new=[]
    for word in sentence_split:
        word=pig_latine_ver2(word)
        sentence_new.append(word)
    sentence=' '.join(sentence_new)
    print(sentence)

#pl_sentence("Crane was traveling from the United States to Cuba as a newspaper reporter. One night, his ship hit a sandbar. It sank in the Atlantic Ocean, off the coast of Florida. Most of the people on board got into lifeboats. Crane was among the last to leave. There were three others with him: the ship’s captain, the cook, and a sailor.")
import os
words=[]
table=[]
with open('6.txt', 'r') as f:
    number=0
    for line in f:       
        words=line.split()
        if len(words)> number:
            table.append(words[number])
            number+=1
        else:
            break       
        table.append(words[number])
        number+=1
print(' '.join(table))

def transpartent_words(matrix_word):
    matrix_word_new=[]
    for words in matrix_word:
        words=words.split(' ')
        matrix_word_new.append(words)
    print(matrix_word_new)
    matrix_word = [[matrix_word_new[i][j] for i in range(len(matrix_word_new))] for j in range(len(matrix_word_new[0]))]
    matrix_word_new=[]
    print(matrix_word)
    for words in matrix_word:
        words=' '.join(words)
        matrix_word_new.append(words)
    print(matrix_word_new)
    return  matrix_word_new
matrix_word=['abc def ghi','jkl mno pqr','stu vwx yz']
#transpartent_words(matrix_word)

def apache_log(error_number):
    import os
    with open('apache.log', 'r') as f:
        for line in f:    
            if str(error_number) in line:
                words=line.split()
                print(f'{words[0]} - ошибка {error_number}')
        
apache_log(404)