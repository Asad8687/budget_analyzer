import json
from app.config import DATA_FILE
from budget.models import Expense

def load_expenses():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        return [Expense(item["amount"], item["category"]) for item in data]

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump([e.to_dict() for e in expenses], file, indent=4)
