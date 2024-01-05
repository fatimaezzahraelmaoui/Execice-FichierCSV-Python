import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f , delimiter= ",")
    for row in reader:
            print (row)