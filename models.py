from datetime import date

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

# Just passes the income instances to the repository
class Income(BaseEntry):
    pass

# Just passes the expenses instances to the repository
class Expense(BaseEntry):
    pass