import pickle
from datetime import datetime

total_earnings = 0
expenses_list = []
spending_categories = {}

def main():
    load_financial_data()  
    while True:
        print("Money Manager Menu:")
        print("1. Add Earnings")
        print("2. Add Expenditure")
        print("3. View Transactions")
        print("4. View Remaining Budget")
        print("5. Save and Quit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            add_earnings()
        elif user_choice == "2":
            add_expenditure()
        elif user_choice == "3":
            view_transactions()
        elif user_choice == "4":
            view_budget_status()
        elif user_choice == "5":
            save_financial_data()
            break
        else:
            print("Invalid choice. Please try again.")

def add_earnings():
    global total_earnings
    amount = get_valid_amount("Enter earnings amount: ")
    total_earnings += amount
    print("Earnings added successfully!")

def add_expenditure():
    global total_earnings
    global expenses_list
    global spending_categories
    category = input("Enter expenditure category: ")
    amount = get_valid_amount("Enter expenditure amount: ")
    expenses_list.append((category, amount, datetime.now()))
    total_earnings -= amount
    spending_categories[category] = spending_categories.get(category, 0) + amount
    print("Expenditure added successfully!")

def view_transactions():
    global expenses_list
    for category, amount, timestamp in expenses_list:
        print(f"Category: {category}, Amount: {amount}, Time: {timestamp}")

def view_budget_status():
    global total_earnings
    global expenses_list
    remaining_budget = total_earnings - sum(amount for _, amount, _ in expenses_list)
    print(f"Remaining Budget: {remaining_budget}")

def save_financial_data():
    global total_earnings
    global expenses_list
    global spending_categories
    data = {
        "total_earnings": total_earnings,
        "expenses_list": expenses_list,
        "spending_categories": spending_categories,
    }
    with open("financial_data.pkl", "wb") as file:
        pickle.dump(data, file)
    print("Financial data saved successfully!")

def load_financial_data():
    global total_earnings
    global expenses_list
    global spending_categories
    try:
        with open("financial_data.pkl", "rb") as file:
            data = pickle.load(file)
            total_earnings = data["total_earnings"]
            expenses_list = data["expenses_list"]
            spending_categories = data["spending_categories"]
        print("Financial data loaded successfully!")
    except FileNotFoundError:
        pass

def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:
                return amount
            else:
                print("Amount must be non-negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
