#Take a number and check whether it is prime or not.
n = int(input("Enter Number: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2 :
    print("Prime Number")
else:
    print("Not Prime Number")

#Print Fibonacci series up to n terms.
def fibo(n):
    n1 = 0
    n2 = 1
    count = 0

    while count < n:
        print(n1, end= " ")
        s = n1 + n2
        n1 = n2
        n2 = s
        count += 1
n = int(input("Enter number of terms: "))
fibo(n)

#Write a program to find the factorial of a given number.
def is_fact(n):
    fact = 1
    for i in range(1,n + 1):
        fact = fact*i

    return fact
res = is_fact(int(input("Enter a number:")))
print(res)

#Take a string and check whether it is a palindrome or not.
s = input("Enter String: ")
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev + s[i]
print("Reversed String =", rev)
if s == rev:
    print("Palindrome String")
else:
    print("Not Palindrome String") 

##Take a number and check whether it is Armstrong Number or not.
n = int(input("Enter Number: "))
temp = n
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit * digit * digit
    n = n // 10
if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number") 
