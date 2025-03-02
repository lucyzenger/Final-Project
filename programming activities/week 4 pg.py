"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""
#ask user what year they were born
birthyear = int(input("What year were you born: "))

#display message telling them what generation they belong to 
if birthyear > 2010:
    print("You are a Zoomer!")
elif birthyear > 1981:
    print("You are a Millenial!")
elif birthyear < 1965:
    print("You are a Gen X!")
elif birthyear < 1946:
    print("You are a Baby Boomer!")


"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""
currentyear = 2025
userage = int(input("What is your age: "))

while age > 1:
    print("You were alive in year:", currentyear)
    age -= 1
    currentyear -= 1
else: 
    print("You were born in year:", current year)


"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
for i in range(5,96,5):
    print("i:", i)
"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
y = 5
while y < 96:
    print("y:", y)
    y += 5
"""
1. Find all the prime numbers within a given range using a for loop

"""
primerange = int(input("Enter the upper end of the range for prime numebrs: "))

for i in range(1, primerange+1):
    if i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            print(i, "is prime")
