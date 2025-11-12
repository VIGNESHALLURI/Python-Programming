#eligible for vote or not
def check(age,gen):
    if age >= 18:
        if gen == 'male':
            return "you are eligible to vote sir"
        elif gen == 'female':
            return "you are eligible to vote ma'am"
        else:
            return "you are eligible to vote "
    else:
        return "you are not eligible to vote "
res = check(int(input("age: ")),input("gender: "))
print(res)

"""#biggest out of 3 numbers (using nested if)
num = int(input("enter a number:"))
if num % 3 == 0 and num % 5 == 0:
    print('fizzbuzz')
elif num % 3 == 0:
    print('fizz')
elif num % 5 == 0:
    print("buzz")
else:
    print("buzzfizz")"""
