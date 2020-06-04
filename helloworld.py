# Copyright (C). No permission granted. All mine.
import datetime
import calendar

name = input("Please enter your name: ")

print(f"Hello, {name}!")
print('Have a nice day')

try:
    date_entry = input('Enter your date of birth in dd/mm/yyyy format: ')
    day, month, year  = map(int, date_entry.split('/'))
    dob = datetime.date(year, month,day )
    print(dob)
    i=dob.weekday()
except (ValueError):
    "Did you use the expected format?"

print("You were born on a ", calendar.day_name[i],"!")
