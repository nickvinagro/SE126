##############################
# Author : Nicholas Vinagro  #
# Midterm                    #
# Date : 2/10/2023           #
##############################

# importing neccessary modules, csv & random
import csv
import random

# initializing neccessary lists & variables, 1D lists for each column in the working CSV file

date_list = []          # Column 1 [0] - Dates
price_list = []         # Column 2 [1] - Close Price
open_price_list = []    # Column 3 [2] - Open Price
high_price_list = []    # Column 4 [3] - High price of the day
low_price_list = []     # Column 5 [4] - Low price of the day
rec_count = 0           # Total record count

# opening csv file bitcoinhistory.csv, reading as variable "csvf". Encoding is used to make sure all the data in CSV file is read properly 
with open("Midterm/bitcoinhistory.csv", encoding='utf-8-sig') as csvf:
    file = csv.reader(csvf)

    # looping through the CSV file and appending each row to its designated list. Incrementing the total record count
    for i in file:
        date_list.append(i[0])
        price_list.append(float(i[1].replace(',', '')))
        open_price_list.append(float(i[2].replace(',', '')))
        high_price_list.append(float(i[3].replace(',', '')))
        low_price_list.append(float(i[4].replace(',', '')))
        
        rec_count += 1

# utility function. Used to calculate the percentage difference between two floats. 
def calc_percent_diff(end: float, start: float):
    return round(((end - start) / abs(start)) * 100, 2) 

# utility function. Used to return all neccessary values from a row. Returns a list...
def record(rec: int) -> list:
    return [date_list[rec], price_list[rec], open_price_list[rec], high_price_list[rec], low_price_list[rec]]

# Menu option 1. Function to calculate the price / percentage difference between two dates
def calc_price_diff_by_date(start_date: str, end_date: str):
    # placeholder variables, to get the index of the two dates choosen from user input
    start_date_index = 0
    end_date_index = 0
        
    # looping through the date list to find the index of both dates choosen
    for i in range(0, len(date_list)):
        if date_list[i] == start_date:
            start_date_index = i
        if date_list[i] == end_date:
            end_date_index = i
        
    # output: basic information on what the first date opened at & the date, and what the second date closed at & the date
    print(f"\nStarting on {date_list[start_date_index]}, Bitcoin had a open price of {open_price_list[start_date_index]}.")
    print(f"Ending on {date_list[end_date_index]}, Bitcoin had a close price of {price_list[end_date_index]}.")
    # checking if the difference between the end price & start price is greater than 0. If yes then it changes the verbage to 'increased'...  
    if price_list[end_date_index] - open_price_list[start_date_index] > 0:
        print(f"\nBitcoin increased in price by {calc_percent_diff(price_list[end_date_index], open_price_list[start_date_index])}%\n")
    else:
        print(f"\nBitcoin decreased in price by {calc_percent_diff(price_list[end_date_index], open_price_list[start_date_index])}%\n")

# Menu option 2. Function to return the top prices that Bitcoin has reached. User input determines the top of the range... 
def top_prices(max: int, price_list: list, date_list: list):
    # hard coded limit on how high the range can go, if > 50 return to start menu
    if max > 50:
        print("Maximum reached. Returning to menu...")
        start_menu(welcome=False)

    # main list used to store the max values, 2D list when returned
    top_prices_list = []
    
    # looping through the max range that the user inputted
    for i in range(0, max):
        # variables used to temporarily store the max value & date of the value
        max, date = 0, '' 

        # looping through the LOCAL price_list variable with range and checking if the value is greater than max, if yes then update the temporary variables
        for x in range(0, len(price_list)):
            if price_list[x] > max:
                max = price_list[x]
                date = date_list[x]
        
        # once the first max value is found, remove it from the LOCAL lists and reiterate to find the next highest value
        price_list.remove(max)
        date_list.remove(date)
        
        # append to the main list that gets returned
        top_prices_list.append([max, date])

    return top_prices_list 

