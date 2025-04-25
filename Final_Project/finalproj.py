import requests
import json

def simplemovingaverage(prices, ticker):
    print(ticker, "Simple Moving Average Output:")
    i = 0 #indexing value to keep track
    buy = 0
    total_profit = 0
    #loop through prices
    for price in prices:
        if i >= 5:
            current_price = price
            #5 day moving average
            average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5 #average price for the 5 previous days

            if current_price > average and buy == 0:
                buy = current_price #buy stock if meets criteria
                #print("Buying At: ", round(current_price,2))
                #store first buy price
                if i == len(prices)-1:
                    print("You should buy", ticker, "stock today.")
            elif current_price < average and buy != 0:
                #print("Selling At: ", round(current_price,2)) #sell stock if meets criteria
                #calculate trade profit
                trade_profit = current_price - buy
                total_profit += trade_profit
                #print("Trade Profit: ", round(trade_profit,2))
                if i == len(prices)-1:
                    print("You should sell", ticker, "stock today.")
                buy = 0 #reset buy variable after selling
            else:
                pass
            #move to next day
            i += 1

        print("Total Profit: ", round(total_profit,2))
        return total_profit

def meanreversionstrategy(prices, ticker):
    print(ticker, "mean reversion strategy output:")
    i           = 0 #indexing value to keep track
    buy         = 0
    totalprofit = 0
    firstbuy    = 0

    for price in prices:
        if i >= 5:
            current_price = price #the next price in the list

            average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5 #average price for the 5 previous days
            # print(average)d

            if current_price < average * 0.98 and buy == 0:
                buy = current_price
                #update buy variable
                #print("Buying at:", round(current_price,2))
                #store first buy price
                if i == len(prices)-1:
                    print("You should buy", ticker, "today! (according to Mean Reversion Strategy)")
            #update first_buy variable if this is the first time you buy
            elif current_price > average * 1.02 and buy != 0:
                #calculate trade profit (how much moeny i made)
                #print("Selling at: ", round(current_price,2))
                trade_profit += current_price - buy
                total_profit += trade_profit
                #print("Trade profit: ", round(trade_profit_2))
                if i == len(prices)-1:
                    print("You should sell", ticker, "today! (according to Mean Reversion Strategy)")
                buy = 0
            else:
                pass
        #move to next day
        i += 1

    print("Total Profit: ", round(total_profit,2))
    return total_profit


def bollingerBands(prices, ticker):
    print(ticker, "Bollinger Bands Strategy output:")
    i = 0
    total_profit = 0
    buy = 0

    #need to loop through prices list
    for price in prices:
        if i >= 5:
            current_price = price
            #5 day moving average
            average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5 #average price for the 5 previous days
            if current_price > average * 1.05 and buy == 0:
                buy = current_price #buy stock if meets criteria
                #print("Buying at: ", round(current_price,2))
                #store first buy price
                if i == len(prices)-1:
                    print("You should buy", ticker, "stock today.")
            elif current_price < average * 0.95 and buy != 0:
                #print("Selling At: ", round(current_price,2)) #sell stock if meets criteria
                #calculate trade profit (how much money made)
                trade_profit = current_price - buy
                total_profit += trade_profit
                #print("Trade Profit: ", round(trade_profit,2))
                if i == len(prices)-1:
                    print("You should sell", ticker, "stock today.")
                buy = 0 #reset buy variable after selling
            else:
                pass
        #move to next day
        i += 1

    print("Total Profit: ", round(total_profit,2))
    return total_profit

def saveResults(dictionary):
    #with open("strategy_results.json", "w") as file:
    json.dump(dictionary, open("/home/ubuntu/Final_Project/finalproj.py/results.json", "w"), indent=4)

def initialDataPull(tickers):
    for ticker in tickers:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

    #making the api call for our stock 
        request = requests.get(url)
        request_dictionary = json.loads(request.text)

        #print("request_dictionary:", request_dictionary) # keys
        key_1 = "Time Series (Daily)"
        #key_1 = "2025-04-08" i need every date not just one
        key_2 = "4. close"

        #print(request_dictionary[key_0][key_1][key_2])
        #print(request_dictionary[key_0].keys())

        lines = []

        for date in request_dictionary[key_1].keys():
            lines.append(date + ", " + request_dictionary[key_1][date][key_2] + "\n")

        #reverse the lines of our file so we don't do our strategies backwards
        lines = lines[::-1]

        with open("/home/ubuntu/Final_Project"+ticker+".csv", "w") as file:
            file.writelines(lines)


def appendData(tickers):
    for ticker in tickers:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

        #make API call for our stock
        request = requests.get(url)
        request_dictionary = json.loads(request.text)

        #keys
        key_1 = "Time Series (Daily)"
        key_2 = "4. close"

        #open pre-existing file
        with open("/home/ubuntu/Final_Project"+ticker+".csv", "r") as file:
            csv_lines = file.readlines()

        #track the last date added to our file
        latest_date = csv_lines[-1].split(",")[0]

        new_lines = []

        for date in request_dictionary[key_1].keys():
            if date == latest_date:
                break
            else:
                new_lines.append(date + "," + request_dictionary[key_1][date][key_2] + "\n")

        new_lines = new_lines[::-1]

        #add new data
        with open("/home/ubuntu/Final_Project"+ticker+".csv", "a") as file:
            file.writelines(new_lines)



#initialize variables we'll need all through the code 
results = {}
tickers = ["AAPL", "GOOG", "HAS", "NKE", "NVDA", "PLTR", "SCHD", "SPXL", "TQQQ", "TSLA"]

#initialDataPull(tickers)
appendData(tickers)

most_profit = 0
best_strat = ""
best_ticker = ""

for ticker in tickers:
    prices = [round(float(line.split(",")[1]), 2) for line in reversed(open("/home/ubuntu/Final_Project" + ticker + ".csv", "r"))]

#run mean reversion and simple moving average
MR_profit = meanreversionstrategy(prices, ticker)
SMA_profit = simplemovingaverage(prices, ticker)
BB_profit = bollingerBands(prices, ticker)  

#isolate the list of prices form file

#get the profit and return % from the functions and save them to a dictionary
results[ticker+"_prices"] = prices
results[ticker+"_MR_profit"] = MR_profit
results[ticker+"_SMA_profit"] = SMA_profit
results[ticker+"_BB_profit"] = BB_profit

if MR_profit > most_profit:
    most_profit = MR_profit
    best_strat = "Mean Reversion"
    best_ticker = ticker
elif SMA_profit > most_profit:
    most_profit =SMA_profit
    best_strat = "Simple Moving Average"
    best_ticker = ticker
elif BB_profit > most_profit:
    most_profit = BB_profit
    best_strat = "Bollinger Bands"
    best_ticker = ticker

saveresults(results)

print("The stock that made the most profit was", best_ticker, "with a profit of", most_profit, "using the", best_strat)



