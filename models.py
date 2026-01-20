from datetime import date
import csv
import os

income_list = []
expense_list = []

class AmountError(Exception):
    pass

class BaseEntry:
    def __init__(self, category : str, description : str, amount : float):
        self.date = date.today().isoformat()
        self.category = category
        self.description = description
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

class Expense(BaseEntry):
    def add_expense(self):
        expense_list.append(self.to_dict())

class Income(BaseEntry):
    def add_income(self):
        income_list.append(self.to_dict())

class EntryRepository:

    def save_to_csv():
        data_pair = [(expense_list, 'expense.csv'), (income_list, 'income.csv')]

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
                print(f"No data to enter in '{file_path}'.")
            
            data.clear()

    @staticmethod
    def show_income_records():
        return income_list
    
    @staticmethod
    def show_expense_records():
        return expense_list
    


