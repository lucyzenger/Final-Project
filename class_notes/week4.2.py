"""
1. Find all the prime numbers within a given range using a for loop

2. Write a Python program to reverse a given three or more digit integer WITHOUT using lists (hint, use // and % to isolate numbers)
"""

#1.
#for loops
#we loop over lists, range of numbers, string
days = ["Friday", "Saturday", "Sunday"]
for day in days:
    print("days:", days)
    
for i in range(8):
    print("i:", i)
    
for i in range(1,8):
    print("i:", i)

for letter in "applesauce":
    print("letter:", letter)

#while loops

i = 0

while i < 8:
    print("while i:", i)
    i = i + 1

#augmented assignment
age = 20
print("age:", age)
age += 1
print("age:", age)
age -= 1
print("age:", age)
age *= 2
print("age:", age)
age /= 3
print("age:", age)
age **= 2
print("age:", age)
age %= 2
print("age:", age)


#guess a secret number

import random

secret_number = random.randint(1, 100)
print("seceret_number:", secret_number)

userguess = int(input("Guess the secret number between 1 and 100: "))

while userguess != secret_number:
    if userguess < secret_number:
        print("You guessed too low. Try again.")
    elif userguess > secret_number: #elif bc you only want it to run if the first if didn't return true
        print("You guessed too high. Try again.")
    elif userguess > 100:
        print("The number is less than 101.")
  
    userguess = int(input("Guess the secret number between 1 and 100: "))
else:
    print("You guessed it!")
