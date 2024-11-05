def dict_fromString(string, key, value):

    l=string.split()
    dict={}
    for i in l:
        x=i.split(',')
        dict[key(x[0])]=value(x[1])
    return dict

string='''aatish,26
    bantu,25
    simant,26
    malli,32
    '''
key=str
value=int
print(dict_fromString(string, key, value))