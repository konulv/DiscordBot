import db
import pytz
#db.addConfig(1623, 20, "utc")
from datetime import datetime, timedelta


# timestr = "23:5"
# datestr = "30/05/19"
# date1str = "30/05/19 23:5"
# date1 = datetime.strptime(date1str, "%d/%m/%y %H:%M")
#
# date2str = "29/05/19 23:5"
# delta = timedelta(1)
# date2 = datetime.strptime(date2str, "%d/%m/%y %H:%M")
# date2 += delta
# print(date1 == date2)
# print(date1)
# print(date2)
#
# with open("db.py", "r") as file:
#     print(file.readlines())


# print(datetime.strptime(timestr, "%H:%M"))
# print(datetime.strptime(datestr, "%d/%m/%y"))
# try:
#     a = Config("abc", "adc", "utc")
#     print(a)
# except ConfigError as e:
#     msg = str(e).split(",")
#     for i in msg:
#         print(i)

# db.addConfig(1235, "5", "PST")
# import pytz
# print([x.lower() for x in pytz.common_timezones].index("us/pacific"))


# class foo:
#     a = "bar"
#
#     def __init__(self):
#         print(foo.a)
#
# b = foo()