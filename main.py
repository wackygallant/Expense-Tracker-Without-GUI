from models import BaseEntry
from repository import EntryRepository
from utils import choose_filter_type, take_user_entry, choose_record_type

repo = EntryRepository()    

# Showing options while asking user for the input
while True:
    menu_choice = input("Menu Options:\n1. Add Record\n2. Get Records\n3. Get Remaining Balance(Savings)\n0. Exit\n==>")

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
            print("\n\nData appended to the csv file!!!\n\n")

        case "2":
            # Gets the filter values and returns the matching values from the csv
            filter_key, filter_value = choose_filter_type()
            data_list = repo.get_data_from_csv(filter_key, filter_value)
            if data_list:
                for data in data_list:
                    print(data)
            else:
                print("\n\nNo Data Found\n\n")

        case "3":
            pass

        case "0":
            print("\n\nOperation Ended.\n\n")
            break

        case _:
            print("\n\nFunction Not Available!!!\n\n")