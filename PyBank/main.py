import csv

pybank = "budget_data.csv"

with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        count = sum(1 for row in csvreader)
    
with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        total_sum = sum(int(row[1]) for row in csvreader)
        
rows = []
rows_stagger = []

with open(pybank, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvreader:
        rows.append(int(row[1]))
with open(pybank, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    next(csvfile)
    for row in csvreader:
        rows_stagger.append(int(row[1]))
        
dfrows = [x1-x2 for (x1,x2) in zip(rows_stagger, rows)]
dfrows_avg = (sum(dfrows))/(count -1)
        
with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        max_val = max(int(row[1]) for row in csvreader)

with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        max_month = [str(row[0]) for row in csvreader if int(row[1]) == max_val]
        
with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        min_val = min(int(row[1]) for row in csvreader)

with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        min_month = [str(row[0]) for row in csvreader if int(row[1]) == min_val]

print(f"Total Months: {count}")
print(f"Total Sum: ${total_sum}.00")
print(f"Average Change: ${round(dfrows_avg, 2)}")
print(f"Greatest Increase in Profits: {max_month[0]} (${max_val}.00)")
print(f"Greatest Decrease in Profits: {min_month[0]} (${min_val}.00)")

f = open("pybank_results.txt", 'w')
f.write(f"Total Months: {count}\n")
f = open("pybank_results.txt", 'a')
f.write(f"Total Sum: ${total_sum}.00\n")
f = open("pybank_results.txt", 'a')
f.write(f"Average Change: ${round(dfrows_avg, 2)}\n")
f = open("pybank_results.txt", 'a')
f.write(f"Greatest Increase in Profits: {max_month[0]} (${max_val}.00)\n")
f = open("pybank_results.txt", 'a')
f.write(f"Greatest Decrease in Profits: {min_month[0]} (${min_val}.00)\n")
f.close