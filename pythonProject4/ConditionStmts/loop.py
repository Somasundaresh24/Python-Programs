#loops

name ='soma sundaresh'

#for loop

for letters in name:
    print(letters)

fruits=['apple', 'orange','fig','banana']
for fruit in fruits:
    print(fruit)

for i in "Hello loop":
    if i==" ":
        continue
        print(" space is present")
        #break
    else:
        print("space not present")

#range

for num in range(4):    #4  op:0 1 2 3
    print(num)
for num1 in range(1 ,6):    #4  op: 1 2 3 4 5
    print(num1)
for num2 in range(10,20,3):
    print(num2)

for num3 in range(5):
    print(num3)
    for i in range(2):
        print(i)
else:
    print("all numbers are printed")