##############################
# Author : Nicholas Vinagro  #
# Lab #1                     #
# Date : 1/15/2023           #
##############################

import part2
import part1

# start of loop, used to continue if user wants to check multiple meetings
cont = True
while cont:

    # inputs for meeting name, room cap, and # of attendees
    meeting_name = input("What is the meeting name? ")
    room_cap = int(input("What is the meeting room capacity? "))
    people_attending = int(input("How many people will be attending the meeting? "))

    # checking the difference between room cap & peeople attending
    diff = part1.difference(people_attending, room_cap)

    # if the difference is greater than 0, more people can attend. if it's less than 0, people need to be removed
    if diff > 0:
        print(f"This meeting meets fire safety regulations. {diff} people can be added to the meeting and still meet fire regulations.")
    else:
        print(f"This meeting DOES NOT meet fire safety regulations and {diff*-1} people must be removed from the meeting to meet fire regulations.")

    # asking the user if more people want to attend. Input MUST be 'y' or 'n'. Passing to function to check result.
    new_meeting = input("Would you like to check another meeting ('y' or 'n') ")
    result = part2.descision(new_meeting)

    if result == "y":
        cont = True
    elif result == "n":
        cont = False
        print("Goodbye!")