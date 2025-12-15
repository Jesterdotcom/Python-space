import pandas as pd

data = pd.read_csv('exp.csv')
df = pd.DataFrame(data)

def total_expense_grouped():
    grouped = df.groupby("Category")["Amount"].sum()
    print("Categorised by amount spent")
    print(grouped)

def total():
    total = df["Amount"].sum()
    print("The total amount you spent is ",total)

def mnm():
    row = df.max()
    print(row)
def nmn():
    row = df.min()
    print(row)

def display():
    print("Choose your option"
    "\n1. View Data"
    "\n2. View expense in group"
    "\n3. View total amount spent"
    "\n4. View max amount details"
    "\n5. View min amount details")

def main():
    
    display()
    try:
        c = int(input("Enter your choice:"))
        print()
        if c == 1:
            print("ORIGINAL DATA")
            print(df)
        elif c == 2:
            total_expense_grouped()
        elif c == 3:
            total()
        elif c == 4:
            mnm()
        elif c == 5:
            nmn()
        else:
             ("Invalid input")
    except ValueError:
            print("\nError: Invalid input")

while True :
        print("\nWelcome to Expense Tracker")
        main()