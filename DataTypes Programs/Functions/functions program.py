"""#function with 1 parameter and pass a list and print it.
def show(numbers):
    print("The list is:",numbers)
show([1,2,3,4,5])"""

"""#function with 1 parameter and pass a tuple and print it.
def show(numbers):
    print("The tuple is:",numbers)
show((50,60,70,80))"""

"""#create a function with 2 parameters and pass 2 arguments then print their reversed and concatinated result.
def f1(s1,s2):
    res=s1[::-1] + s2[::-1]
    print(res)
f1(input("enter a string value 1:"),input("enter a string value 2:"))"""

"""#create a function with 1 parameter and read string as an argument then print alternate, reverse alternate characters.
def f(s):
    print(s[::2],s[::-1],s[::-2])
f(input("enter a string:"))"""

def f1(a, b):
    print(a)
    print(b)
f1(10, (15, 60))
f1(5, 5, True, 'hi')
f1((100, 250, "hello"))
f1([1, 2, 3], {'hi', 'hello'}, 20)
f1(150, 200)