#take an array / list of 10 random numbers. print elements in reverse order. 
#python students using for loop with ranges. java people should use a for loop. 
arr = [10,20,30,40,50,60,70,80,90,100]
for i in range(len(arr)-1,-1,-1):
    print(arr[i], end=" ")

#take an array / list of 10 random numbers. print alternate elements 0th, 2nd, 4th etc. 
#Python students use for loop with ranges. java should use a for loop. 
arr = [10,20,30,40,50,60,70,80,90,100]
for i in range(0,len(arr),2):
    print(arr[i], end=" ")

#take array 1/list1 with some random numbers. copy the elements of that array / list into a second array2 / list2.
list1 = [10,20,30,40,50]
list2 = []
for i in range(len(list1)):
    list2.append(list1[i])
print(list2) 

#take array 1/list1 with some random numbers. copy the elements of that array / list into a second array2 / list2 in reverse order 
list1 = [10,20,30,40,50]
list2 = []
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)

#take an array / list of 10 random numbers. write logic to count how many even nos are there and how many odd numbers are there.
arr = [12,15,8,7,20,13,10,5,18,9]
even_count = 0
odd_count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even =", even_count)
print("Odd =", odd_count) 

#take an array / list of 10 random numbers. find big in that array / list. don't use the max() function. 
arr = [10,50,20,90,30,70]
big = arr[0]
for i in range(1, len(arr)):
    if arr[i] > big:
        big = arr[i]
print("Biggest =", big)

#take an array / list of 10 random numbers. find even big and odd big in that array / list. don't use the max() function. 
arr = [12,45,78,23,90,55,67]
even_big = -1
odd_big = -1
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        if arr[i] > even_big:
            even_big = arr[i]
    else:
        if arr[i] > odd_big:
            odd_big = arr[i]
print("Biggest Even =", even_big)
print("Biggest Odd =", odd_big)

#take an array / list of 10 random numbers. copy even numbers into array2/list2. 
# copy odd numbers into array3/list3. don't use copy() or other copying methods. 
arr = [10,15,20,25,30,35]
list2 = []
list3 = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        list2.append(arr[i])
    else:
        list3.append(arr[i])
print("Even List =", list2)
print("Odd List =", list3)

#take arr1/list1, arr2/list2 with some random numbers. take an empty arr3/list3 of relevant size. 
#copy first arr1/list1 into arr3/list3. copy the next arr2/list2 elements into arr3/list3. 
list1 = [10,20,30]
list2 = [40,50,60]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i])
for i in range(len(list2)):
    list3.append(list2[i])
print(list3)

#take an arr / list with some numbers. print even nos present in the even positions. 
arr = [10,15,20,25,30,35,40]
for i in range(0, len(arr), 2):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")
        
#take 2 arrays / lists with some numbers. add both arrays / list into third array / list 
list1 = [10,20,30]
list2 = [1,2,3]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(list3)