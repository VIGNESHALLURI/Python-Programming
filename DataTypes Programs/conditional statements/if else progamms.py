"""#create a function which is reading an int value and returning 
# wheather it is positive or negative numbers.
def check(n):
    if n > 0 :
        return "positive number"
    else:
        return "negative number"
res=check(int(input("enter a number:")))
print(res)"""

"""#write a program to check wheather the given number is even or odd?
def check(n):
    if n %2==0:
        return "even number"
    else:
        return "odd number"
res=check(int(input("enter a number:")))
print(res)"""

"""#write a program to check if the given string is palindrome or not?
def fetch(s):
    if s == s[::-1]:
        return "palindrome" 
    else: 
        return "not palindrome"
res = fetch(input("enter a string:")) 
print(res)"""

"""#write a program to check if the given number is 5 multiple or not and return the result?
def check(n):
    if n % 5 == 0:
        return "given number is multiple of 5"
    else:
        return "given number is not multiple of 5"
res=check(int(input("enter a number")))
print(res)"""

"""#write a program to check wheather the length of both the strings is same or different?
def checking(s,s1):
    if len(s) == len(s1):
        return "both the length are same"
    else:
        return "both the lenths are different"
res = checking(input("enter a string1:"),input("enter a string2:"))
print(res)"""

#write a program which is reading length and breadth and return wheather it is a square or rectangle?
def check(l, b):
    if l + b == l ** b:
        return "square"
    else:
        return "rectangle"
res = check(int(input("enter a number1: ")), int(input("enter a number2: ")))
print(res)





