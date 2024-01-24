##############################
# Author : Nicholas Vinagro  #
# Lab #3                     #
# Date : 1/23/2023           #
##############################

# importing neccessary modules, CSV
import csv

# initializing neccessary lists, 1D lists for each column in the working CSV file

id_list = []
age_list = []
registered_list = []
votes_list = []

# opening CSV file that is being used voters.csv in Week 3/Labs directory and reading it as "csvfile"
with open("Week 3/Labs/voters.csv") as csvfile:
    file = csv.reader(csvfile)
    
    # looping through the file and appending each value to its respective lis
    for i in file:
        id_list.append(i[0])
        age_list.append(int(i[1]))
        registered_list.append(i[2])
        votes_list.append(i[3])


vote_not_eligible = 0               # num of individuals not eligible to register
vote_min_age_not_registered = 0     # num of individuals who are old enough to vote but, didn't register
vote_min_age_no_vote = 0            # num of individuals who are old eligible to vote but, didn't
voters_voted = 0                    # num of individuals who did vote
total_records = 0                   # total # of records

# looping through the list and getting the index AND the element in the list
# the index will be used to access other values in the other 3 parallel lists.
for i, age in enumerate(age_list):
    # incrementing the total records 
    total_records += 1            

    # checking if there not eligible to register by, checking if there less than 18 years old.
    if age < 18: vote_not_eligible += 1

    # checking if there old enough to vote but, didn't register
    if age >= 18 and registered_list[i] == "N": vote_min_age_not_registered += 1

    # checking if there eligible to vote, 18 or older, and registered but, did NOT vote
    if age >= 18 and registered_list[i] == "Y" and votes_list[i] == "N": vote_min_age_no_vote += 1

    # checking the # of people who voted
    if votes_list[i] == "Y": voters_voted += 1
    
# outputting all the variables, stored earlier and the total # of records.
print(f"Number of individuals not eligible to register: {vote_not_eligible}")
print(f"Number of individuals who are old enough to vote but have not registered: {vote_min_age_not_registered}")
print(f"Number of individuals who are eligible to vote but did not vote: {vote_min_age_no_vote}")
print(f"Number of individuals who did vote: {voters_voted}")
print(f"\nTOTAL RECORDS: {total_records}")