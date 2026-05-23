import csv
fh = open("Employee.csv", "w", newline="")
ewriter = csv.writer(fh)
empdata=[
    ['Empno','Name', 'Designation', 'Salary'],
    [101, 'Rahul', 'Manager', 50000],
    [102, 'Aman', 'Developer', 40000],
    [103, 'Arjun', 'Tester', 30000],
    [104, 'Priya', 'Designer', 35000]]
ewriter.writerows(empdata)
print("File successfully created.")
fh.close()

import csv
with open("Employee.csv", "r") as fh:
    ereader = csv.reader(fh)
    print("FileEmployee.csv contains:")
    for rec in ereader:
        print(rec)