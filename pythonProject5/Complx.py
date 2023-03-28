# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)

# a =int (input("value"))
# for i in range(a):
#   print(i,end=' ' )

lst=[10,30,40,60]
for j in lst:
  if j ==40:
    break
  else:
    print("40")

ls=[10,30,40,60]
print((10*2)in ls)
print(ls[-1]+ls[1])

tup=(10,20,30,40,60)
print(tup[1:5])
print(type(tup))

sr ='troll geek'
lst=sr.split()
print(lst)

st='HEL LO'
i=st.isupper() and st.isspace()
j=st[0:3].isupper() or st.isspace()
k=st[0:3]
print(int(i))
print(int(j))
print(int(i)+int(j)+5)
print(k)

dict={1:"one",2:"two"}
Lst=list(dict)
print(Lst)