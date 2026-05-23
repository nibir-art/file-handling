import csv
fh = open("student.csv", "w")
cwriter = csv.writer(fh)
compdata=[
    ['Name', 'Points', 'Ranks'],
    ['Rahul', 90, 1],
    ['Aman', 85, 2],
    ['Arjun', 95, 1],
    ['Priya', 88, 3]]
cwriter.writerows(compdata)
fh.close()