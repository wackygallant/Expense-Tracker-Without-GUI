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
    # Prompts user to choose which record to add, returns income or expense or None
    while True:
        choice = input("\n1. Income\n2. Expense\n0. Cancel\n==> ")
        match choice:
            case "1": return "income"
            case "2": return "expense"
            case "0": return None
            case _: print("\nInvalid Option!!!\n")

def choose_filter_type():
    # Prompts user for the filter values and returns filter_key and filter_value
    while True:
        choice = input("\n1. By Record Type\n2. By Category\n0. Cancel\n==> ")
        match choice:
            case "1": return ("record_type", input("Enter filter value: ").lower())
            case "2": return ("category", input("Enter filter value: ").lower())
            case "0": return None
            case _: print("\nInvalid Option!!!\n")
