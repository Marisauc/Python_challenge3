import os
import csv

Revenue = []

#Set csv pathway
budget_data = os.path.join("PyBank", "resources", "budget_data.csv")

#open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#read header first (skip)
    csv_header = next(csv_file)    
    #print(f"Header: {csv_header}")

#Make list 
    # counter = 0
    # for row in csv_reader:
    #     counter +=1
    # print(counter)

 #importing profit/loss data
    for row in csv_reader:
        Revenue.append(row[1])
    #print(Revenue)

# convert string to int
    for i in range(0, len(Revenue)):
        Revenue[i] = int(Revenue[i])
    #print(Revenue)

#find sum using function
    Sum = sum(Revenue)
    print(Sum)

#  changes in loss/profit
    for i in range(1, len(Revenue)):
        print(Revenue[i])



                       
    
 


    
