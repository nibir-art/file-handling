import csv
with open("Employee.csv", "r") as fh:
    ereader = csv.reader(fh)
    print("FileEmployee.csv contains:")
    for rec in ereader:
        print(rec)