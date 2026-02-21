# 💰 CLI Expense Tracker

A simple, lightweight command-line expense tracker built with Python. No external libraries required — just Python and your terminal.

## Features

- ➕ **Add** expenses with description, category, and amount
- 📋 **View** all expenses in a formatted table
- ✏️ **Edit** any expense — change amount, category, or fix a typo
- 🗑️ **Delete** expenses by ID
- 📊 **Summary** — total spending broken down by category

## Getting Started

```bash
# Clone the repo
git clone https://github.com/kunal-gswm/expense-tracker.git
cd expense-tracker/expense-tracker-cli/expense-tracker

# Run the tracker
python expense_tracker.py
```

## Usage

```
========================================
   💰  CLI Expense Tracker
========================================

  What would you like to do?
  [1] Add Expense
  [2] View All Expenses
  [3] Delete Expense
  [4] Edit Expense
  [5] Summary / Total
  [6] Exit
```

Data is stored locally in `expenses.json` in the same directory.

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON file (no database needed)
