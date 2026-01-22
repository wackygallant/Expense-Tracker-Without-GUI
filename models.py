from datetime import date

from repository import EntryRepository

class AmountError(Exception):
    pass

class BaseEntry:
    def __init__(self, category : str, description : str, amount : float):
        id_field_data = EntryRepository()
        self.id = id_field_data.generate_next_id('re')
        self.date = date.today().isoformat()
        self.category = category
        self.description = description
        self.amount = amount

    def to_dict(self):
        return {
            "id" : self.id,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }