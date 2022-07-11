import numbers
import os

#importing csv file 
import csv

#List Variables
months =[]
profit_loss = []
month_profit_change = []

# variables with inital value of 0
total_amount = 0
row_count = 0
open_profit = 0
profit_changes = 0
net_profit_loss = 0

# Read the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  # reading the header line into csv_header
  csv_header = next(csvreader)
  for i in csvreader:
    #appeding month values to months list and profit/Loss values to profit_loss list
    months.append(i[0])
    profit_loss.append(i[1])

    #calculating total months with row_count and total amount in i[1]
    close_profit = int(i[1])
    row_count += 1
    total_amount += close_profit

    if (row_count == 1):
       open_profit = close_profit
    else:
      profit_changes = close_profit - open_profit

      month_profit_change.append(profit_changes)
    
      open_profit = close_profit

#calculating the net profit loss and average profit change
net_profit_loss = sum(month_profit_change)
average_profit_changes = (net_profit_loss/(row_count-1))

# greatest increase and decrease along with the months
greatest_profit_increase = max(month_profit_change)
greatest_profit_decrease = min(month_profit_change)

increase_month = months[month_profit_change.index(greatest_profit_increase)+1]
decrease_month = months[month_profit_change.index(greatest_profit_decrease)+1]

#printing the values to terminal
print("Financial Analysis")
print("----------------------------------------")
print(f"Total_months: {row_count}")   
print(f"Total: ${total_amount}")
print(f"Average Change: ${round(average_profit_changes,2)}")
print(f"Greatest Increase in profits: {increase_month} (${greatest_profit_increase})")
print(f"Greatest Decrease in profits: {decrease_month} (${greatest_profit_decrease})")

#writing to text file
Pybank = os.path.join('Analysis', 'Pybank.txt')
with open(Pybank, 'w') as txtfile:
  txtfile.write("Financial Analysis")
  txtfile.write("----------------------------------------")
  txtfile.write(f"Total_months: {row_count}")   
  txtfile.write(f"Total: ${total_amount}")
  txtfile.write(f"Average Change: ${round(average_profit_changes,2)}")
  txtfile.write(f"Greatest Increase in profits: {increase_month} (${greatest_profit_increase})")
  txtfile.write(f"Greatest Decrease in profits: {decrease_month} (${greatest_profit_decrease})")
