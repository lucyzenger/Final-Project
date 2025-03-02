# 1 Obtaining data from a web JSON API (40 points)
# 2 Storing the data in CSV files on your AWS Cloud9 server (40 points)
# 3 Reverse and append: The ability to add new data to your dataset.  Meaning, tomorrow you can run your program again, and it will go get the latest data, and run your analysis again. (40 points)
# 4 Perform analysis on the data. (40 points)  *** I am starting to do this with the moving average

import requests
import json #import JSON library to read JSON data

#define stock ticker symbol
ticker = 'AAPL'
#URL to extract daily stock prices from Alpha Vantage
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
print(url)

#send request to API and store the response
req = requests.get(url)
#convert the API response from JSON to a python dictionary
req_dict = json.loads(req.text) 
#json.dump(rqst_dictionary, open("results.json", "w"))
print(req_dict.keys())

#define keys to extract data
key1 = "Time Series (Daily)"
key2 = "4. close"

#open csv file that stores the previous stock data
fil = open(ticker + ".csv", "r")
lines = fil.readlines()
#extract the last recorded date from csv file
last_date = lines[-1].split(",")[0]

#list to store new stock price data
new_lines = []
for date in req_dict[key1]:
    if date == last_date:
        break #stop adding data once the last recorded date is reached
        print(date + "," + req_dict[key1][date][key2]) #print date and closing price
        new_lines.append(date + "," + req_dict[key1][date][key2]+"\n") #append the data to the list

#reverse the order fo the new data so it goes oldest to newest date
new_lines.reverse()
#open csv file in append mode and write new data
fil = open(ticker + ".csv", "a")
fil.writelines(new_lines) #append the new stock prices to the csv file
fil.close() #close the file


#these are notes i have so far on the 2 strategies taht i will perfect to turn in for the final project. still learning!

# Strategy #1: Mean reversion average trading strategy logic
# if price < avg * .98:
#    print("buy at: ", price)
# elif price > avg * 1.02:
#    print("sell at: ", price)
# else:
#    pass

# Strategy #2: Simple moving average trading strategy logic *** (i have included notes to help get me started with the moving average when that time comes)

      # the basic logic, explained above, will look like this
      # this is not the complete logic, but you are allowed to copy/paste and start with this

# tickerlist = []
# for price in req_dict[key2]:

# Current_price = #the next price in the list
# Avg_price = #average price for the 5 previous days
# if current_price < average * 0.98:
#     #buy
#     #update buy variable
#     #update first_buy variable if this is the first time you buy
# elif current_price > average * 1.02:
#     #sell
#     #calculate profit of this individual trade
#     #keep a running total of all profit
# else: 
    # do nothing this iteration
# if price > avg:
#    print("buy at: ", price)
# elif price < avg:
#    print("sell at: ", price)
# else:
#     pass

# # Calculate the average for the entire dataset
# total_avg = sum(prices) / len(prices)
# print(f"Total Average Price for the Year: ${total_avg:.2f}")

# # Calculate the average for the first 5 days
# if len(prices) >= 5:
#     five_day_avg = sum(prices[:5]) / 5
#     print(f"5-Day Moving Average: ${five_day_avg:.2f}")

# Extract dates and closing prices
# for line in lines:
#     parts = line.strip().split(",")
#     dates.append(parts[0])
#     prices.append(float(parts[1]))

# # Ensure we have at least 5 days of data
# if len(prices) >= 5:
#     for i in range(len(prices) - 4):
#         five_day_avg = sum(prices[i:i+5]) / 5  # Calculate 5-day moving average
#         print(f"Date: {dates[i+4]}, 5-Day Moving Avg: {five_day_avg:.2f}, Closing Price: {prices[i+4]:.2f}")

#         # Apply Mean Reversion Strategy
#         if prices[i+4] < five_day_avg * 0.98:
#             print(f"BUY signal on {dates[i+4]} (Price: {prices[i+4]:.2f}, Below 98% of 5-day avg)")
#         elif prices[i+4] > five_day_avg * 1.02:
#             print(f"SELL signal on {dates[i+4]} (Price: {prices[i+4]:.2f}, Above 102% of 5-day avg)")

# Strategy #3: Bollinger Bands