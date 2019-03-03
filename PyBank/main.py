import os
import csv

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

for n in range (1, Months):
    TotalProfits = TotalProfits + Profits[n]
    CurrentChange = Profits[n] - Profits[n-1]
    if CurrentChange > BigInc:
        BigInc = CurrentChange
        BigIncDate = Dates[n]
    elif CurrentChange < BigDec:
        BigDec = CurrentChange
        BigDecDate = Dates[n]
    TotaledChanges = TotaledChanges + CurrentChange

print("Financial Analysis")
print("----------------------------")
print(f"Months: {Months}")
print(f"Total Profits: ${round(TotalProfits, 2)}")
print(f"Average Change: ${round(TotaledChanges/(Months - 1), 2)}")
print(f"Greatest Increase in Profits: {BigIncDate} (${round(BigInc, 2)})")
print(f"Greatest Decrease in Profits: {BigDecDate} (${round(BigDec, 2)})")


with open("Financial_Analysis.txt","w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Months: {Months}\n")
    txtfile.write(f"Total Profits: ${round(TotalProfits, 2)}\n")
    txtfile.write(f"Average Change: ${round(TotaledChanges/(Months - 1), 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {BigIncDate} (${round(BigInc, 2)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {BigDecDate} (${round(BigDec, 2)})\n")