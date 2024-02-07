##############################
# Author : Nicholas Vinagro  #
# Lab #4 In Class            #
# Date : 2/7/2024            #
##############################

# importing neccessary modules, CSV
import csv

# PART 1

# initializing neccessary lists & variables, 1D lists for each column in the working CSV file

fname = [] # Column 1: First names
lname = [] # Column 2: Last names
test1 = [] # Column 3: Test grade 1
test2 = [] # Column 4: Test grade 2
test3 = [] # Column 5: Test grade 3


counter = 0 # Total 'record' or Student counter 

# opening txt file that is being used listPractice1.txt in Week 4 In class assignment and reading it as "txtfile"
with open("Week 4/listPractice1.txt") as txtfile:

    # reading txtfile as file with CSV module
    file = csv.reader(txtfile)

    # looping through the file, appending each column to its designated list and incrementing the record counter
    for rec in file:
        counter += 1

        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

# outputting column headers
print(f"{'FIRST':12} \t {'LAST':12} \t TEST1 \t TEST2 \t TEST3")
print('-'*55)

# looping through a column list with range, to get the index, and outputting each column
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")

# PART 2

# initializing new lists for student averages, letter & numerical
average_list = []
average_letter_list = []

# outputting column headers
print('-'*70)
print(f"{'FIRST':12} \t {'LAST':12} \t TEST1 \t TEST2 \t TEST3 \t AVERAGE")
print('-'*70)

# looping through a column list with range, to get index
for i in range(0, len(fname)):
    # calculating the students average and appending it to the designated list
    avg = round((test1[i] + test2[i] + test3[i]) / 3, 1)
    average_list.append(avg)

    # finding the letter equivalent with the average just calculated
    if avg >= 90:
        average_letter_list.append("A")
    elif avg >= 80:
        average_letter_list.append("B")
    elif avg >= 70:
        average_letter_list.append("C")
    elif avg >= 60:
        average_letter_list.append("D")
    elif avg < 60:
        average_letter_list.append("F")

    # outputting each record with the numerical average
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t {average_list[i]:8.1f}")

# outputting column headers
print('-'*80)
print(f"{'FIRST':12} \t {'LAST':12} \t TEST1 \t TEST2 \t TEST3 \t AVERAGE \t LETTER AVG")
print('-'*80)

# looping through a column list with range, to get index
for i in range(0, len(fname)):
    # outputting each record with the numerical and letter average
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]} \t {average_list[i]:8.1f} \t {average_letter_list[i]}")


# output total students in file and the class average
print(f"STUDENTS IN FILE {counter}")
print(f"CLASS AVERAGE: {round(sum(average_list) / len(average_list), 1)}") 
# *** Could do a for loop, loop through the average_list, add it all up and then divide it to also get the average. The python builtins are much faster/cleaner ***

# PART 3

# using list comprehension. looping through a column list with range, to get index and then creating a new list in 'all_students' for each row
all_students = [[fname[i], lname[i], test1[i], test2[i], test3[i], average_list[i], average_letter_list[i]] for i in range(0, len(fname))]

# outputting column headers
print('-'*100)
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1':8} \t {'TEST2':8} \t {'TEST3':8} \t {'AVERAGE':8} {'LETTER AVG':12}")
print('-'*100)

# looping through the all_students 2D list, return value will be each new list
for i in range(0, len(all_students)):
    # looping through each list in the 2D all_students list. Nested for loop
    for x in range(0, len(all_students[i])): # getting the list by using the [i]

        # outputting the values, checking there types to determine the width, int or float = 8, anything else is 12 
        if type(all_students[i][x]) == int or type(all_students[i][x]) == float:
            print(f"{all_students[i][x]:8} \t", end="")
        else:
            print(f"{all_students[i][x]:12} \t", end="")

    # since each print statement in the nested for loop has end="", a additional print statement outside of the loop is needed to seperate each record
    print()

