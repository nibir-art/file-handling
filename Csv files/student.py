count=int(input("Enter the number of students: "))
fileout=open("mark.txt","w")
for i in range(count):
    print("Enter details of student ", (i+1),"below: ")
    name=input("Enter the name of student: ")
    rollno=int(input("Enter the marks of student: "))
    rec=str(rollno) + " " + name + " " + str(marks) + "\n"
    fileout.write(rec)
fileout.close() 
