def budget_tracker():
    transactions = []
    categories = ["food", "rent", "entertainment", "other"]
    types = ["income", "expense"]
    menu = """
Budget Tracker:
1. Add income or expense
2. Show all transactions
3. Filter transactions by category
4. Show current balance
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose a number to perform a task: ").strip()
        if choice == '1':
            type = input("Enter 'Income' or 'Expense': ").strip().lower()
            if type not in types:
                print("You must choose Income or Expense.")
                continue
            description = input("Enter the description: ").strip().capitalize()
            if not description:
                print("You must enter a description.")
                continue
            try:
                amount = float(input("Enter the amount: ").strip())
                if not amount:
                    print("You must enter a value.")
                    continue
                elif amount <= 0:
                    print("The amount must be greater then 0.")
                elif type == 'expense':
                    amount = -amount
            except ValueError:
                print("You must put only numbers.")
                continue
            category = input("Enter the category (Food/Rent/Entertainment/Other): ").strip().lower()
            if category not in categories:
                print("You must choose from the relevant categories.")
                continue
            else:
                entry = {"Type": type, "Description": description, "Amount": amount, "Category": category}
                transactions.append(entry)
                print(f"""Added entry:
Type: {entry['Type'].capitalize()}
Description: {entry['Description'].capitalize()}
Amount: {entry['Amount']}
Category: {entry['Category'].capitalize()}\n""")
        elif choice == '2':
            if not transactions:
                print("No transactions to show.")
            else:
                for index, transaction in enumerate(transactions, start= 1):
                    print(f"{index}. {transaction['Type'].capitalize()}: {transaction['Description'].capitalize()} - Amount: {float(transaction['Amount'])} (Category: {transaction['Category'].capitalize()})")
        elif choice == '3':
            filter = input("Enter the category to filter by (Food/Rent/Entertainment/Other): ").lower().strip()
            if not transactions:
                print("No transactions to show.")
            else:
                if filter == 'food':
                    for index, transaction in enumerate(transactions, start= 1):
                        if transaction['Category'] == 'food':
                            print(f"{index}. {transaction['Type'].capitalize()}: {transaction['Description'].capitalize()} - Amount: {float(transaction['Amount'])} (Category: {transaction['Category'].capitalize()})")
                elif filter == 'rent':
                    for index, transaction in enumerate(transactions, start= 1):
                        if transaction['Category'] == 'rent':
                            print(f"{index}. {transaction['Type'].capitalize()}: {transaction['Description'].capitalize()} - Amount: {float(transaction['Amount'])} (Category: {transaction['Category'].capitalize()})")
                elif filter == 'entertainment':
                    for index, transaction in enumerate(transactions, start= 1):
                        if transaction['Category'] == 'entertainment':
                            print(f"{index}. {transaction['Type'].capitalize()}: {transaction['Description'].capitalize()} - Amount: {float(transaction['Amount'])} (Category: {transaction['Category'].capitalize()})")
                elif filter == 'other':
                    for index, transaction in enumerate(transactions, start= 1):
                        if transaction['Category'] == 'other':
                            print(f"{index}. {transaction['Type'].capitalize()}: {transaction['Description'].capitalize()} - Amount: {float(transaction['Amount'])} (Category: {transaction['Category'].capitalize()})")
                else:
                    print("You must choose from the relevant categories.")        
        elif choice == '4':
            result = sum(transaction['Amount'] for transaction in transactions)
            print(result)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

budget_tracker()
