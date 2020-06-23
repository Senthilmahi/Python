def onlypos(a):
    a=a.split(",")
    l=len(a)
    b=[]
    for i in range(l):
        a[i]=int(a[i])
        if a[i]>=0:
            b.append(a[i])
    return b
            


list1=input('Enter list 1:')
list2=input('Enter list 2:')
print('list1=',onlypos(list1))
print('list2=',onlypos(list2))
