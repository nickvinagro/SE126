import csv

id_list = []
age_list = []
registered_list = []
votes_list = []

with open("Week 3/Labs/voters.csv") as csvfile:
    file = csv.reader(csvfile)
    
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

    for i, age in enumerate(age_list): 
        total_records += 1

        if age < 18: vote_not_eligible += 1

        if age >= 18 and registered_list[i] == "N": vote_min_age_not_registered += 1

        if age >= 18 and registered_list[i] == "Y" and votes_list[i] == "N": vote_min_age_no_vote += 1

        if votes_list[i] == "Y": voters_voted += 1
        
    
    print(f"Number of individuals not eligible to register: {vote_not_eligible}")
    print(f"Number of individuals who are old enough to vote but have not registered: {vote_min_age_not_registered}")
    print(f"Number of individuals who are eligible to vote but did not vote: {vote_min_age_no_vote}")
    print(f"Number of individuals who did vote: {voters_voted}")
    print(f"\nTOTAL RECORDS: {total_records}")