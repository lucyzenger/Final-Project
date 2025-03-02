

# # list slicing
# prices = [123.56, 32.9, 87.99, 100.40, 456.78]

# subset_prices = prices[1:3]
# print("subset_prices:", subset_prices)

# # everything except last element
# last_element = prices[:-1]
# print("last_element:", last_element)

# # last element
# last_ele_for_real = prices[-1:]
# print("last_element:", last_ele_for_real)

# # reverse a list
# rev_prices = prices[::-1]
# print("reversed_prices:", rev_prices)

# # every third element
# every_other = prices[::3]
# print("every_third:", every_other)

# #attempting something 0.0
# n = 3
# test_slice = prices[0.n]
# print("test_slice:", test_slice)

# #list sorting
# list1 = [5, 7, 1, 9]
# list2 = [2, 10, 8, 4]

# print(list1.sort())
# print("list1:", list1)



name = "Lucy"
name2 = "Caroline"
letter_list = []
for letter in name: 
    letter_list.append(letter)
print("list before sorting:", letter_list)
letter_list.sort()
print("list after sorting:", letter_list)