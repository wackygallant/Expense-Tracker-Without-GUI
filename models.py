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

class Income(BaseEntry):
    def __init__(self, category: str, description: str, amount: float):
        super().__init__(category, description, amount)  # inheritance
        
    def add_income(self):
        income_list.append({
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        })

class Expense(BaseEntry):
    def __init__(self, category: str, description: str, amount: float):
        super().__init__(category, description, amount)  # inheritance

    def add_expense(self):
        expense_list.append({
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        })

class ListParser:
    @staticmethod
    def show_income_records():
        return income_list
    
    @staticmethod
    def show_expense_records():
        return expense_list
    
    @staticmethod
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

            # if income_list:
            #     file_path_exists = os.path.exists('income.csv')
            #     # Ope the CSV file in append mode
            #     with open('income.csv', mode='a', newline='') as file:
            #         writer = csv.DictWriter(file, fieldnames=headers)
            #         if not file_path_exists:
            #             writer.writeheader()
            #         writer.writerows(income_list)
            #     print("List appended to the CSV file successfully.")
            # else:
            #     print("No income data to enter.")



