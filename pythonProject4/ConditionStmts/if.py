#if statements

age=  30
if age > 18:
    print("Eligeble to vote")
elif age==18:
    print("Apply for vote id")
else:
     print("Not Eligeable to vote")

a, b = 25, 50
if a==10 and b==30:    #and
     print("values are correct")
else:
     print("values are wrong")

a1, b1 = 25, 50
if a1==10 or b1==50:  #or
     print("values are correct")
     if a1==25:
         print("Welcome")
else:
     print("values are wrong")