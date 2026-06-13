import logging
import json
import os

# Setup logging
logging.basicConfig(
    filename="transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Program started...")

# File for persistence
DATA_FILE = "transactions_data.json"

# Store all transactions
transactions_list = []


# Base Class
class Transaction:
    def __init__(self, amount, category):
        if amount < 0:
            logging.error("Negative amount entered")
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.category = category

    def display_info(self):
        print(f"Amount: {self.amount}, Category: {self.category}")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "amount": self.amount,
            "category": self.category
        }


# Subclasses
class Income(Transaction):
    def display(self):
        print("\n--- Income ---")
        self.display_info()


class Expense(Transaction):
    def display(self):
        print("\n--- Expense ---")
        self.display_info()


# Save transactions to JSON file
def save_data():
    data = [t.to_dict() for t in transactions_list]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# Load transactions from JSON file
def load_data():
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        for item in data:
            if item["type"] == "Income":
                transactions_list.append(Income(item["amount"], item["category"]))
            elif item["type"] == "Expense":
                transactions_list.append(Expense(item["amount"], item["category"]))
        print(f"Loaded {len(data)} saved transactions.")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Warning: Could not load saved data ({e})")


# Function to show all transactions
def show_all():
    if not transactions_list:
        print("\nNo transactions yet.")
        return

    print("\n--- All Transactions ---")
    for t in transactions_list:
        t.display_info()


# Function to calculate totals
def show_summary():
    total_income = 0
    total_expense = 0

    for t in transactions_list:
        if isinstance(t, Income):
            total_income += t.amount
        elif isinstance(t, Expense):
            total_expense += t.amount

    balance = total_income - total_expense

    print("\n--- Summary ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {balance}")


# Main function
def main():
    load_data()

    while True:
        print("\n===== MENU =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '5':
            print("Exiting...")
            break

        elif choice not in ['1', '2', '3', '4']:
            print("Invalid choice!")
            continue

        try:
            if choice in ['1', '2']:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")

                if choice == '1':
                    obj = Income(amount, category)
                else:
                    obj = Expense(amount, category)

                transactions_list.append(obj)
                save_data()
                obj.display()

            elif choice == '3':
                show_all()

            elif choice == '4':
                show_summary()

        except ValueError as e:
            print("Error:", e)


# Run program
if __name__ == "__main__":
    main()