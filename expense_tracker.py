import csv
from datetime import *

#create a csv file
FileName="expense.csv"

def add_expences():
    
    date=datetime.now().strftime("%d-%m-%y")
    category=input("shopping,cinema,travel:")
    amount=int(input("enter amount:"))
               
    with open(FileName,"a",newline="")as file:
        write=csv.writer(file)
        write.writerow([date,category,amount])
        
def show_expences():
    total=0
    with open(FileName,"r") as file:
        read=csv.reader(file)
        print("date  | category | amount")
        print("-----------------------------")
        
        for row in read:
            print(f"{row[0]} | {row[1]} | {row[2]}")
            total += int(row[2])
        print(f"Total amount spent: {total}")
            

while True:
    print("1.add_expence\n")
    print("2.show_expence\n")
    print("3.exit")
    choose=int(input("enter your choice (1,2,3):"))
    if choose==1:
        add_expences()
    elif choose==2:
        show_expences()
    elif choose==3:
        print("exit")
    else:
        print("invalid choice")
                
