import datetime
from datetime import date

def takeInput():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))

date1 = date(takeInput())
date2 = date(takeInput())

day_difference = date1 - date2
print(day_difference)


