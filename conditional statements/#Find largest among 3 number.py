#Find largest among 3 number
num1 =int(input("enter a first:"))
num2 =int(input("enter a second:"))
num3 =int(input("enter a third:"))

if num1 > num2 and num1 > num3:
    print("print num1 is largest")
if num2 > num1 and num1 > num1:
    print("print num2 is largest")
else:
    print("print num3 is largest")