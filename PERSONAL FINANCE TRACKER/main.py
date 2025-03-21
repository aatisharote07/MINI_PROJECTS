import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount,get_category,get_date,get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE="finance_data.csv"
    COLUMNS=["date","amount","category","description"]  
    FORMAT ="%d-%m-%Y"  
    @classmethod
    def initialized_csv(cls):
        try:
            df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\PROJECTS\PERSONAL FINANCE TRACKER\finance_data.csv")
        except FileNotFoundError: 
            df= pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)
    @classmethod
    def add_entry(cls,date,amount,category,description):
            new_entry={
                "date":date,
                "amount":amount,
                "category":category,
                "description":description
            }   
            with open(cls.CSV_FILE,"a", newline="") as csvfile:
                 writer= csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
                 writer.writerow(new_entry)
            print("Entry added succesfully")
    @classmethod
    def get_transactions(cls,start_date,end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"]= pd.to_datetime(df["date"],format=CSV.FORMAT)         
        start_date = datetime.strptime(start_date,CSV.FORMAT)
        end_date = datetime.strptime(end_date,CSV.FORMAT)
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
             print("No transactions found in the given date range")
        else:
            print(f"transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(
                  index=False,formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            total_credit = filtered_df[filtered_df["category"]=="Credit"]["amount"].sum()
            total_debit = filtered_df[filtered_df["category"]=="Debit"]["amount"].sum()
            print("\nSummary: ")
            print(f"Total Credit:₹{total_credit:.2f}")
            print(f"Total Debit:₹{total_debit:.2f}")
            print(f"Net savings:₹{total_credit-total_debit:.2f}")
        return filtered_df
def add():
    CSV.initialized_csv()
    date=get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for todays date: ",allow_default=True)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)
def plot_transactions(df):
    df.set_index('date',inplace=True)
    Credit_df=df[df["category"]== "Credit"].resample("D").sum().reindex(df.index, fill_value=0)
    Debit_df=df[df["category"]== "Debit"].resample("D").sum().reindex(df.index, fill_value=0)
    plt.figure(figsize=(10,5))
    plt.plot(Credit_df.index,Credit_df["amount"], label="Credit", color="g")
    plt.plot(Debit_df.index,Debit_df["amount"], label="Credit", color="r")
    plt.xlabel("Date")
    plt.ylabel("amount")
    plt.title("Credit and Debit over time")
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    while True: 
        print("\n1. Add a new Transaction")
        print("2. View Transactions and Summary within a date range")
        print("3. Exit")
        choice=input("Enter your choice(1-3): ")
        if choice=="1":
            add()
        elif choice=="2":
            start_date=get_date("Enter the start date(dd-mm-yyyy): ")
            end_date=get_date("Enter the end date(dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date,end_date)
            if input("Do you want to see a plot? (y/n): ").lower()=="y":
                plot_transactions(df)
        elif choice=="3":
            print("Exiting...")
            break             
        else:
            print("Invalid choice. Please enter a correct number(1-3).")
if __name__=="__main__":
    main()





