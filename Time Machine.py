from datetime import date

date(year_int, month_int, day_int)
first_year = 1832 // 100 * 100
last_year = first_year + 100
year_given_by_time_machine = random.randint(first_year, last_year)
• Year – date_obj.year
• Month – date_obj.month
• Day – date_obj.day
# Generator comprehention
data1 = (int(item) for item in data_list1)

# while True:
#     pass
# If you get the time_machine  result
# # with the desired year, just break the loop and print the WINNER MESSAGE 
# 30 вариантов дат, но напечатайте
# yield только те даты, которые относятся к желаемому десятилетию.