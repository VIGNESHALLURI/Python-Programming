"""#take list of 5elements print only even numbers in the list.
mylist = [21,23,43,56,78,82]
if mylist[0]% 2==0:
    print(mylist[0])
if mylist[1]% 2==0:
    print(mylist[1])
if mylist[2]% 2==0:
    print(mylist[2])
if mylist[3]% 2==0:
    print(mylist[3])
if mylist[4]% 2==0:
    print(mylist[4])
if mylist[5]% 2==0:
    print(mylist[5])

#Method:-2
mylist = [21,23,43,56,78,82]
for i in range(0,6):
    if mylist[i] % 2 == 0:
        print(mylist[i])

#method:-3
mylist = [21,23,43,56,78,82]
for i in range(0,len(mylist)):
    if mylist[i] % 2 ==0:
        print(mylist[i])"""

"""#take list of 10 numbers,count how many even numbers are there and odd numbers are there.

mylist=[10,11,13,14,15]
count=0
if mylist[0]%2==0:
    count = count + 1

if mylist[1]%2==0:
    count = count + 1
    
if mylist[2]%2==0:
    count = count + 1

if mylist[3]%2==0:
    count = count + 1

if mylist[4]%2==0:
    count = count + 1
    
print(count)"""

#take a  mylist =[10,12,13,14,15] count even numbers and odd numbers
mylist = [10,12,13,14,15]
ecount = 0
ocount = 0

if mylist[0] % 2 == 0:
    ecount += 1
else:
    ocount += 1

if mylist[1] % 2 == 0:
    ecount += 1
else:
    ocount += 1

if mylist[2] % 2 == 0:
    ecount += 1
else:
    ocount += 1

if mylist[3] % 2 == 0:
    ecount += 1
else:
    ocount += 1

if mylist[4] % 2 == 0:
    ecount += 1
else:                 
    ocount += 1 

print(ecount)
print(ocount)

#method2:
ecount = 0
ocount = 0
for i in range (0,len(mylist)):
    if mylist[i]%2 == 0:
        ecount = ecount +1
    else:   
        ocount = ocount + 1
print(ecount)
print(ocount)


