#garbage collector

#pseudocode - written code about the code. outline. in words. breaking it down into steps.
'''
i need to import libraries and stuff
'''

#if else if
day = "monday"
if day == "monday":
    print("it's another monday 😮‍💨")

#usu vs unlv
usu_score = 50
unlv_score = 57

if usu_score > unlv_score:
    print("What happened in Vegas was a fluke! USU always wins!")
elif unlv_score > usu_score:
    print("This is a tragedy!")
elif usu_score == unlv_score:
    print("It's overtime!!!")
elif weather == True:
    print("The game goes on!")
elif weather != True:
    print("Cancel the game!")
else: 
    print("Nothing happens!")

#pseudocode - drive to slc and cook dinner

#define our variables
gas = int(input("How much gas do you have: "))
weather = input("What is the weather like: ")
is_cooking = bool(input("Is your roommate cooking right now, True or False: "))

#check weather - good or bad
if weather == "Good":
    #check gas level
    if gas > 12:
         print("Drive to slc!")
    else:
        print("Go get gas")

elif weather == "Whiteout conditions":
    print("Stay home and stay warm!")

#check if roommate is cooking dinner
if is_cooking == True:
    print("We're still going to SLC")


#do i need an emissions test for my car


#define variables: current year, model year, vintage car (boolean)
#current year
current_year = 2025
model_year = input("What is the model year of your vehicle: ")
is_vintage = bool(input("Is your car older than 1967, True or False: "))

#exemotions from emissions testing
if is_vintage == True:
    print("Your vehicle is exempt from emissions testing.")
elif model_year == current_year:
    print("Your vehicle is exempt from emissions testing this year.")

#test inputs - if statements to determine
    if model_year % 2 == 0:
        if current_year % 2 == 0:
            print("You need an emissions test next year.")
        
    else: #model_year % 2 == 1:
        if current_year % 2 == 1:
            print("You need an emissions test this year")
        else:
            print("You need an emissions test next year.")

#print out results
   
#vintage variable

#get model year


