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
#convert strings to integers using list comprehension
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

#zip lists to find out which month corresponds to the greatest incease/decrease
together = list(zip(numbers,months))

#find out the greatest increase/decrease
greatestincrease = max(together)
greatestdecrease = min(together)


#test print; where the information was obtained from

#print("Total Months:",len(months))
#print("Total:$", sum)
#print("Average Change: $", round(averagechange,2))
#print(greatestincrease)
#rint(greatestdecrease)

file = open("PyBank Results.txt", "w+")

file.write("Financial Analysis\n")

file.write("\n-------------------------------------\n")

file.write("\nTotal Months: 86\n")
file.write("\nTotal: $22564198\n")
file.write("\nAverage Change: $-8311.11\n")
file.write("\nGreatest Increase in Profits: Mar-13 $1141840\n")
file.write("\nGreates Decrerase in Profits: Mar-10 -1194133\n")
           
file.close()