import os
import csv

class EntryRepository:
    def __init__(self):
        self.file_path = "records.csv"

    # Saves to the CSV file
    def save_to_csv(self, data : dict):
        file_path_exists = os.path.exists(self.file_path)
        write_header = not file_path_exists or os.stat(self.file_path).st_size == 0
        # Opens the CSV file in append mode
        with open(self.file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if write_header:
                writer.writeheader()
            writer.writerow(data)


    # Generates an id
    def generate_next_id(self, starting_id: int = 1) -> int:
        # If file doesn't exist or is empty → start fresh
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            return starting_id

        # Opens the CSV file in read mode
        with open(self.file_path, mode='r', newline='') as file:
            reader = list(csv.DictReader(file))

            if not reader:
                return starting_id

            # Gets the last item on the list and returns the id field
            last_id = int(reader[-1]["id"])
            return last_id + 1

    def get_data_from_csv(self, filter_key, filter_value):
        # Opens the CSV file in read mode
        with open(self.file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            matches = [row for row in reader if row[filter_key] == filter_value]
            
        return matches

    def get_total_income(self):
        filter_key, filter_value = "record_type" , "income"
        amount_list = []
        for amount in self.get_data_from_csv(filter_key, filter_value): amount_list.append(float(amount['amount']))
        return sum(amount_list)

    def get_total_expense(self):
        filter_key, filter_value = "record_type" , "expense"
        amount_list = []
        for amount in self.get_data_from_csv(filter_key, filter_value): amount_list.append(float(amount['amount']))
        return sum(amount_list)

    def check_balance(self):
        return self.get_total_income() - self.get_total_expense()