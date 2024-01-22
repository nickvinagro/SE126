##############################
# Author : Nicholas Vinagro  #
# Lab #2A                    #
# Date : 1/16/2023           #
##############################

import csv

# output the headers for the CSV file below
# list of rooms, max room cap, # of people attending
print(f"{'Room':15} \t {'Max':5} \t {'Min':5} \t {'Over':5}")

# total records count & total # of rooms over the maximum cap 
record_count = 0 
rooms_over_count = 0

# opening csv and initializing
with open("Week 2/Labs/2A/lab2a.csv") as csvf:
    file = csv.reader(csvf)

    # loop over file and initalize all the variables for each header
    # additional variable for how over/under a room / meeting is

    for i in file:
        record_count += 1

        room_name = str(i[0])
        max_room_cap = int(i[1])
        num_people_attending = int(i[2])

        over = num_people_attending - max_room_cap

        # checking if the meeting is over on capacity, if YES then printing a formatted message with the details
        if over > 0:
            print(f"{room_name:15} \t {max_room_cap:3} \t {num_people_attending:3} \t {over:3}")
            rooms_over_count += 1
        else:
            continue

# output to show total records & how many rooms were over
print(f"\nProcessed {record_count} records.\nThere are {rooms_over_count} rooms over the limit.")