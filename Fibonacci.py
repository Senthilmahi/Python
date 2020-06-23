n=int(input('Enter the number of fibonacci numbers you need:'))
fn=[0,1]
for i in range(2,n):
    f=fn[i-1]+fn[i-2]
    fn.append(f)
for i in range(n):
    print(fn[i])

