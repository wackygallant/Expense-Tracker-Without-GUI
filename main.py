from models import AmountError, BaseEntry
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
            1. Add a record
            2. Get records
            3. 
            4.         
            0. Exit
            
            ==> """))
    match menu_choice:
        case "1":
            category, description, amount = take_user_entry()
            # Structuring the data before sending it to save it as dictionary
            entry = BaseEntry(category, description, amount)
            # Calling to add the dictionary to the temporary list created in repo
            breakpoint()
            repo.save_to_csv(entry.to_dict())

        case "2":
            repo.get_data_from_csv()

        case "0":
            print("Operation Ended.")
            break

        case _:
            print("Function Not Available")

