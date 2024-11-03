#we have to sort a given list using obvious sort
#The algorithm is:  1.) find the minimum
#                   2.) append the minimum is new list
#                   3.) remove the minimum from the list

def mini(l):
    x= l[0]
    for i in range(len(l)):
        if l[i]<x:
            x=l[i]
    return x

def obvious(l):
    y=[]
    while len(l)>0:
        minim=mini(l)
        y.append(minim)
        l.remove(minim)
    return y

l=[1,4,876,86,3,97,44,9,2,5]
print(obvious(l))