# # example 1
# def calculatearea(length, width):
#     return length * width

# # example 2
# def sum_list(numbers):
#     return sum(numbers)

# # example 3
# def concat_strings(strings):
#     return "".join(strings)



# '''
# every function has: 
# 1. name or definition
# 2. arguments
# 3. main logic - body code
# 4. return - if we dont have a returun statement, the default is to return nothing
# '''

# def fun_function():
#     print("Were having fun")

# print(fun_function()) #function call


#function arguments
#farenheit to celsius
def FtoCconvert(tempF):
    return(tempF-32) * (5/9)
print(round(FtoCconvert(33), 0))

#celsius to farenheit
def CtoFconvert(tempC):
    return(tempC/(5/9)) + 32
print(round(CtoFconvert(33), 0))

#function default
def valentinemessage(name="hot stuff"):
    print("Hey," + name + " you are beautiful. 🩷🩷🩷🩷🩷🩷🩷 May I slide into your DMS? 🩷🩷🩷🩷🩷🩷🩷🩷")

valentinemessage()
valentinemessage("Lucy")
valentinemessage("Abby")
valentinemessage("Blake")










