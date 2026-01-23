import os
import csv

class EntryRepository:
    def __init__(self):
        self.file_path = "records.csv"

    def save_to_csv(self, data : dict):
        if data:
            file_path_exists = os.path.exists(self.file_path)
            write_header = not file_path_exists or os.stat(self.file_path).st_size == 0
            breakpoint()
            # Open the CSV file in append mode
            with open(self.file_path, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                if write_header:
                    writer.writeheader()
                writer.writerow(data)
            print(f"Data appended to the CSV file '{self.file_path}' successfully.")
        else:
            print(f"No data to append in '{self.file_path}'.")

    
    def get_data_from_csv(self, filter_key, filter_value):
        with open(self.file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            breakpoint()
            matches = [row for row in reader if row[filter_key] == filter_value]

        # Read filtered data
        if matches:
            for row in matches:
                print(row)
            else:
                print("No Data Found")


    def generate_next_id(self, starting_id: int = 1) -> int:
        # If file doesn't exist or is empty → start fresh
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            return starting_id

        with open(self.file_path, mode='r', newline='') as f:
            reader = list(csv.DictReader(f))

            if not reader:
                return starting_id

            last_id = int(reader[-1]["id"])
            return last_id + 1


