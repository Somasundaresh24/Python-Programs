#list
fruits=['apple','orange','banana','cheery']
print(fruits)
print(fruits[1:2])
print(fruits[0])
print(fruits[-5:-1])
fruits[3]='mango'
print(fruits)
print(fruits[-1])
print(len(fruits))
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
fruits.append('fig')
print(fruits)
fruits.reverse()
print(fruits)
fruits.remove('mango')
print(fruits)


num=[89,6,23,64,36,9,24]
add=num+fruits
print(add)