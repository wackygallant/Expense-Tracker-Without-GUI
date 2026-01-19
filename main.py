from models import AmountError, Expense, Income, ListParser

# Showing Options and Asking user for the input
while True:
    print("""Options:
            1. Add Expenses
            2. Add Income
            3. Verify Expenses Entry
            4. Verify Income Entry
            5. Save Updates to CSV 
            6. Get Updates From CSV        
            0. Exit
        """)

    user_response = input("Please Select an option: ")
    match user_response:
        case "1":
            # Taking user inputs for the instances
            category = input("Category: ")
            description = input("Description: ")
            # Checking if the user input amount is in negative
            try:
                amount = float(input("Amount: "))
                if amount < 0:
                    raise AmountError
            except AmountError:
                print("Amount must be positive")
                continue

            # Instantiating the expense
            expense_entry = Expense(category, description, amount)
            expense_entry.add_expense()

        case "2":
            # Taking user inputs for the instances
            category = input("Category: ")
            description = input("Description: ")
            # Checking if the user input amount is in negative
            try:
                amount = float(input("Amount: "))
                if amount < 0:
                    raise AmountError
            except AmountError:
                print("Amount must be positive")
                continue
            
            # Instantiating the expense
            income_entry = Income(category, description, amount)
            income_entry.add_income()

        case "3":
            records = ListParser.show_expense_records()
            if not records:
                print("There are no expenses recorded.")
            else:
                for record in records:
                    print(record)

        case "4":
            records = ListParser.show_income_records()
            if not records:
                print("There are no incomes recorded.")
            else:
                for record in records:
                    print(record)
        
        case "5":
            ListParser.save_to_csv()

        case "6":
            pass

        case "0":
            print("Operation Ended.")
            break

        case _:
            print("Function Not Available")

