import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
   
    print("\n── Add Expense ──")
    description = input("Description (e.g. Lunch, Rent): ").strip()
    if not description:
        print("  ⚠  Description cannot be empty.")
        return

    category = input("Category (e.g. Food, Travel, Bills) [Other]: ").strip()
    if not category:
        category = "Other"

    while True:
        amount_str = input("Amount (₹): ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("  ⚠  Please enter a valid positive number.")

    expense = {
        "id": len(expenses) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "description": description,
        "category": category,
        "amount": round(amount, 2),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\n  ✅ Added: {description}  ₹{amount:.2f}  [{category}]")


def view_expenses(expenses):
    
    print("\n── All Expenses ──")
    if not expenses:
        print("  No expenses recorded yet.")
        return

    print(f"{'ID':<5} {'Date':<17} {'Description':<20} {'Category':<12} {'Amount':>10}")
    print("─" * 68)
    for e in expenses:
        print(
            f"{e['id']:<5} {e['date']:<17} {e['description']:<20} "
            f"{e['category']:<12} ₹{e['amount']:>9.2f}"
        )
    print("─" * 68)


def delete_expense(expenses):
    print("\n── Delete Expense ──")
    view_expenses(expenses)
    if not expenses:
        return

    while True:
        id_str = input("\nEnter the ID to delete (or 0 to cancel): ").strip()
        try:
            exp_id = int(id_str)
            break
        except ValueError:
            print("  ⚠  Please enter a valid number.")

    if exp_id == 0:
        print("  Cancelled.")
        return
    original_len = len(expenses)
    expenses[:] = [e for e in expenses if e["id"] != exp_id]

    if len(expenses) < original_len:
        for i, e in enumerate(expenses, start=1):
            e["id"] = i
        save_expenses(expenses)
        print(f"  ✅ Expense ID {exp_id} deleted.")
    else:
        print(f"  ⚠  No expense found with ID {exp_id}.")


def show_summary(expenses):
    print("\n── Summary ──")
    if not expenses:
        print("  No expenses to summarise.")
        return

    total = sum(e["amount"] for e in expenses)

    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

    print(f"\n  {'Category':<20} {'Total':>10}")
    print("  " + "─" * 32)
    for cat, amt in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat:<20} ₹{amt:>9.2f}")
    print("  " + "─" * 32)
    print(f"  {'GRAND TOTAL':<20} ₹{total:>9.2f}")
    print(f"\n  ({len(expenses)} expense(s) recorded)")

def main():
    print("=" * 40)
    print("   💰  CLI Expense Tracker")
    print("=" * 40)

    expenses = load_expenses()

    menu = {
        "1": ("Add Expense",       lambda: add_expense(expenses)),
        "2": ("View All Expenses", lambda: view_expenses(expenses)),
        "3": ("Delete Expense",    lambda: delete_expense(expenses)),
        "4": ("Summary / Total",   lambda: show_summary(expenses)),
        "5": ("Exit",              None),
    }

    while True:
        print("\n  What would you like to do?")
        for key, (label, _) in menu.items():
            print(f"  [{key}] {label}")

        choice = input("\n  Enter choice: ").strip()

        if choice == "5":
            print("\n  Bye! Keep tracking those expenses. \n")
            break
        elif choice in menu:
            _, action = menu[choice]
            action()
        else:
            print("  ⚠  Invalid choice. Please enter 1–5.")


if __name__ == "__main__":
    main()
