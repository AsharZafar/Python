def fun(x):
    if x%2==0:
        return 1
    else:
        return 2
print(fun(fun(2)))


l1=[[x for x in range(3)]for y in range(3)]
for r in range(3):
    for c in range(3):
        if l1[r][c]%2!=0:
            print('#')


t=(1,2,4,8)
t=t[-2:-1]
t=t[-1]
print(t)


z=0
y=0
x=y<z and z>y or y>z and z<y
print(x)


def f(x,y):
    if x==y:
        return x
    else:
        return f(x, y-1)
print(f(0,3))

lst=[i for i in range(-1,-2)]
print(len(lst))

a=1
b=0
a=a^b
b=a^b
a=a^b
print(a,b)


l=[x*x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(l))





foo=(1,2,3)
foo.index(0)
i=0
while i<i+2:
    i+=1
    print("*")
else:
    print("*")