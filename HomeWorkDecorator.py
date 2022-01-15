
from datetime import datetime



first_name = input('Enter your First Name here: ')
surname = input('Enter your Surname here: ')
raw_data1 = input('Enter the date the vacation begins in the format "YYYY,MM,DD": ')
data_list1 = (raw_data1.split(','))
data1 = [int(item) for item in data_list1]
from_date = datetime(data1[0], data1[1], data1[2])
raw_data2 = input('Enter the end date of the vacation in the format "YYYY,MM,DD": ')
data_list2 = (raw_data2.split(','))
data2 = [int(item) for item in data_list2]
to_date = datetime(data2[0], data2[1], data2[2])
select_vocation_type = input('Select the type of your vacation from the following: '
                             '\nvocation\nsick leave\nday off\n')


def vocation_request_builder(func):
    def wrapper(*args, **kwargs):
        title = ("CEO Red Bull Inc.\nMr. John Bigbull")
        return title + func(*args, **kwargs)
    return wrapper

@vocation_request_builder
def request_example(first_name, surname, from_date,to_date, select_vocation_type):
    return (f"Hi John,\nI need the paid {select_vocation_type} from {from_date.strftime('%d %b %Y')} to {to_date.strftime('%d %b %Y')}.\n"
          f"{first_name} {surname}")

print (request_example(first_name, surname, from_date, to_date, select_vocation_type))
