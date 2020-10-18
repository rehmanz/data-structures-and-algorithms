"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_numbers_d = {}
for record in calls:
    number = record[0]
    if number not in phone_numbers_d:
        phone_numbers_d[number] = 1

for record in texts:
    number = record[0]
    if number not in phone_numbers_d:
        phone_numbers_d[number] = 1

print("There are %s different telephone numbers in the records."
      %(len(phone_numbers_d)))
