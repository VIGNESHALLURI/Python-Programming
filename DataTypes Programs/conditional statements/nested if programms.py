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

    """"""

#