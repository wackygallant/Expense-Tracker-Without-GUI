from models import AmountError, Expense, Income
from repository import EntryRepository

repo = EntryRepository()

def take_user_entry():    
    # Taking user inputs for the instances
    category = input("Category: ").capitalize()
    description = input("Description: ").capitalize()
    # Checking if the user input amount is in negative
    while True:
        try:
            amount = float(input("Amount:"))
            if amount <= 0:
                raise AmountError
            return category, description, amount
        except ValueError:
            print("Please enter a valid number!")
        except AmountError:
            print("Amount must be a positive number!")


# Showing options while asking user for the input
while True:
    menu_choice = input(("""Menu Options:
            1. Add Income/Expense
            2. Verify Entries
            3. Save Updates to CSV 
            4. Get Updates From CSV        
            0. Exit
            
            ==> """))
    match menu_choice:
        case "1":
            print()

            sub_menu_choice = input("""Selected: 1. Add Income/Expense
                (1) Income
                (2) Expense

                ==> """)
            if sub_menu_choice == "1":
                category, description, amount = take_user_entry()
                # Structuring the data before sending it to save it as dictionary
                entry = Income(category, description, amount)
                # Calling to add the dictionary to the temporary list created in repo
                repo.add_income(entry.to_dict())

            elif sub_menu_choice == "2":         
                category, description, amount = take_user_entry()
                # Structuring the data before sending it to save it as dictionary
                entry = Expense(category, description, amount)
                # Calling to add the dictionary to the temporary list created in repo
                repo.add_expense(entry.to_dict())

            else:
                print("Invalid Input")
                break

            print("Data Added to temporary list")

        case "2":
            print("Selected: 2. Verify Entries")
            print("INCOMES")
            for record in repo.show_income_records():
                if record:
                    print(record)
                else:
                    print("No entry found for income!!!")

            print("EXPENSES")
            for record in repo.show_expense_records():
                if record:
                    print(record)
                else:
                    print("No entry found for expenses!!!")
                
        case "3":
            repo.save_to_csv()

        case "4":
            pass

        case "0":
            print("Operation Ended.")
            break

        case _:
            print("Function Not Available")

