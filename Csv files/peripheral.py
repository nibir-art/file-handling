import csv
def Add_Device():
    try:
        with open('peripheral.csv','a', newline='') as file:
            writer = csv.writer(file)
            P_id = int(input("Enter Peripheral ID: "))
            P_name = input("Enter Peripheral Name: ")
            Price=int(input(" enter peripheral price: "))
            writer.writerow([P_id,P_name, Price])
        print("Peripheral added successfully.")
    except Exception as e:
        print("An exception occured: ", e)

def Count_Device():
    try:    
        count=0
        with open('peripheral.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[2])>1000:
                    count += 1
        print(f"Number of peripherals with price greater than 1000: {count}")
    except FileNotFoundError:
        print("The file 'peripheral.csv' does not exist.")