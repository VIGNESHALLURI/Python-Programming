#take a string, reverse the string and print it. check if it is a palindrome string or not. python students should not use [::-1] 
s = input("Enter String: ")
rev = ""
for i in range(len(s)-1, -1, -1):
    rev = rev + s[i]
print("Reversed String =", rev)

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#take a string. count how many vowels are there in the string. you have considered both small letters and capital letters. 
s = input("Enter String: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels =", count)

#take a string. replace vowels in the string with letter z. After that print the string. 
s = input("Enter String: ")
result = ""
for ch in s:
    if ch in "aeiouAEIOU":
        result += "k"
    else:
        result += ch
print(result)

#take a string, count how many words are there. assume that there are no extra spaces in the string and there are no spaces at the beginning and and the end.
s = input("Enter Statement: ")
count = 1
for ch in s:
    if ch == " ":
        count += 1
print("Words =", count) 

#take 2 strings. find those 2 strings are anagrams. if 2 strings are of same length, and made up of same letters with dif combinations then it is anagram. 
s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")
if len(s1) != len(s2):
    print("Not Anagram")
else:
    flag = True
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            flag = False
            break
    if flag:
        print("Anagram")
    else:
        print("Not Anagram")

#take a string. write logic to count how many no of times each letter is repeating in that string.[letter occurrences] 
s = input("Enter String: ")
printed = ""
for i in range(len(s)):
    if s[i] not in printed:
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        print(s[i], "=", count)
        printed += s[i]

#take a statement. print words in the reverse order. eg: "palle tech pvt ltd" . output : ltd pvt tech palle. student can use split() function 
s = input("Enter Statement: ")
words = s.split()
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

#take a statement. print words in the reverse order. eg: "palle tech pvt ltd" . output : ellap hcet tvp dtl. student can use split() function 
s = input("Enter Statement: ")
words = s.split()
for word in words:
    rev = ""
    for i in range(len(word)-1, -1, -1):
        rev += word[i]
    print(rev, end=" ")

#take a string, print unique letters present in the string.
s = input("Enter String: ")
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count == 1:
        print(s[i], end=" ") 

#take a string, print duplicate letters present in the string. 
s = input("Enter String: ")
printed = ""
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count > 1 and s[i] not in printed:
        print(s[i], end=" ")
        printed += s[i]
