import os
import csv

class EntryRepository:
    def __init__(self):
        self.expense_list = []
        self.income_list = []

    def save_to_csv(self):
        data_pair = [(self.income_list, 'income.csv'), (self.expense_list, 'expense.csv')]

        for data, file_path in data_pair:
            if data:
                file_path_exists = os.path.exists(file_path)
                # Open the CSV file in append mode
                with open(file_path, mode='a', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    if not file_path_exists:
                        writer.writeheader()
                    writer.writerows(data)
                print(f"Data appended to the CSV file '{file_path}' successfully.")
            else:
                print(f"No data to append in '{file_path}'.")
            
            data.clear()

    def add_income(self, data : dict):
        return self.income_list.append(data)

    def add_expense(self, data : dict):
        return self.expense_list.append(data)   
        
    def show_income_records(self):
        return self.income_list
    
    def show_expense_records(self):
        return self.expense_list
