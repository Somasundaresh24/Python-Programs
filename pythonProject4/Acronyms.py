user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i).upper()
print(a)