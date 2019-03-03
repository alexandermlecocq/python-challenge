import csv

Candidates = []
CandidateVotes = []
VoteCount = 0
WinnerVotes = 0

with open("../Resources/election_data.csv", newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        VoteCount += 1
        if Candidates.count(row[2]) > 0:
            CandidateVotes[Candidates.index(row[2])] += 1
        else:
            Candidates.append(row[2])
            CandidateVotes.append(1)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {VoteCount}")
print("-------------------------")
for n in range(len(Candidates)):
    print(f"{Candidates[n]}: {round((100*CandidateVotes[n]/VoteCount), 3)}% ({CandidateVotes[n]})")
    if CandidateVotes[n] > WinnerVotes:
        WinnerName = Candidates[n]
        WinnerVotes = CandidateVotes[n]
print("-------------------------")
print(f"Winner: {WinnerName}")
print("-------------------------")

with open("Election_Results.txt","w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {VoteCount}\n")
    txtfile.write("-------------------------\n")
    for n in range(len(Candidates)):
        txtfile.write(f"{Candidates[n]}: {round((100*CandidateVotes[n]/VoteCount), 3)}% ({CandidateVotes[n]})\n")
        if CandidateVotes[n] > WinnerVotes:
            WinnerName = Candidates[n]
            WinnerVotes = CandidateVotes[n]
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {WinnerName}\n")
    txtfile.write("-------------------------\n")