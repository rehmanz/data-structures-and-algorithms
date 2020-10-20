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
    if record[0] not in phone_numbers_d:
        phone_numbers_d[record[0]] = 1
    if record[1] not in phone_numbers_d:
        phone_numbers_d[record[1]] = 1

for record in texts:
    if record[1] not in phone_numbers_d:
        phone_numbers_d[record[1]] = 1

print("There are %s different telephone numbers in the records."
      %(len(phone_numbers_d)))