# Menu option 3. Function to find the highest and lowest prices that Bitcoin has reached within a year that is supplied by user input.
def top_low_prices_by_year(year: int):
    # loop to check if the inputted year is not within the dataset range. If it's not then trap user in loop until a valid year is given.
    while year not in [x for x in range(2010, 2025)]:
        print('Invalid input... Input must be within 2010-2024.')
        year = int(input("Enter the year you would like to see the highest and lowest point for Bitcoin. (Example: 2023): "))

    # variables used to temporarily store the max value & date of the value
    high, high_date = 0, ''
    
    # looping through the date list with enumerate to also get the index
    for i, x in enumerate(date_list):
        # checking if the date in the year list matches the supplied year 
        if int(x.split("/")[2]) == year:
            
            # checking if the value in the high price list is greater than the temporary max variable. If yes then reassign the values to the respective value & date.
            if high_price_list[i] > high:
                high = high_price_list[i]
                high_date = date_list[i]
    
    # variables used to temporarily store the low value & date of the value. The low variable uses the high as the top of the range.
    low, low_date = high, ''

    # looping through the date list with enumerate to also get the index
    for i, x in enumerate(date_list):
        # checking if the date in the year list matches the supplied year 
        if int(x.split("/")[2]) == year:

            # checking if the highest value is greater than the lowest value, if yes then reassign the temp variables to the respective value & date.
            if low > low_price_list[i]:
                low = low_price_list[i]
                low_date = date_list[i]

     # returning 2D list with all the temp variables 
    return [[high, high_date], [low, low_date]]

# main function, start menu. Captures all the user input and calls the respective functions
def start_menu(welcome: bool):
    # check to see if this is the first time the menu is being called.
    if welcome:
        print('Welcome to the Bitcoin price analysis tool!')
    else:
        print()

    # main print statement that outputs all the menu options & input to collect the users choice
    print("1. Calculate price difference between two dates.\n2. Find the top prices that Bitcoin has reached. \n3. Find the highest and lowest price that Bitcoin reached within a year.\n4. Find a random row in the dataset.\n5. Exit")
    start = input('Please choose a option (Example: 1): ')
    
    # match statement to check the users input
    match start.lower():
        case '1': # if input is 1 then gather the start & end date
            start_date = input("Enter the start date (Example: 10/1/2022): ")
            end_date = input("Enter the end date (Example: 10/1/2023): ")
            if len(start_date) < 8 or len(end_date) < 8: # simple input validation to see if the dates entered are less than 8 characters
                print('Invalid input. Try again...')
                start_menu(welcome=False)
            else:
                calc_price_diff_by_date(start_date, end_date) # pass dates to function and the percentage increase/decrease is outputted

        case '2': # if input is 2 then gather the # of top prices the user would like to see
            top_price = int(input("Enter the # of top prices you would like to see. (Example: 20, MAX 50): ")) 
            top_list = top_prices(max=top_price, price_list=high_price_list, date_list=date_list) # calling the designated function with all the needed variables
            for x in range(1, len(top_list)+1): # looping through the returned 2D list and outputting all the values in the correct order.
                print(f"{x}. ${top_list[x-1][0]:,} - {top_list[x-1][1]}")
            print()

        case '3': # if input is 3 then gather the year the user would like to see highest & lowest points for
            year = int(input("Enter the year you would like to see the highest and lowest point for Bitcoin. (Example: 2023): "))
            top_low_list = top_low_prices_by_year(year=year) # call the designated function to get the highest & lowest points based on the year
            # output the dates & prices from the function call
            print(f"Bitcoin's Highest price was on {top_low_list[0][1]} @ ${top_low_list[0][0]:,}.\nThe lowest price was on {top_low_list[1][1]} @ ${top_low_list[1][0]:,}.")
            print()

        case '4': # if input is 4 then generate a random int, then call the record function to get all the neccessary data
            rec_info = record(random.randint(0, rec_count))
            # output all the data from the record function call
            print(f"On {rec_info[0]}, Bitcoin opened at ${rec_info[2]:,} and closed the day at ${rec_info[1]:,}.\nWith a High of ${rec_info[3]:,} and a Low of ${rec_info[4]:,}.")
            print()

        case 'exit' | '5': # if input is exit or 5, exit
            print('Goodbye!')
            exit()

        case _: # if the input does not match anything else above, restart the menu
            start_menu(welcome=False)

    # continue input statement that is run after the menu choice, if N -> exit. Anything else will continue 
    cont = input('Continue? ("Y" or "N"): ').lower()
    if cont == "n":
        print('Goodbye!')
        exit()
    else:
        start_menu(welcome=False)

# main function call to start program
start_menu(welcome=True)