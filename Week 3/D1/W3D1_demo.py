##############################
# Author : Nicholas Vinagro  #
# Lab #W3 In Class Lab       #
# Date : 1/23/2023           #
##############################

# importing neccessary modules, CSV
import csv

# initializing neccessary variables, total records and all 1D lists for each column in the working CSV file
records = 0

device = []
brand = []
cpu = []
ram = []
first_disk = []
no_hdd = []
second_disk = []
os = []
yr = []

# opening CSV file that is being used lab3a.csv in D1 directory and reading it as "file"
with open("Week 3/D1/lab3a.csv") as csvf:
    file = csv.reader(csvf)

    # iterating through the CSV file, each row is "rec"
    for rec in file:

        # incrementing the total records variable
        records += 1

        # checking if the first value in the record is a Desktop or Laptop, if not "ERROR" 
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "*ERROR*"

        # checking the computer brand in the second value, Dell, Gateway, or HP, if not "ERROR"
        if rec[1] == "DL":
            comp_brand = "Dell"
        elif rec[1] == "GW":
            comp_brand = "Gateway"
        elif rec[1] == "HP":
            comp_brand = "HP"
        else:
            comp_brand = "*ERROR*"

        # declaring static variables in the records. These are always in the same spot in the file
        comp_cpu = rec[2]               # CPU
        comp_ram = rec[3]               # amount of RAM
        comp_first_hdd = rec[4]         # storage size of the 1st HDD
        comp_num_of_hdd = int(rec[5])   # number of hard drives

        # if # of HDD's is 1 then there is no 2nd HDD and declaring the computer OS & Year, setting the 2nd HDD value to a blank value
        if comp_num_of_hdd == 1:
            comp_second_hdd = "---"
            comp_os = rec[6]
            comp_year = rec[7]

        # if # of HDD's is 2 then all values are in the record. Declaring all variables
        elif comp_num_of_hdd == 2:
            comp_second_hdd = rec[6]
            comp_os = rec[7]
            comp_year = rec[8]

        else:
            comp_second_hdd = "*ERROR*"
            comp_os = "*ERROR*"
            comp_year = "*ERROR*"

        # appending all the values declared above to there designated lists
        device.append(comp_type) 
        brand.append(comp_brand)
        cpu.append(comp_cpu)
        ram.append(comp_ram)
        first_disk.append(comp_first_hdd)
        no_hdd.append(comp_num_of_hdd)
        second_disk.append(comp_second_hdd)
        os.append(comp_os)
        yr.append(comp_year)

# printing the total # of records
print("RECORDS: ", records)

print("\n\n\nPRINTING FROM LISTS----------------")

# loop through range of records. 
# "records" has the number of values in each list.
# printing each value with it's index
for index in range(0, records):
     print(f"INDEX: {index} \t {device[index]:10} \t {brand[index]:10} \t {cpu[index]:3} \t {ram[index]:2} \t {first_disk[index]:7} \t {no_hdd[index]:7} \t {second_disk[index]:7} \t {os[index]:4} \t {yr[index]}")


# START OF IN WEEK #3 - IN CLASS LAB | ASSIGNMENT
     
# declaring the old # of desktop & laptop counts     
old_desktop_count = 0
old_laptop_count = 0

# declaring the replacement costs for old desktops & laptops
total_replacement_cost_desktops = 0
total_replacement_cost_laptops = 0 

# looping through the range of records
for index in range(0, records):

    # if the device is a Desktop and it's older than 2016, it needs to be replaced. 
    #Incrementing the old desktop count & adding the cost for a new one
    if device[index] == "Desktop" and int(yr[index]) <= 16:
        old_desktop_count += 1
        total_replacement_cost_desktops += 2000
    
    # if the device is a Laptop and it's older than 2016, it needs to be replaced. 
    # Incrementing the old laptop count & adding the cost for a new one
    if device[index] == "Laptop" and int(yr[index]) <= 16:
        old_laptop_count += 1
        total_replacement_cost_laptops += 1500
    
# outputting the total number of desktop & laptops & there respective costs
print(f"TOTAL DESKTOPS TO REPLACE: {old_desktop_count} AND WOULD COST ${total_replacement_cost_desktops:,d}")
print(f"TOTAL LAPTOP TO REPLACE: {old_desktop_count} AND WOULD COST ${total_replacement_cost_laptops:,d}")

# outputting the total for all the replacements
print(f"\nTOTAL: ${total_replacement_cost_desktops + total_replacement_cost_laptops:,d}")