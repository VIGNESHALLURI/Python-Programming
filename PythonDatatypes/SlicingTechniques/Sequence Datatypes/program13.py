#take 2 arrays / lists with some numbers. add both arrays / list into third array / list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
elementwise_sum = [a + b for a, b in zip(list1, list2)]
concatenated_list = list1 + list2
print("Element-wise sum:", elementwise_sum)
print("Concatenated list:", concatenated_list)
