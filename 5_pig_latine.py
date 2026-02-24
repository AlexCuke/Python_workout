def pig_latine_oldest() :
    """Пиг-Латин"""
    word = input('Введите слово: ')
    symbols='aiou'
    if word[0] in symbols:
        word=word+'way'
    else:
        word=word[1:]+word[0]+'ay'
    print (word)
#pig_latine_oldest() 
   
def pig_latine_old ():
    """Пиг-Латин"""
    word = input('Введите слово: ')
    symbols='aiou'
    if word[0] in symbols:
        word=word+'way'
    else:
        if word[0].isupper() is True : 
            word=word[1].upper()+word[2:]+word[0]+'ay'
        else:
            word=word[1:]+word[0]+'ay'
    print (word)
#pig_latine_old()

def pig_latine (word):
    """Пиг-Латин"""
    #word = input('Введите слово: ')
    symbols='aiou'
    symbols_two='!,.:;-'
    if word[-1:] in symbols_two:       
            if word[0] in symbols:
                word=word[:-1]+'way'+word[-1:] 
            else:
                if word[0].isupper() is True : 
                    word=word[1].upper()+word[2:-1]+word[0]+'ay'+word[-1:]
                else:
                    word=word[1:]-1+word[0]+'ay'+word[-1:]
    else:
        if word[0] in symbols:
            word=word+'way'
        else:
            if word[0].isupper() is True : 
                word=word[1].upper()+word[2:]+word[0]+'ay'
            else:
                word=word[1:]+word[0]+'ay'
    print (word)
pig_latine("Python")
pig_latine("Python!")
pig_latine("Input!")
pig_latine("output.")
pig_latine("output")

print()
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
    print(word)
pig_latine_ver2("Python")
pig_latine_ver2("Python!")
pig_latine_ver2("Input!")
pig_latine_ver2("output.")
pig_latine_ver2("output")
pig_latine_ver2("out")
pig_latine_ver2("egg!")
pig_latine_ver2("oogg!")