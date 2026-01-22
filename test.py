import csv


with open('expense.csv', mode='r') as f:
    reader = list(csv.DictReader(f))
    print(type(reader))
    print(reader[-1]['id'])