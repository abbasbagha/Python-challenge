"""
election data 
"""
# importing os and csv module
import os
import csv

# defining the path of the csv file and opening it in read format
election_data_path = os.path.join("Resources","election_data.csv")
with open(election_data_path, "r", encoding="UTF-8") as electionfile:
    input_data = csv.reader(electionfile, delimiter=",")
    header = next(input_data)  # column data headers
    # print(header)
    candidate_list = []  # creating the list for candidates in the election
    vote_data = []  # creating the list for votes for canidates
    for row in input_data:
        vote_data.append(row[2])
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    print(f'candidates : {" , ".join(candidate_list)}')
    # print(data)
    total_votes = len(vote_data)
    for candidate in candidate_list:
        print(
            f"{candidate}:   {vote_data.count(candidate)}: {(((vote_data.count(candidate))/total_votes)*100):.3f}%"
        )
    print(f"The total votes cast: {total_votes}")
