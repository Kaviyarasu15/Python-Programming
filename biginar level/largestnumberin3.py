a1 = float(input("Enter first number: "))
a2 = float(input("Enter second number: "))
a3 = float(input("Enter third number: "))
 
if (a1 > a2) and (a1 > a3):
   largest = a1
elif (a2 > a1) and (a2 > a3):
   largest = a2
else:
   largest = a3
 
print("The largest number is",largest)
