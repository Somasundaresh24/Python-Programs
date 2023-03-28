def add():
    a=int(input("Enter First value : "))
    b=int(input("Enter Second value : "))
    return a+b, a-b, a*b, a/b
print(add())

def nn():
    n1=int(input("value 1: "))
    n2=int(input("value 2: "))
    print(n1**n2)
print(nn())

def num(m,m1):
    return(m*m1)

m=int(input("m1 value"))
m1=int(input(("m2 value")))

print(num(m,m1))
print(num(4,4))


def ab(c,d=4):
    return (c+d)
print(ab(2))
print(ab(3,9))

def addEn(x,y,z):
    print (x+y+z)
x,y,z= 4,5,6
print(addEn(x, y, z),end='')
