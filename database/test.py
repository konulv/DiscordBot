from config import Config, ConfigError

try:
    a = Config(12021, 20, "utc")
    print(a)
except ConfigError as e:
    msg = str(e).split(",")
    for i in msg:
        print(i)

# import pytz
# print([x.lower() for x in pytz.common_timezones].index("us/pacific"))


# class foo:
#     a = "bar"
#
#     def __init__(self):
#         print(foo.a)
#
# b = foo()