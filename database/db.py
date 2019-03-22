import sqlite3
import pytz
from datetime import datetime, timedelta
from event import Event

ALL_TIME_ZONES = [x.lower() for x in pytz.common_timezones]

conn = sqlite3.connect("database.db")
c = conn.cursor()
## delete later
# c.execute("insert into config(ChannelID, Reminder, TimeZone) values (123132, 20, 'UTC')")
# conn.commit()
#
# print(c.execute("SELECT * FROM config WHERE ConfigID == 10").fetchone())


def addConfig(channelID, reminder, timeZone):

    check = c.execute("SELECT * FROM config WHERE (:ID) == ChannelID", {"ID": channelID})
    if check is not None:
        raise ConfigError("This channel already has config set up")

    errors = ""
    try:
        temp = int(reminder)
    except ValueError:
        errors += f"reminder '{reminder}' must be a number,"

    if not(timeZone.lower() in ALL_TIME_ZONES):
        errors += f"TimeZone '{timeZone}' not found"
    else:
        # in case time zone is valid but cases are wrong, e.g. UtC but i need UTC
        timeZone = pytz.common_timezones[ALL_TIME_ZONES.index(timeZone.lower())]

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


def addEvent(channelID, name, date, time, message="1", repeat=False, mode="D"):
    errors = ""
    try:
        configID = getConfig(channelID)[0]
    except TypeError:
        raise EventError("Config hasn't been set up on this channel")

    try:
        datetime.strptime(date, "%d/%m/%y")
    except ValueError:
        errors += f"Date '{date}' is invalid, check if its in a correct format DD/MM/YY"

    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        errors += f"Date '{time}' is invalid, check if its in a correct format HH:MM"

    c.execute("INSERT into event(configID, Name, Date, Time, Message, Repeat, Mode) "
              "values (:configID, :Name, :Date, :Time, :Message, :Repeat, :Mode)",
              {"channelID": configID, "Name": name, "Date": date, "Time": time,
               "Mode": mode, "Repeat": repeat, "Message": message})
    conn.commit()


def getChannelEvents(ID):
    data = c.execute("SELECT * FROM event where ")


def _updateEvent(ID, date):
    pass


def updateEvent(ID, name, date, time, msg, repeat, mode):
    pass


def getEvent(ID):
    eventData = c.execute("SELECT * FROM event WHERE (:ID) == EventID", {"ID": ID}).fetchone()
    channelID = c.execute("SELECT ChannelID FROM config WHERE (:ID) == ConfigID", {"ID": eventData[1]}).fetchone()
    event = Event(channelID, eventData[2], eventData[5])
    return event

# c.execute("""CREATE TABLE config (
#            ConfigID INTEGER PRIMARY KEY AUTOINCREMENT,
#            ChannelID INTEGER,
#            Reminder INTEGER,
#            TimeZone TEXT)""")
#
# c.execute("""CREATE TABLE timer (
#            TimerID INTEGER PRIMARY KEY AUTOINCREMENT,
#            ConfigID INTEGER,
#            Timer INTEGER,
#            Repeat TEXT,
#            Message TEXT,
#            FOREIGN KEY(ConfigID) REFERENCES config(ConfigID))""")

# c.execute("""CREATE TABLE event (
#            EventID INTEGER PRIMARY KEY AUTOINCREMENT,
#            ConfigID INTEGER,
#            Name TEXT,
#            Date TEXT,
#            Time TEXT,
#            Message TEXT,
#            Repeat TEXT,
#            Mode TEXT,
#            FOREIGN KEY(ConfigID) REFERENCES config(ConfigID))""")


class ConfigError(Exception):
    pass

class EventError(Exception):
    pass