class Dog:
    def addOne(self,x):
        return x+1
    def bark(self):
        print("Dog barks")

d=Dog()
d.bark()
print(d.addOne(4))
print(type(d))
 