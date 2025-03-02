"""
Programming Activity 1

Write a program which can tell if a 3 digit number is a palindrome. 
 - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
 - Convert the user input into an integer (int). To get the first digit alone, floor division by 100. 
 - To get the 3rd digit alone, modulus by 10. 
 - Check if the first digit and 3rd digit are the same. 
 - If they are the same print("palindrome!!!!"). 
 - Else print("not palindrome!")
"""

#create variable
usernumber = int(input("Please enter a 3-digit number :"))
firstdigit = usernumber // 100
thirddigit = usernumber % 10
if firstdigit == thirddigit:
    print("Palindrome!")
else:
    print("Not palindrome!")


"""
Programming Activity 2

Write a program which can add up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?

"""

total = 0
numerator = 1
denominator = 2
for i in range(1000):
    total += (numerator/denominator)
    denominator **= 2
    print(total)
print(total)


"""
Programming Activity 3

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. 
Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""

# #ask for weight
age = int(input("What is your age?"))
weight = float(input("What is your weight?"))

if age >= 12:
    print("You can sit in the front")
if age == 11 and weight > 90:
    print("You can sit in the front")
if age < 11 and weight > 100:
    print("You can sit in the front")
else:
    print("You cannot sit in the front")

#boolean
rule1 = age >= 12
rule2 = age == 11 and weight > 90
rule3 = age > 11 and weight > 100

if rule1 or rule2 or rule3:
    print("Yes")
else:
    print("No")