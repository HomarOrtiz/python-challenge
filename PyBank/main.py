#import libraries
import os
import csv
#create empty lists to store total months and profit/losses
months = []
profit_losses = []

# These variables are used to keep track of profit loss changes.
previous_profit_loss = None
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

#create the path for the csv file
csvpath = os.path.join('Resources/budget_data.csv')

#read in the csv file and identify the headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   

#iterate through rows
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        months.append(date)
        profit_losses.append(profit_loss)
        if previous_profit_loss is not None:
            profit_loss_change = profit_loss - previous_profit_loss

            if profit_loss_change > greatest_increase:
                greatest_increase = profit_loss_change
                greatest_increase_month = date
            if profit_loss_change < greatest_decrease:
                greatest_decrease = profit_loss_change
                greatest_decrease_month = date
        
        previous_profit_loss = profit_loss

#find the total amount of Profit/Losses over the entire period
sum = sum(profit_losses)

#find the changes in profit over the entire period
lastmonth = profit_losses[85]
firstmonth = profit_losses[0]
change = lastmonth - firstmonth
averagechange = change/85

# print results to terminal 
print("Financial Analysis\n")

print("\n-------------------------------------\n")

print(f"\nTotal Months: {len(months)}\n")
print(f"\nTotal: ${sum:,.0f}\n")
print(f"\nAverage Change: ${averagechange:,.2f}\n")
print(f"\nGreatest Increase in Profits: {greatest_increase_month} ${greatest_increase:,.0f}\n")
print(f"\nGreates Decrerase in Profits: {greatest_decrease_month} ${greatest_decrease:,.0f}\n")

#create a txt file to write the results in
file = open("PyBank Results.txt", "w+")

file.write("Financial Analysis\n")

file.write("\n-------------------------------------\n")

file.write(f"\nTotal Months: {len(months)}\n")
file.write(f"\nTotal: ${sum:,.0f}\n")
file.write(f"\nAverage Change: ${averagechange:,.2f}\n")
file.write(f"\nGreatest Increase in Profits: {greatest_increase_month} ${greatest_increase:,.0f}\n")
file.write(f"\nGreates Decrerase in Profits: {greatest_decrease_month} ${greatest_decrease:,.0f}\n")

file.close()