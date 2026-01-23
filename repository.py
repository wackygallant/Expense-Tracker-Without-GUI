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

    
    def get_data_from_csv(self):
        with open(self.file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for record in reader:
                print(record)


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

