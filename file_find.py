'''def funk_find():
    """Используйте os.listdir, чтобы получить имена файлов
    в текущем каталоге. Какие расширения файлов (т.е. суф-
    фиксы, следующие за конечным символом «.») находятся
    в этом каталоге? Вероятно, будет полезно использовать
    os.path.splitext.
        """
    import os
    
    files=os.listdir()
    f=os.path.splitext('.')
    file_rash=[]
    table_of_contents={}
    
    for filename in files:
        f=os.path.splitext(filename)
        if f[1]==('.py'):
            func={}
            with open(filename, 'r', encoding='utf-8') as file:
                content=file.read()
                #print(type(content))
                lines=content.split('\n')
                func_inc=[]
                for i,line in enumerate(lines):
                    if 'def' in line:
                        a=3
                        if '"""' in lines[i+1]:
                            comment=''
                            line_clean=line.split('def')
                            func_name=line_clean[1].split(' ')[1]
                            for comment_line in lines[i+1:]:
                                comment=comment+lines[i+1]
                                if '"""' in comment_line:
                                    break
                                
                            func.setdefault(func_name,comment)


                            #print(full_content)
                    table_of_contents.setdefault(filename,func)
    for keys,values in table_of_contents.items():
        print(f'Название файла:{keys} Название функции:{values}')                
              
    #print(table_of_contents)

                        
                         

funk_find()
        '''
        
def funk_find():
    """Вывожу список всех функций в файлах
        """
    import os
    
    files=os.listdir()
    f=os.path.splitext('.')
    file_rash=[]
    #table_of_contents={}
    table_of_func={}
    func_tuple=[]
    for filename in files:
        f=os.path.splitext(filename)
        if f[1]==('.py'):
            with open(filename, 'r', encoding='utf-8') as file:
                content=file.read()
                #print(type(content))
                lines=content.split('\n')
                for i,line in enumerate(lines):
                    if 'def' in line:
                        func_inc=[filename]
                        if '"""' in lines[i+1]:
                            comment=''
                            line_clean=line.split('def')
                            func_name=line_clean[1].split(' ')[1]
                            func_tuple.append(func_name+filename)
                            newline=lines[i+1:]
                            for comment_line in newline:
                                
                                comment=comment+comment_line
                                if '"""' in comment_line:
                                    comment=comment.split('"""')
                                    comment=func_inc.append(comment[1])   
                                    break
                                                
                            table_of_func.setdefault(func_name,func_inc)


                            #print(full_content)
                    #table_of_contents.setdefault(filename,func)
    #for keys,values in table_of_contents.items():
    #    print(f'Название файла:{keys} Название функции:{values}')              
    for keys,values in table_of_func.items():
        print(f'Функция: {keys} : {values}')    
    print(len(table_of_func))  
    func_tuple.sort()
    #print(func_tuple)               
    #print(table_of_contents)

                        
                         

funk_find()
        