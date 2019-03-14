from config import Config, ConfigError
import db
import pytz
#db.addConfig(1623, 20, "utc")

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