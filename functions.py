
def most_frequent(x):
    z=list(dict.fromkeys(x))
    l=len(z)
    count1=[]
    for i in range(l):
        count1.append(0)
    for i in range(l):
        count1[i]=x.count(z[i])
    z1=dict(zip(z,count1))
    z2=sorted(z1.items(),key=lambda x: x[1], reverse=True)
    return z2

x=input('Please enter a string:')
print(most_frequent(x))


