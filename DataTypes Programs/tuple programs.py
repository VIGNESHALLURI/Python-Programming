numbers = (10,20,30,40,50,60,70,80,90)
#expected output: (10,30,50,70,90)
print(numbers[0::2])
#expected output: (20,40,60,80)
print(numbers[1::2])
#expected output: (90,70,50,30,10)
print(numbers[-1::-2])
#expected output: (80,60,40,20)
print(numbers[-2::-2])
#expected output: (20,30,40,50)
print(numbers[1:5])
#change 20 to Twenty
numbers = numbers[:1] + ("Twenty",) + numbers[2:]
print(numbers)
