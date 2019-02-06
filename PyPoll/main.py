import csv

pypoll = "election_data.csv"

with open(pypoll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        total_count = sum(1 for row in csvreader)

candidates = []

with open(pypoll, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvreader:
        candidates.append(row[2])

candidates = list(set(candidates))

count_0 = 0

with open(pypoll, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[2] == candidates[0]:
            count_0 += 1
perc_0 = float((count_0 / total_count)*100)

count_1 = 0

with open(pypoll, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[2] == candidates[1]:
            count_1 += 1
perc_1 = float((count_1 / total_count)*100)

count_2 = 0

with open(pypoll, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[2] == candidates[2]:
            count_2 += 1
perc_2 = float((count_2 / total_count)*100)

count_3 = 0

with open(pypoll, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[2] == candidates[3]:
            count_3 += 1
perc_3 = float((count_3 / total_count)*100)

if (
    count_0 > count_1
    and count_0 > count_2 
    and count_0 > count_3
    ):
    win = str(candidates[0])
elif (
    count_1 > count_0
    and count_1 > count_2
    and count_1 > count_3
    ):
    win = str(candidates[1])
elif (
    count_2 > count_1
    and count_2 > count_0
    and count_2 > count_3
    ):
    win = str(candidates[2])
else:
    win = str(candidates[3])
    
print("Election Results")
print("---------------------")
print(f"Total Votes: {total_count}")
print("---------------------")
print(f"{candidates[0]}: {round(perc_0)}% ({count_0})")
print(f"{candidates[1]}: {round(perc_1)}% ({count_1})")
print(f"{candidates[2]}: {round(perc_2)}% ({count_2})")
print(f"{candidates[3]}: {round(perc_3)}% ({count_3})")
print("---------------------")
print(f"Winner: {win}")