def Obvious_sort(l):
    nl=[]
    while len(l)>0:
        mini = l[0]
        for i in range(len(l)):
            if l[i]<mini:
                mini=l[i]
        nl.append(mini)
        l.remove(mini)
    return nl

l= list(input("Enter value"))
print(Obvious_sort(l))