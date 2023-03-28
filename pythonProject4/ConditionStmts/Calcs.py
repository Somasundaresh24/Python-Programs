#simple Calculator

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modlo(a,b):
    return a%b

print("""Select operations
1.add
2.sub
3.mul
4.div
5.modulo """)

choice=int(input("Enter Ur Choice : "))
a=int(input("Enter Ur 1st number : "))
b=int(input("Enter Ur 2nd number : "))

if choice == 1:
    print(add(a,b))
elif choice ==2:
    print(sub(a,b))
elif choice == 3:
    print(mul(a,b))
elif choice ==4:
    print(div(a,b))
elif choice ==5:
    print(modlo(a,b))
else:
    print("Enter valid Choice")
