#sort the array / list, without using sort() function.
arr = [5, 2, 8, 1, 4]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)

#take an array / list with some numbers. find the second biggest number with only one for loop.
#don't sort. don't use max()
arr = [10, 45, 22, 90, 75]
biggest = arr[0]
second = arr[0]
for i in range(1, len(arr)):
    if arr[i] > biggest:
        second = biggest
        biggest = arr[i]
    elif arr[i] > second:
        second = arr[i]
print(second)

#take an array / list with random 0's 1's. move 0's to left and 1's to right. don't sort.
arr = [1, 0, 1, 0, 1, 0, 0, 1]
count = 0
for i in range(len(arr)):
    if arr[i] == 0:
        count = count + 1
for i in range(count):
    arr[i] = 0
for i in range(count, len(arr)):
    arr[i] = 1
print(arr)

#find the factorial of a number with recursion.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
num = 5
print(factorial(num))

#take a string. find the largest substring with unique letters. if any letter repeats you have to stop
#there.
s = "AndhraPradesh"
result = ""
for ch in s:
    if ch in result:
        break
    result = result + ch
print(result)

#39. search for an element in the array / list. print the position. if element is not found, print -1.
arr = [10, 20, 30, 40, 50]
key = 40
position = -1
for i in range(len(arr)):
    if arr[i] == key:
        position = i
        break
print(position)