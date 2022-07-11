import os

# Path to collect data from the Resources folder
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

# Declaring the variables
row_count = 0
total_votes_c = 0
total_votes_d = 0
total_votes_r = 0
candidate_list = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]


# Read the csv file
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  # reading the header line into csv_header
  csv_header = next(csvreader)
  
  # loop through the data in csv
  for i in csvreader:
    row_count += 1
    if i[2] == candidate_list[0]:
      total_votes_c +=1
    if i[2] == candidate_list[1]:
      total_votes_d +=1
    if i[2] == candidate_list[2]:
      total_votes_r +=1

# calculating the perecntage of votes to each candidate        
Percentage_c = "{:.3%}".format(total_votes_c/row_count)
Percentage_d = "{:.3%}".format(total_votes_d/row_count)
Percentage_r = "{:.3%}".format(total_votes_r/row_count)


#printing the values to terminal
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {row_count}")
print("-----------------------------------")
print(f"{candidate_list[0]}: {Percentage_c} ({total_votes_c})")
print(f"{candidate_list[1]}: {Percentage_d} ({total_votes_d})")
print(f"{candidate_list[2]}: {Percentage_r} ({total_votes_r})")
print("-----------------------------------")

#winner based on the popular vote
if (Percentage_c > Percentage_d) and (Percentage_c > Percentage_r):
  print(f"Winner: {candidate_list[0]}")
elif (Percentage_d > Percentage_r) and (Percentage_d > Percentage_c):
  print(f"Winner: {candidate_list[1]}")
elif (Percentage_r > Percentage_c) and (Percentage_r > Percentage_d):
 print(f"Winner: {candidate_list[2]}")
print("-----------------------------------")

#writing to text file
PyPoll = os.path.join('Analysis', 'PyPoll.txt')
with open(PyPoll, 'w') as txtfile:
  txtfile.write("Election Results")
  txtfile.write("----------------------------------------")
  txtfile.write(f"Total Votes: {row_count}")   
  txtfile.write("----------------------------------------")
  txtfile.write(f"{candidate_list[0]}: {Percentage_c} ({total_votes_c})")
  txtfile.write(f"{candidate_list[1]}: {Percentage_d} ({total_votes_d})")
  txtfile.write(f"{candidate_list[2]}: {Percentage_r} ({total_votes_r})")
  txtfile.write("-----------------------------------")