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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
calls_incoming = []
calls_outgoing = []
texts_incoming = []
texts_outgoing = []
telemarketers = []

for record in calls:
    caller = record[0]
    receiver = record[1]

    if caller not in calls_outgoing:
        calls_outgoing.append(caller)
    if receiver not in calls_incoming:
        calls_incoming.append(receiver)

for record in texts:
    sender = record[0]
    receiver = record[1]

    if sender not in texts_outgoing:
        texts_outgoing.append(sender)
    if receiver not in texts_incoming:
        texts_incoming.append(receiver)

for caller in calls_outgoing:
    if (caller not in calls_incoming) and (caller not in texts_outgoing) and (caller not in texts_incoming):
        telemarketers.append(caller)

print("These numbers could be telemarketers: %s" %("\n".join(telemarketers)))