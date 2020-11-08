import math

print("Please select operation 1-7")
print("1. +")
print("2. -") 
print("3. *")
print("4. /")
print("5. sin")
print("6. cos")
print("7. tan")
operation = int(input("Menu No: "))

# Two number operations
if operation>=1 and operation<=4:
  num1 = float(input("Please input first number: "))
  num2 = float(input("Please input second number: "))
  if operation == 1:
    print (num1,"+",num2,"=",(num1+num2))
  elif operation == 2:
    print (num1,"-",num2,"=",(num1-num2))
  elif operation == 3:
    print (num1,"*",num2,"=",(num1*num2))
  elif operation == 4:
    print (num1,"/",num2,"=",(num1/num2))
elif operation>=5 and operation<=7:
  num = float(input("Please input number: "))
  if operation == 5:
    print("sin(",num,") = ",math.sin(num))
  elif operation == 6:
    print("cos(",num,") = ",math.cos(num))
  elif operation == 7:
    print("tan(",num,") = ",math.tan(num))
else:
  print ("Invalid Option. Please try again!")
  exit()