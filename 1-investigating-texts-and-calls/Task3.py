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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def isBangaloreCaller(number):
    if number[0:4] == "(080":
        return True
    # elif number[0] == "7" or number[0] == "8" or number[0] == "9":
    #     return True

def isBangaloreCallee(number):
    if number == "7" or number == "8" or number == "9":
        return True

def isBangaloreCallerFromFixedLine(number):
    if number[0:4] == "(080":
        return True

##
# Part A
##
codes_l = []
for record in calls:
    caller_number = record[0]
    called_number = record[1]
    if isBangaloreCaller(caller_number):
        if isBangaloreCaller(called_number):
            if called_number not in codes_l:
                codes_l.append(called_number)

print("The numbers called by people in Bangalore have codes: %s" %"\n".join(sorted(codes_l)))


##
# Part B
##
local_calls_counter = 0
bangalore_calls_counter = 0
for record in calls:
    caller_number = record[0]
    called_number = record[1]
    if isBangaloreCallerFromFixedLine(caller_number) and isBangaloreCallerFromFixedLine(called_number):
        local_calls_counter += 1
    if isBangaloreCaller(caller_number):
        bangalore_calls_counter += 1
print("%s percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      %(round(100 * local_calls_counter/bangalore_calls_counter, 2)))
