##############################
# Author : Nicholas Vinagro  #
# Lab #4 Lab                 #
# Date : 2/7/2024            #
##############################

# importing neccessary modules, CSV
import csv

# initializing neccessary lists & variables, 1D lists for each column in the working CSV file

fname = [] # Column 1: First names
lname = [] # Column 2: Last names
age = [] # Column 3: Age
nickname = [] # Column 4: Nickname
house_allegiance = [] # Column 5: House Allegiance

# dictionary of each house and its motto, as well as the count of each 
house_motto = {
    "House Stark": ["Winter is Coming", 0],
    "House Baratheon": ["Ours is the fury.", 0],
    "House Tully":	["Family. Duty. Honor.", 0],
    "Night's Watch": ["And now my watch begins.", 0],
    "House Lannister": ["Hear me roar!", 0],
    "House Targaryen": ["Fire & Blood", 0]
 
}
# opening txt file that is being used listPractice1.txt in Week 4 In class assignment and reading it as "txtfile"
with open("Week 4/Labs/lab4A_GOT_NEW.txt") as txtfile:

    # reading txtfile as file with CSV module
    file = csv.reader(txtfile)

    # looping through the file, appending each column to its designated list and incrementing the record counter
    for rec in file:
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        house_allegiance.append(rec[4])

# outputting column headers
print(f"{'FIRST':12} \t {'LAST':12} \t {'AGE':5} \t {'NICKNAME':16} \t {'HOUSE':18}")
print('-'*80)

# looping through a column list with range, to get the index, and outputting each column
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:3} \t {nickname[i]:16} \t {house_allegiance[i]:18}")


# outputting column headers
print(f"{'FIRST':12} \t {'LAST':12} \t {'AGE':5} \t {'NICKNAME':16} \t {'HOUSE':18} \t {'HOUSE MOTTO':32}")
print('-'*120)

# looping through a column list with range, to get the index, and outputting each column with the house motto. 
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:3} \t {nickname[i]:16} \t {house_allegiance[i]:18} \t {house_motto[house_allegiance[i]][0]:32}")
    # getting the house motto from the house_motto dictionary

# initializing new variables to calculate average age and count the # of people
total_num_people = 0
average_age = 0
for i in range(0, len(fname)):
    total_num_people += 1
    average_age += age[i]
    house_motto[house_allegiance[i]][1] += 1 # counting how many rows are in the designated house

# outputting the total number of people, average age, and the count of each house
print(f'TOTAL NUMBER OF PEOPLE: {total_num_people}')
print(f'AVERAGE AGE: {average_age / total_num_people:.0f}')
for x in set(house_allegiance): print(f'COUNT OF {x}: {house_motto[x][1]}')