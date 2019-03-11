import csv

#We will be keeping track of candidates and their votes in two separate lists 
Candidates = []
CandidateVotes = []
VoteCount = 0
WinnerVotes = 0

with open("../Resources/election_data.csv", newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    #For each non-header row
    for row in csvreader:
        #Increment the count of votes
        VoteCount += 1
        #If the candidate does not appear in the list of candidates, add them to it and give them a vote in the vote count list
        if Candidates.count(row[2]) == 0:
            Candidates.append(row[2])
            CandidateVotes.append(1)
        else:
            #If the candidate already appears, increment their vote count
            CandidateVotes[Candidates.index(row[2])] += 1

#Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {VoteCount}")
print("-------------------------")
#Run through the candidate list
for n in range(len(Candidates)):
    #Each canddiate has their name printed, following by the percentage of votes they received and the number of votes they received
    print(f"{Candidates[n]}: {(100*CandidateVotes[n]/VoteCount):.3f}% ({CandidateVotes[n]})")
    #Check if the current candidate was the highest vote getter, if so save their name and vote count as the new front runner
    if CandidateVotes[n] > WinnerVotes:
        WinnerName = Candidates[n]
        WinnerVotes = CandidateVotes[n]
print("-------------------------")
#Print winner's name
print(f"Winner: {WinnerName}")
print("-------------------------")

#As above but outputs to txt file
with open("Election_Results.txt","w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {VoteCount}\n")
    txtfile.write("-------------------------\n")
    for n in range(len(Candidates)):
        txtfile.write(f"{Candidates[n]}: {(100*CandidateVotes[n]/VoteCount):.3f}% ({CandidateVotes[n]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {WinnerName}\n")
    txtfile.write("-------------------------\n")