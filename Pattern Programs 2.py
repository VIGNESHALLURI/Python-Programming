"""
1
22
333
4444
"""
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()
"""
1
12
123
1234
"""
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()
"""
a
ab
abc
abcd
"""
for i in range(1, 5):
    for j in range(i):
        print(chr(97 + j), end="")
    print()
"""
a
bb
ccc
dddd
"""
for i in range(1, 5):
    for j in range(i):
        print(chr(96 + i), end="")
    print()
"""
1
23
456
78910
"""
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()
