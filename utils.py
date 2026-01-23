from models import AmountError


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
            

def choose_record_type():
    while True:
        choice = input("1. Income\n2. Expense\n0. Cancel\n==> ")
        match choice:
            case "1": return "Income"
            case "2": return "Expense"
            case "0": return None
            case _: print("Invalid option")

            