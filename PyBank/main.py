import csv

#Read the CSV, count the number of non-header rows and then load all the values into two lists
Months = 0
Profits = []
Dates = []

with open("../Resources/budget_data.csv", newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        Months += 1
        Dates.append(row[0])
        Profits.append(float(row[1]))

TotalProfits = Profits[0]
TotaledChanges = 0
BigInc = 0
BigDec = 0

#Start at 1 rather than 0 so we can calculate the change in profit below (we already put the first month's profit into total profit)
for n in range (1, Months):
    #Add current month's profit to total profits
    TotalProfits += Profits[n]
    
    #Calculate the change between this month and the month before it and then add it to the totaled changes
    CurrentChange = Profits[n] - Profits[n-1]
    TotaledChanges += CurrentChange
    
    #Check if the current change was the biggest increase/decrease and if so, make it the biggest
    if CurrentChange > BigInc:
        BigInc = CurrentChange
        BigIncDate = Dates[n]
    elif CurrentChange < BigDec:
        BigDec = CurrentChange
        BigDecDate = Dates[n]

#Print the final results
print("Financial Analysis")
print("----------------------------")
print(f"Months: {Months}")
print(f"Total Profits: ${(TotalProfits):.2f}")
print(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}")
print(f"Greatest Increase in Profits: {BigIncDate} (${(BigInc):.2f})")
print(f"Greatest Decrease in Profits: {BigDecDate} (${(BigDec):.2f})")

#Output final results to txt file
with open("Financial_Analysis.txt","w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Months: {Months}\n")
    txtfile.write(f"Total Profits: ${(TotalProfits):.2f}\n")
    txtfile.write(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {BigIncDate} (${(BigInc):.2f})\n")
    txtfile.write(f"Greatest Decrease in Profits: {BigDecDate} (${(BigDec):.2f})\n")