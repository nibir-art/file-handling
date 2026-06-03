f=open("marks.txt","a")
for i in range(5):
    a=input("Enter your name")
    b=int(input("Enter your contact info"))
    z=a+","+str(b)+"\n"
    f.write(z)
f.close()