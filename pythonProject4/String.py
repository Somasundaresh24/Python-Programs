#string

Word='Hi Nanbha'
words="I have 5+years Exp in IT"
print(Word)
print(words)

Paragr=''' I am    #morethan one line
from Coimbatore
Looking for job    
in Bangalore
'''
print(Paragr)

name="Soma Sundaresh"
print(name)
print(name[6])

#slicing
name1=' ajay kumar '
print(name1[2:8])
print(name[3:9])

print(name[-8:-1])
print(name[-16:-1])

#length
print(len(name1))
print(len(name))

#strip
print(name1.strip())

#upper
print(name1.upper())
#lower
print(name1.lower())

#replace
a='Soma'
print(a.replace("s" , "dd"))


#split
print(a.split('o'))

#check
print('om' in a)

#concodinate
ab='arun'
bc=" kumar"
print(ab + bc)