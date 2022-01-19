import time
from datetime import date
import random

def countdown(given_sec):
    counter = (seconds for seconds in range(given_sec, -1, -1))
    return counter

for remaining_seconds in countdown(20):
    print(remaining_seconds)
    time.sleep(1)


def time_machine(given_date: date):
    year = given_date.year
    month = given_date.month
    day = given_date.day
    given_century_first_year = year // 100 * 100 #equal to ceil(year/100) * 100
    given_century_last_year = given_century_first_year + 100
    time_machine_date = date(random.randint(given_century_first_year, given_century_last_year), month, day)
    return time_machine_date

destination = date(1998, 3, 25)
count_cycle = 0
while True:
    count_cycle += 1
    if time_machine(destination) == destination:
        print(f'WINNER MESSAGE {count_cycle}')
        break

def year_decade_date(given_date: date):
    decade_first_year = given_date.year//10 * 10
    decade_last_year = decade_first_year + 10
    for i in range(30):
        arrival_date = time_machine(destination)
        if decade_first_year <= arrival_date.year < decade_last_year: #последний год на самом деле предпоследний перед концом декады
            yield arrival_date

dates_in_decade = year_decade_date(destination)
# dates_in_decade = [next(g) for i in g] #создаем список из дат list_comprehention, а потом выводим по одному
for n in dates_in_decade:
    print(n)


