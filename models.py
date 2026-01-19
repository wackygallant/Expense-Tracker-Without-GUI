from datetime import date
import csv
import os

income_list = []
expense_list = []
headers = ['date', 'category', 'description', 'amount']

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
        super().__init__(category, description, amount)  # ✅ inheritance
        
    def add_income(self):
        income_list.append({
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        })

class Expense(BaseEntry):
    def __init__(self, category: str, description: str, amount: float):
        super().__init__(category, description, amount)  # ✅ inheritance

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
        if expense_list:
            # Open the CSV file in append mode
            with open('expense.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerows(expense_list)
            print("List appended to the CSV file successfully.")
        else:
            print("No expenses data to enter")

        if income_list:
            with open('income.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerows(income_list)
            print("List appended to the CSV file successfully.")
        else:
            print("No income data to enter.")
