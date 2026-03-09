def dictdiff(first,second):
    all_keys=first.keys()|second.keys()
    return all_keys
a={'a':1, 'b':2, 'c':3}
b={'a':1, 'b':2, 'c':4}

result=dictdiff(a,b)
print(result)