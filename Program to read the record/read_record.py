import csv
with open("student.csv", "r") as fh:
    ereader = csv.reader(fh)
    for rec in ereader:
        print(rec)