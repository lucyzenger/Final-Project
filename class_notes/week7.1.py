# #write a function that takes a natural number as input and returns the number of digits the input has.
# #dont use any loops

# # numdigits = len(input("Enter a whole number: "))
# # print(f"The number of digits of the number you entered is {numdigits}")


# # def countlength(num):
# #     return len(str(num))
# # print(countlength(23))


# #random numbers
# import random

# rand_number1 = random.randint(1, 12)
# rand_number2 = random.randrange(1, 3)

# print("rand1:", rand_number1)
# print("rand2:", rand_number2)


# #math module
# #lists

# #heterogeneous data = bad
# mylist = ["Lucy", 23, True]
# for i in mylist:
#     print("i:", i)

# #homogeneous data = good
# grades = [98, 99, 45, 100]

# print(grades[0])
# print(grades[3])
# print(grades)

# # append function

# grades.append(100)
# print("grades post append:", grades)

# # for i in range(10):
# #     grades.append(0)

# print("grades after list append:", grades)

# # insert function

# grades.insert(0, 85)
# print("grades after insert:", grades)
# print(len(grades))

# # take stuff out of the list

# grades.pop() #takes out the end one unless specified against otherwise
# print("grades after pop:", grades)

# grades.remove(45)
# print("grades after remove:", grades)

# grades.append(85)
# grades.append(99)
# grades.append(100)
# print("grades:", grades)

# grades.remove(85)
# print("grades after remove:", grades)
# grades.remove(85)
# print("grades after remove:", grades)
# grades.pop(2) 
# print("grades after pop:", grades)




#colors
fav_aggies = ["Big Blue", "Justin Bean", "Mason Falslev"]

for aggie in fav_aggies:
    print("aggie:", aggie)

fav_aggies[2] += "Ian Martinez"
print("aggie", aggie)



