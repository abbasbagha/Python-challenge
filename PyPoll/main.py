"""
election data 
"""
# importing os and csv module
import os
import csv

# defining the path of the csv file and opening it in read format
election_data_path = os.path.join("Resources", "election_data.csv")
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
    winner = 0
    candidate_results: list[str] = []
    for candidate in candidate_list:
        candidate_count = vote_data.count(candidate)
        if candidate_count > winner:
            winner = candidate_count
            winner_name = candidate
        candidate_result: str =  f"{candidate}:   {vote_data.count(candidate)}: {(((vote_data.count(candidate))/total_votes)*100):.3f}%"
        candidates_results.append(candidate_result)
        print(candidate_result)
    print(f"The total votes cast: {total_votes}")
    print(winner)
    print(winner_name)


    # writing the results to analysis
    text_file_path = "Analysis/Analysis.txt"
    with open(text_file_path, "w", encoding="UTF-8") as text_file:
        text_file.write("PyPoll Analysis")
        text_file.write("\n----------------------------------------")
        text_file.write("\n" f"The total votes cast: {total_votes}")
        text_file.write("\n----------------------------------------")
        text_file.write("\n" f'the winner is {winner_name}')
        text_file.write(candidates_results)
