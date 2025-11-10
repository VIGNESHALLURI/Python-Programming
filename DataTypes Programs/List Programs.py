"""numbers=[10,20,30,40]
#update the list["ten","twenty","thirty","fourty"]
numbers = numbers + ["ten"]
numbers = numbers + ["twenty"]
numbers = numbers + ["thirty"]
numbers = numbers + ["fourty"]
del(numbers[0:4])
print(numbers)"""

"""details = [1, "name","place","course"]
#print 1 & 2 elms using +ve index
print(details[0:2])
#print 3 & 4 elms using -ve index
print(details[-2:])"""

subjects = ["english","mathematics","science","computers","Hindi"]
#output should be ["english","mathematics","science"]
#output should be ["mathematics","science","computers"]
#output should be ["Hindi","computers","science"]
print(subjects[0:3])
print(subjects[1:4])
print(subjects[::-1][:3])





