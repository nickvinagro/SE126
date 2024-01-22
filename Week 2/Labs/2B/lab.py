##############################
# Author : Nicholas Vinagro  #
# Lab #2B                    #
# Date : 1/16/2023           #
##############################

# importing needed modules
import csv

# outputting headers 
print(f"{'Type':8} \t {'Brand':8} \t {'CPU':3} \t {'RAM':3} \t {'1st Disk':9} \t {'No HDD':7} \t {'2nd Disk':9} \t {'OS':4} \t {'YR':3}")

# total # of records that will be processed.
total_records = 0

# opening csv and initializing
with open("Week 2/Labs/2B/lab2b.csv") as csvf:
    file = csv.reader(csvf)

    # looping through the file, incrementing the total # of records
    for i in file:
        total_records += 1

        # initializing all the variables for values that are in the file
        comp_type = i[0] #
        comp_brand = i[1]#
        comp_cpu = i[2]  #
        comp_ram = i[3]  #
        comp_first_hdd = i[4] #
        comp_num_of_hdd = i[5] #

        # initializing temporary variables for values that may be in the file
        comp_second_hdd = ''
        comp_os = ''
        comp_year = ''
        
        # translating the computer type into Desktop or Laptop
        if comp_type == "D": comp_type = "Desktop"
        elif comp_type == "L": comp_type = "Laptop"

        # translating the computer brand into Dell or Gateway
        if comp_brand == "DL": comp_brand = "Dell"
        elif comp_brand == "GW": comp_brand = "Gateway"

        # if length of record is 8 only assign values to the correct variable, if it's 9 then all values are in place         
        if len(i) == 8:
            comp_os = i[6] #
            comp_year = i[7] #

        elif len(i) == 9:
            comp_second_hdd = i[6]
            comp_os = i[7] #
            comp_year = i[8] #
        
        # outputting all variables & 1 final output of computers processed.
        print(f'{comp_type:8} \t {comp_brand:8} \t {comp_cpu:3} \t {comp_ram:3} \t {comp_first_hdd:9} \t {comp_num_of_hdd:7} \t {comp_second_hdd:9} \t {comp_os:4} \t {comp_year:3}')

print(f"\n{total_records} COMPUTERS PROCESSED.")