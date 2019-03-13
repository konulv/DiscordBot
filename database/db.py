import sqlite3


conn = sqlite3.connect("database.db")
c = conn.cursor()

# c.execute("insert into config(ChannelID, Reminder, TimeZone) values (123132, 20, 'UTC')")
# conn.commit()
#
print(c.execute("SELECT * FROM config WHERE ConfigID == 10").fetchone())
#def addConfig(channelID, reminder, timeZone, configID=None)


def getConfig(ID):
    data = c.execute("SELECT * FROM config WHERE (:ID) == ConfigID", {"ID": ID}).fetchone()
    if len(data) == 0:
        return None
    return data

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
