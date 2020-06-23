
def count1(x):
    z=list(dict.fromkeys(x))
    l=len(z)
    count1=[]
    for i in range(l):
        count1.append(0)
    for i in range(l):
        count1[i]=x.count(z[i])  
    z1=dict(zip(z,count1))
    return z1

x=input('Please enter a string:')
print(count1(x))


