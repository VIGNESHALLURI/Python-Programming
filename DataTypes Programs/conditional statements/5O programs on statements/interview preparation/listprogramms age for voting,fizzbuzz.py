"""##you are given ages of 5 personds if age <18  print not eligible for voting else print eligible for voting.
mylist =[12,17,18,29,34]
if mylist[0] < 12:
    print('kid')
elif mylist[0] < 18:
    print('not eligible for voting')
else:
    print('eligible for voting')
if mylist[1] < 12:
    print('kid')
elif mylist[1] < 18:
    print('not eligible for voting')
else:
    print('eligible for voting')
if mylist[2] < 12:
    print('kid')
elif mylist[2] < 18:
    print('not eligible for voting')
else:
    print('eligible for voting')
if mylist[3] < 12:
    print('kid')
elif mylist[3] < 18:
    print('not eligible for voting')
else:
    print('eligible for voting')
if mylist[4] < 12:
    print('kid')
elif mylist[4] < 18:
    print('not eligible for voting')
else:
    print('eligible for voting')

#method2:-
mylist =[12,17,18,29,34]
for i in range(0,5):
    if mylist[i]<12:
        print('kid')
    elif mylist[i]<18:
        print('not eligible for voting')
    else:
        print('eligible for voting')

#method3:-
mylist =[12,17,18,29,34]
for i in range(0,len(mylist)):
    if mylist[i]<12:
        print('kid')
    elif mylist[i]<18:
        print('not eligible for voting')
    else:
        print('eligible for voting')"""


#take a list of five numbers. For each number in the list, check its divisibility and print the following:
#If the number is divisible only by 3, print ‘Fizz’. If the number is divisible only by 5, print ‘Buzz’.
#  If the number is divisible by both 3 and 5, print ‘FizzBuzz’.
# If the number is number is divisible by either 3 or 5, then print the number itself.”
mylist=[10,34,45,6,20]

if mylist[0] % 3 == 0 and mylist[0] % 5 == 0:
    print("FizzBuzz")
elif mylist[0] % 3 == 0:
    print("Fizz")
elif mylist[0] % 5 == 0:
    print("Buzz")
else:
    print("num") 

if mylist[1] % 3 == 0 and mylist[1] % 5 == 0:
    print("FizzBuzz")
elif mylist[1] % 3 == 0:
    print("Fizz")
elif mylist[1] % 5 == 0:
    print("Buzz")
else:
    print("num") 

if mylist[2] % 3 == 0 and mylist[2] % 5 == 0:
    print("FizzBuzz")
elif mylist[2] % 3 == 0:
    print("Fizz")
elif mylist[2] % 5 == 0:
    print("Buzz")
else:
    print("num") 

if mylist[3] % 3 == 0 and mylist[3] % 5 == 0:
    print("FizzBuzz")
elif mylist[3] % 3 == 0:
    print("Fizz")
elif mylist[3] % 5 == 0:
    print("Buzz")
else:
    print("num") 

if mylist[4] % 3 == 0 and mylist[4] % 5 == 0:
    print("FizzBuzz")
elif mylist[4] % 3 == 0:
    print("Fizz")
elif mylist[4] % 5 == 0:
    print("Buzz")
else:
     print('num')

#method2:-
mylist=[10,34,45,6,20]
for i in range(0,5):
    if mylist[i] % 3==0 and mylist[i] % 5 == 0:
        print('fizzbuzz')
    elif mylist[i] %3==0:
        print('fizz')
    elif mylist[i] %5==0:
        print('buzz')
    else:
        print('num')

#method3:-
mylist=[10,34,45,6,20]
for i in range(0,len(mylist)):
    if mylist[i] % 3==0 and mylist[i] % 5 == 0:
        print('fizzbuzz')
    elif mylist[i] %3==0:
        print('fizz')
    elif mylist[i] %5==0:
        print('buzz')
    else:
        print('num')



   

