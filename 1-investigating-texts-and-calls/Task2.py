"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone_numbers_d = {}

for record in calls:
    number = record[0]
    date_time = record[2]
    time_secs = record[3]
    if number not in phone_numbers_d:
        phone_numbers_d[number] = time_secs
    else:
        phone_numbers_d[number] += time_secs

max_record_t = ()
for number in phone_numbers_d:
    number = record[0]
    date_time = record[2]
    time_secs = record[3]
    if not max_record_t:
       max_record_t = (time_secs, number, date_time)
    elif time_secs > max_record_t[0]:
        max_record_t = (time_secs, number, date_time)

print("%s spent the longest time, %s seconds, on the phone during %s"
      %(max_record_t[1], max_record_t[0], max_record_t[2]))