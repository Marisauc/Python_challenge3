import csv

#Set csv pathway
budget_data = "Resources/budget_data.csv"


#open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#read header first (skip)
    csv_header = next(csv_file)    

#Make lists
    Revenue = []
    profit_loss = []
    profit_loss_change = []
    total = 0
    max_change = 0
    min_change = 0
    max_month = " "
    min_month = " "

 #append local list to include each month, total profit/loss , and provit/loss
    for row in csv_reader:
        Revenue.append(row[1])
        total+= float(row[1])
        profit_loss.append(float(row[1]))

# create for loop to give change over months for profit/loss
    for x in range(1, len(profit_loss)):
        profit_loss_change.append(profit_loss[x] - profit_loss[x-1])
        if (profit_loss[x] - profit_loss[x-1]) > max_change:
            max_change = (profit_loss[x] - profit_loss[x-1])
            max_month = Revenue[x]
        if (profit_loss[x] - profit_loss[x-1]) < min_change:
            min_change = (profit_loss[x] - profit_loss[x-1])
            min_month = Revenue[x] 

 #Calculate average change for profit/loss                
    average_change = round(sum(profit_loss_change) / len(profit_loss_change), 2)
    

# Print results in terminal
print("Total Months: " + str(len(Revenue)))
print("Total Revenue: " + '${:,.2f}'.format(total))
print("Average Revenue Change: " + '${:,.2f}'.format(average_change))
print("Greatest Increase in Profits: " + str(max_month) +
      " " + '${:,.2f}'.format(max_change))
print("Greatest Decrease in Profits: " + str(min_month) +
      "  " + '${:,.2f}'.format(min_change))

# This will output to a file called Analysis my findings
output = "Analysis.txt"
with open(output, "w+") as file:
    file.write("Financial Analysis\n")
    file.write(" ----------------------------\n")
    file.write("Total Months: " + str(len(Revenue))+"\n")
    file.write("Total Revenue: " + '${:,.2f}'.format(total)+"\n")
    file.write("Average Revenue Change: " +
               '${:,.2f}'.format(average_change)+"\n")
    file.write("Greatest Increase in Profits: " + str(max_month) +
               " " + '${:,.2f}'.format(max_change)+"\n")
    file.write("Greatest Decrease in Profits: " + str(min_month) +
               " " + '${:,.2f}'.format(min_change)+"\n")


                       
    
 


    
