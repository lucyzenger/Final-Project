"""
Programming interveiwi quesiton asked by uber:

given an array of integerse, retyrn a new array such that each element at index i of the new array is the 

"""

#range function

for i in range(1, 20, 2):
    print("i:", i)

range(2)
range(4, 6)
range(3, 5, 2)
    
for i in range(20, 1, -2):
    print("i:", i)

#nested statements

for i in range(12):
    while True:
        if True:
            for i in range(1):
                if False:
                    print("I dont know how you got here :0")


# sentinal values

sentinal = 0

while sentinal != -1:
    sentinal = int(input("Enter a number (enter -1 to quit)"))

# example with sentinals
# upgrade code to include a 2nd player
# include a sentinal value to quit game at anytime

import random
# set up sentinal and other variables
sentinal = 0
player = 1
secret_number = random.randint(1, 100)
print("Welcome to the number guessing game! Decide who is player 1 and player 2 then player 1 enter your first guess :")
userguess = int(input("Guess the secret number between 1 and 100: "))

# while loop while userguess != secret_number and userguess != -1::

while True:
# if at anytime sentinal is selected, then quit

# check to see which player's turn it is... if player ==1:

for i in range(2, 1, -1): #nto sure if this will work
    print("player", i, "make a guess:")
    userguess = int(input())
# implement old code
    if userguess < secret_number:
            print("You guessed too low. Try again.")
    elif userguess > secret_number: #elif bc you only want it to run if the first if didn't return true
        print("You guessed too high. Try again.")
    elif userguess > 100:
         print("The number is less than 101.")
        elif guess == -1:
            print("thanks for playing")
            break

else:
    print("You guessed it!")

 
# # implement old code
#     if userguess < secret_number:
#             print("You guessed too low. Try again.")
#     elif userguess > secret_number: #elif bc you only want it to run if the first if didn't return true
#         print("You guessed too high. Try again.")
#     elif userguess > 100:
#          print("The number is less than 101.")
# # switch turns from 1 to 2 or 2 to 1
# # if secret number is guessed correctly, then end

# secret_number = random.randint(1, 100)
# print("secret_number:", secret_number)

# userguess = int(input("Guess the secret number between 1 and 100: "))

# while userguess != secret_number:
#     if userguess < secret_number:
#         print("You guessed too low. Try again.")
#     elif userguess > secret_number: #elif bc you only want it to run if the first if didn't return true
#         print("You guessed too high. Try again.")
#     elif userguess > 100:
#         print("The number is less than 101.")
  
#     userguess = int(input("Guess the secret number between 1 and 100: "))
# else:
#     print("You guessed it!")


