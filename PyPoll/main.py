import os
import csv

#Vote counter
voter_count = 0

#Variable for the list of candidates and votes
candidate_list = {}

#create the path for the csv file
csvpath = os.path.join('Resources/election_data.csv')

#read in the csv file and identify the headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#count all of the votes, and identify the candidates who received votes
    for row in csvreader:
       voter_count += 1
       candidate = row[2]
       if candidate not in candidate_list:
           candidate_list[candidate] = 1
       else: 
           candidate_list[candidate] += 1

#print results to terminal
print("Election Results")
print("-------------------------")
print("Total votes: " + str(voter_count))
print("-------------------------")

#variables to keep track of the winning candidate
winner_name = ""
winner_votes = 0
#use a for loop to find out percentage and print out results
for candidate in candidate_list:
    total_votes = candidate_list[candidate]
    percentage = total_votes/voter_count * 100
    print(f"{candidate}: {percentage:.3f}% ({total_votes})")

    if total_votes > winner_votes:
        winner_name = candidate
        winner_votes = total_votes

print("------------------------")
print(f"Winner: {winner_name}")

#create a txt file to write the results in
file = open("PyPoll Results.txt", "w+")

file.write("Election Results\n")
file.write("\n-------------------------\n")
file.write("\nTotal votes: " + str(voter_count) + "\n")
print("-------------------------")

#variables to keep track of the winning candidate
winner_name = ""
winner_votes = 0
#use a for loop to find out percentage and print out results
for candidate in candidate_list:
    total_votes = candidate_list[candidate]
    percentage = total_votes/voter_count * 100
    file.write(f"\n{candidate}: {percentage:.3f}% ({total_votes})\n")

    if total_votes > winner_votes:
        winner_name = candidate
        winner_votes = total_votes

file.write("\n------------------------\n")
file.write(f"\nWinner: {winner_name}\n")
