import sqlite3
import pytz

ALL_TIME_ZONES = [x.lower() for x in pytz.common_timezones]

conn = sqlite3.connect("database.db")
c = conn.cursor()

# c.execute("insert into config(ChannelID, Reminder, TimeZone) values (123132, 20, 'UTC')")
# conn.commit()
#
# print(c.execute("SELECT * FROM config WHERE ConfigID == 10").fetchone())

def addConfig(channelID, reminder, timeZone):
    #TODO add a check, only 1 config per channel
    errors = ""
    try:
        temp = int(reminder)
    except ValueError:
        errors += f"reminder '{reminder}' must be a number,"

    if not(timeZone.lower() in ALL_TIME_ZONES):
        errors += f"TimeZone '{timeZone}' not found"

    if len(errors) != 0:
        raise ConfigError(errors)

    c.execute("INSERT into config(ChannelID, Reminder, TimeZone) values (:channelID, :reminder, :timeZone)",
              {"channelID": channelID, "reminder": reminder, "timeZone": timeZone})
    conn.commit()


def getConfig(ID):
    data = c.execute("SELECT * FROM config WHERE (:ID) == ConfigID", {"ID": ID}).fetchone()
    if data is None:
        data = c.execute("SELECT * FROM config WHERE (:ID) == ChannelID", {"ID": ID}).fetchone()
    return data


def updateConfig(ConfigID, reminder, timeZone):
    pass


def addEvent(channelID, name, date, mode, repeat, message):
    configID = getConfig(channelID)[1]



# c.execute("""CREATE TABLE config (
#            ConfigID INTEGER PRIMARY KEY,
#            ChannelID INTEGER,
#            Reminder INTEGER,
#            TimeZone TEXT)""")
#
# c.execute("""CREATE TABLE timer (
#            TimerID INTEGER PRIMARY KEY,
#            ConfigID INTEGER,
#            Timer INTEGER,
#            Repeat TEXT,
#            Message TEXT,
#            FOREIGN KEY(ConfigID) REFERENCES config(ConfigID))""")

# c.execute("""CREATE TABLE event (
#            EventID INTEGER PRIMARY KEY,
#            ConfigID INTEGER,
#            Name TEXT,
#            Date TEXT,
#            Mode TEXT,
#            Repeat TEXT,
#            Message TEXT,
#            FOREIGN KEY(ConfigID) REFERENCES config(ConfigID))""")


class ConfigError(Exception):
    pass