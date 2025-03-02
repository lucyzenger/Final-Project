"""
Programming Activity 1

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""

colors = ["pink", "purple", "green"]
for color in colors:
    print("color:", color)


"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, 
but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""

colors = ["pink", "purple", "green"]
for color in colors:
    print("color:", color)
    for letter in color:
        print("letter:", letter)

"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
import random

something = []

for x in range(10):
    # x = random.randint(4, 40)
    # something.append(x)
    something.append(random.randint(4, 40))

print(something)

"""
Programming Activity 4 

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""

import random

something = []
for x in range(10):
    something.append(random.randint(4, 40))
print("something:", something)
count = 0
for num in something:
    if count == 10:
        break
    else:
        # print(something[count], something[count+1])
        if something[count] % 2 == 0 and something[count + 1] % 2 == 0:
            print("found two evens in a row!")
            print(something[count], something[count+1])
        count += 1


"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""
file = open("/home/ubuntu/programming activities/aapl.txt")
lines = file.readlines()
print("lines:", lines)
prices = []
for line in lines:
    line = float(line)
    prices.append(line)
print("prices:", prices)

# Calculate the average for the entire dataset
total_avg = sum(prices) / len(prices)
print(f"Total Average Price for the Year: ${total_avg:.2f}")

# Calculate the average for the first 5 days
if len(prices) >= 5:
    five_day_avg = sum(prices[:5]) / 5
    print(f"5-Day Moving Average: ${five_day_avg:.2f}")
else:
    print("Not enough data for a 5-day moving average")
"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homework.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""

file = open("/home/ubuntu/programming activities/aapl.txt")

lines = file.readlines()

#print("lines:", lines)
prices = []

for line in lines:
    line = float(line)
    prices.append(line)

print("prices:", prices)




