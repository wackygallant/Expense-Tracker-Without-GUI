from models import AmountError, Expense, Income, EntryRepository

def take_user_entry():    
    # Taking user inputs for the instances
    category = input("Category: ").capitalize()
    description = input("Description: ").capitalize()
    # Checking if the user input amount is in negative
    while True:
        try:
            amount = float(input("Amount:"))
            if amount <=0:
                raise AmountError
            return category, description, amount
        except ValueError:
            print("Please enter a valid number!")
        except AmountError:
            print("Amount must be a positive number!")


# Showing Options and Asking user for the input
while True:
    print("""Menu Options:
            1. Add Income/Expense
            2. Verify Entries
            3. Save Updates to CSV 
            4. Get Updates From CSV        
            0. Exit
        """)

    menu_choice = input("Please select an option: ")
    match menu_choice:
        case "1":
            print("Selected: 1. Add Income/Expense")
            sub_menu_choice = input("(1) For Income \n(2) For Expense\n-->")
            if sub_menu_choice == "1":
                category, description, amount = take_user_entry()
                Income(category, description, amount).add_income()

            elif sub_menu_choice == "2":         
                category, description, amount = take_user_entry()
                Expense(category, description, amount).add_expense()
            else:
                print("Invalid Input")
                break

            print("Data Added to temporary list")

        case "2":
            print("Selected: 2. Verify Entries")
            print("EXPENSES")
            records = EntryRepository.show_expense_records()
            if not records:
                print("There are no expenses recorded.")
            else:
                for record in records:
                    print(record)
            
            print("INCOMES")
            records = EntryRepository.show_income_records()
            if not records:
                print("There are no incomes recorded.")
            else:
                for record in records:
                    print(record)

        case "3":
            EntryRepository.save_to_csv()

        case "4":
            pass

        case "0":
            print("Operation Ended.")
            break

        case _:
            print("Function Not Available")

