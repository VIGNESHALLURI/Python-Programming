#Print 1,2,3,..99,100 using for loop. 
for i in range(1,101):
    print(i)

#Print 0,2,4,6,..98,100 using for loop. 
for i in range(0,101,2):
    print(i)

#Print take a no find even or odd 
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#swap with temp and without temp 
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a, b)

#print 1-10 first line, 2-20 second line etc. up to 100. 
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

#read a char, find vowel are not with if else, with switch also. 
ch = input("Enter character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Not Vowel")

#read age, find if a person is eligible for voting. 
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible")
