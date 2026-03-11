def funk_find():
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
    
    for file in files:
        f=os.path.splitext(file)

funk_find()
        