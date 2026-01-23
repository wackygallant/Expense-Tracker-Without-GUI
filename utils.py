from models import AmountError

def take_user_entry():    
    # Taking user inputs for the instances
    category = input("Category: ").lower()
    description = input("Description: ").lower()
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
            case "1": return "income"
            case "2": return "expense"
            case "0": return None
            case _: print("Invalid Option!!!")

def choose_filter_type():
    while True:
        choice = input("1. By Record Type\n2. By Category\n0. Cancel\n==> ")
        match choice:
            case "1": return ("record_type", input("Enter filter value: ").lower())
            case "2": return ("category", input("Enter filter value: ").lower())
            case "0": return None
            case _: print("Invalid option")
            