from budget.storage import load_expenses, save_expenses
from budget.models import Expense
from app.logger import get_logger

logger = get_logger()

def add_expense(expenses):
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid number")
        return

    category = input("Category: ").strip()
    if not category:
        print("Category required")
        return

    expense = Expense(amount, category)
    expenses.append(expense)
    save_expenses(expenses)

    logger.info("Expense added")
    print("Expense saved")

def show_expenses(expenses):
    for e in expenses:
        print(f"{e.category}: {e.amount}")

def show_total(expenses):
    total = sum(e.amount for e in expenses)
    print(f"Total: {total}")

def main():
    expenses = load_expenses()
    logger.info("Program started")

    while True:
        print("\n1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            logger.info("Program ended")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
