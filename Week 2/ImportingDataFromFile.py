import csv

total_records = 0

total_salarys = 0

print("NAME \tAGE \tSALARY")
print("-"*30)

with open("Week 2/example.csv") as csvfile:
    file = csv.reader(csvfile)


    for rec in file:
        print(rec)