from models import AmountError, BaseEntry
from repository import EntryRepository
from utils import take_user_entry, choose_record_type

repo = EntryRepository()    

# Showing options while asking user for the input
while True:
    menu_choice = input(("""Menu Options:
            1. Add a record
            2. Get Records
            3. 
            4.         
            0. Exit
            
            ==> """))

    match menu_choice:
        case "1":
            record_type = choose_record_type()
            
            if record_type == None:
                    break

            category, description, amount = take_user_entry()
            # Structuring the data before sending it to save it as dictionary
            entry = BaseEntry(category, description, amount, record_type)
            breakpoint()
            # Calling to add the dictionary to the temporary list created in repo
            repo.save_to_csv(entry.to_dict())

        case "2":
            repo.get_data_from_csv()

        case "0":
            print("Operation Ended.")
            break

        case _:
            print("Function Not Available")

