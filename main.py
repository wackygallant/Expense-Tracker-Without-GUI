from models import BaseEntry
from repository import EntryRepository
from utils import choose_filter_type, take_user_entry, choose_record_type

repo = EntryRepository()    

# Showing options while asking user for the input
while True:
    menu_choice = input("\nMenu Options:\n1. Add Record\n2. Get Records\n3. Summary\n0. Exit\n==>")

    match menu_choice:
        case "1":
            record_type = choose_record_type()
            
            if record_type == None:
                break

            category, description, amount = take_user_entry()
            # Structuring the data before sending it to save it as dictionary
            entry = BaseEntry(category, description, amount, record_type)
            # Calling to add the dictionary to the temporary list created in repo
            repo.save_to_csv(entry.to_dict())
            print("\nData appended to the csv file!!!\n")

        case "2":
            # Gets the filter values and returns the matching values from the csv
            filter_key, filter_value = choose_filter_type()
            data_list = repo.get_data_from_csv(filter_key, filter_value)
            if data_list:
                for data in data_list:
                    print(data)
            else:
                print("\nNo Data Found\n")

        case "3":
            while True:
                choice = input("\n1. Get Total Income\n2. Get Total Expenses\n3. Get Balance\n0. Go back\n==> ")
                match choice:
                    case "1": 
                        print(f"\Your total income till date is Rs.{repo.get_total_income()}\n")
                        break
                    case "2":
                        print(f"\nYour total expense till date is Rs.{repo.get_total_expense()}\n")
                        break
                    case "3":
                        if repo.get_total_income() > repo.get_total_expense():
                            print(f"\nYou have Rs.{repo.check_balance()} left.\n")
                        else:
                            print(f"\nYou are Rs.{repo.check_balance()} on debt.\n")
                        break     
                    case "0": 
                        break                    
                    case _: 
                        print("\nInvalid Option!!!\n")
                        continue

        case "0":
            print("\nOperation Ended.\n")
            break

        case _:
            print("\nFunction Not Available!!!\n")