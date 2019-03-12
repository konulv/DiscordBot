from config import Config, ConfigError
try:
    a = Config("ab", "a", "as", "acas")
except ConfigError as e:
    msg = str(e).split(",")
    for i in msg:
        print(i)
