import datetime
class Expense:
    def __init__(self, expense_id, date, category, description, amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return (f"ID: {self.expense_id}, Date: {self.date}, "
                f"Category: {self.category}, Description: {self.description}, "
                f"Amount: ${self.amount}")


# 3. Data Storage

expenses = []


def add_expense(expense):
    expenses.append(expense)


def update_expense(expense_id, new_expense):
    for i, exp in enumerate(expenses):
        if exp.expense_id == expense_id:
            expenses[i] = new_expense
            return
    print("Expense ID not found.")


def delete_expense(expense_id):
    global expenses
    for i,exp in enumerate(expenses):
        if exp.expense_id== expense_id:
            removed = expenses.pop(i)
            print(f"Expense removed{removed}")
            return
    print("Expense Not Found")

def display_expenses():
    for exp in expenses:
        print(exp)


# 4. User Authentication

cred ={
    'arun':'password@1',
    'raj':'password@2'
}


def authenticate_user(username,password):
    if username in cred and cred[username] == password:
        print("Authentification is Successful")
        return True
    else:
        print("Authentification failure")
        return False


# 5. Categorization and Summarization

def categorize_expenses():
    categories = {}
    for exp in expenses:
        if exp.category not in categories:
            categories[exp.category] = 0
        categories[exp.category] += exp.amount
    return categories


def summarize_expenses():
    total=0
    for exp in expenses:
        total +=exp.amount
    return total


# 6. Functions for Repetitive Tasks

def calculate_total_expenses():
    total_expense=0
    for exp in expenses:
        total_expense+=exp.amount

    return total_expense


def generate_summary_report():
    categorized = categorize_expenses()
    print("Category Summary:")
    for category, total in categorized.items():
        print(f"{category}: ${total}")
    print(f"Total Expenses: ${calculate_total_expenses()}")


# 7. Simple CLI for Interaction

def cli():
    print("\nMenu:")
    print("1. Add a new expense")
    print("2. Update an existing expense")
    print("3. Delete an expense")
    print("4. Display all expenses")
    print("5. Generate a summary report")
    print("6. Exit")

    option = input("Select an option(1-6) ")

    if option == '1':
        expense_id = input("Enter Expense ID:")
        date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        amount = float(input("Enter Amount: "))
        add_expense(Expense(expense_id, date, category, description, amount))
        cli()
    elif option == '2':
        expense_id = input("Enter expense ID to update: ")
        date = input("Enter new date (YYYY-MM-DD): ")
        category = input("Enter new category: ")
        description = input("Enter new description: ")
        amount = float(input("Enter new amount: "))
        update_expense(expense_id, Expense(expense_id, date, category, description, amount))
        cli()
    elif option == '3':
        expense_id = input("Enter expense ID to delete: ")
        delete_expense(expense_id)
        cli()

    elif option == '4':
        display_expenses()
        cli()
    elif option == '5':
        generate_summary_report()
        cli()

    elif option == '6':
        print("Exiting...")

    else:
        print("Invalid option, please try again.")
        cli()



# 8. Run the program and verify the results

def main():
    print("*"*10,"Expense Tracker","*"*10)
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate_user(username, password):
        cli()
    else:
        print("Failed to authenticate.")


if __name__ == "__main__":
    main()


