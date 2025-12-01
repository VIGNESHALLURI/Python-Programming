"""#read season from user if it is summer return validation time, if it is rainy return carry umbrella otherwise.
#if it is winter return its freezing cold.
def check(season):
    if season == "summer":
        return "validation time"
    elif season == "rainy":
        return "carry umbrella"
    elif season == "winter":
        return "it's freezing cold"
    else:
        return "invalid season"
res =check(input("Enter the season: "))
print(res)"""   

"""#leap year or not
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return f"{year} is a normal leap year"
    elif year % 400 == 0 and year % 100 == 0:
        return f"{year} is a century leap year"
    else:
        return f"{year} is not a leap year"
res = leap_year(int(input("enter a year:")))
print(res)"""

"""n = int(input("enter a number:"))
print("The number is",n)

# string formatting techigue
print(f"the number is ")"""

"""#Read one character from user and return wheather it is vowel or consonant?
char = input("enter a character: ")
if char == 'a' or char == 'e' or char == 'i' or char == 'e' or char == 'u':
    print(f"{char} is a vowel")
else:
    print(f"{char} is a constant")"""
"""def vowel(char):
    s = "aeiouAEIOU"
    if char in s:
        return f"{char} is a vowel"
    else:
        return f"{char} is a consonant"
res = vowel(input("enter a character:"))
print(res)"""

"""l = []
for i in range(10):
    ele = int(input("enter a number:"))
    l = l + [ele]
print(l)"""

"""#salary
def find(name,sal,exp):
    if exp > 5:
        inc = 10/100 * sal
        return f"The net salary is {sal+inc}"
    else:
        return f"The net salary is {sal}"
res= find("Rajesh",12000,6)
print(res)"""

"""def fetch(x):
    a = list(range(3,x,4))
    print(a)
fetch(int(input("enter a number:")))"""

"""def find(p1,p2,p3,p4):
    if p1 >= 13 and p1 <= 19:
        return "some is a teenager"
    elif p1 >= 13 and p1 <= 19:
        return "some is a teenager"
    elif p1 >= 13 and p1 <= 19:
        return "some is a teenager"
    elif p1 >= 13 and p1 <= 19:
        return "some is a teenager"
    else:
        return "no one is a teenager"
res = find(int(input("p1 age: ")),int(input("p2 age: ")),int(input("p3 age: ")),(int(input("p4 age: "))))
print(res)"""
# biggest number
def fetch(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return f"{n1} is the biggest"
    elif n2 > n1 and n2 > n3:
        return f"{n2} is the biggest"
    else:
        return f"{n3} is the biggest"
res = fetch(int(input("n1: ")),int(input("n2: ")),int(input("n3: ")))
print(res)


        




       






