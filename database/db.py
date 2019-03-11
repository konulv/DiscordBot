import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
# c.execute("""CREATE TABLE config (
#            ConfigID INTEGER PRIMARY KEY,
#            ChannelID INTEGER,
#            Reminder INTEGER
#            TimeZone TEXT)""")

#c.execute("""CREATE TABLE timer (
#            TimerID INTEGER PRIMARY KEY,
#            ConfigID INTEGER,
#            Timer INTEGER,
#            Repeat TEXT,
#            Message TEXT,
#            FOREIGN KEY(ConfigID) REFERENCES config(ConfigID))""")

#c.execute("""CREATE TABLE event (
#            EventID INTEGER PRIMARY KEY,
#            ChannelID INTEGER,
#            Name TEXT,
#            Date TEXT,
#            Mode TEXT,
#            Repeat TEXT,
#            Message TEXT,
#            FOREIGN KEY(ConfigID) REFERENCES config(ConfigID))""")
