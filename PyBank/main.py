#import libraries
import os
import csv
#create empty lists to store total months and profit/losses
months = []
profitloss = []
#create the path for the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#read in the csv file and identify the headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"{csv_header}")
#divide the columns into two separate lists
    for row in csvreader:
        months.append(row[0])
        profitloss.append(row[1])
#convert strings to integers 
numbers = [int(i) for i in profitloss]
#print the total amount of months as reference
print("The total amount of months in the first column is",len(numbers), "months")

#find the total amount of Profit/Losses over the entire period
sum = sum(numbers)

#find the changes in profit over the entire period
lastmonth = numbers[85]
firstmonth = numbers[0]
change = lastmonth - firstmonth
averagechange = change/85
#test print
print("Total Months:",len(months))
print(" Total:$", sum)
print("Average Change: $", round(averagechange,2))
#findgreatesincrease/decrease
greatestincrease = max(numbers)
greatestdecrease = min(numbers)

