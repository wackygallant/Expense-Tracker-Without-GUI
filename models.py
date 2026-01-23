from datetime import date

from repository import EntryRepository

class AmountError(Exception):
    pass

class BaseEntry:
    def __init__(self, category, description, amount : float, record_type):
        id_field_data = EntryRepository()
        self.id = id_field_data.generate_next_id()
        self.date = date.today().isoformat()
        self.category = category
        self.description = description
        self.amount = amount
        self.record_type = record_type

    def to_dict(self):
        return {
            "id" : self.id,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount,
            "record_type" : self.record_type
        }