import pytz
import db
from typing import TYPE_CHECKING


class Config:
    ALL_TIME_ZONES = [x.lower() for x in pytz.common_timezones]

    def __init__(self, channelID, reminder, timeZone, configID=None):
        self._errors = ""
        self.channelID = channelID
        self.reminder = reminder
        self.timeZone = timeZone
        self.configID = configID

        self.checkErrors()


    @property
    def channelID(self):
        return self._channelID

    @channelID.setter
    def channelID(self, channelID):
        try:
            temp = int(channelID)
        except ValueError:
            self._errors += "Channel ID must be a number,"
            self._channelID = 0
            return
        self._channelID = channelID


    @property
    def reminder(self):
        return self._reminder

    @reminder.setter
    def reminder(self, reminder):
        try:
            temp = int(reminder)
        except ValueError:
            self._errors += "reminder must be a number," #potentially change
            self._reminder = 0
            return
        self._reminder = reminder


    @property
    def timeZone(self):
        return self._timeZone

    @timeZone.setter
    def timeZone(self, timeZone):
        if timeZone.lower() in Config.ALL_TIME_ZONES:
            self._timeZone = timeZone
        else:
            self._errors += "TimeZone not found,"
            self._timeZone = 0



    @property
    def configID(self):
        return self._configID

    @configID.setter
    def configID(self, configID):
        if configID != None:
            if db.getConfig(configID) != None:
                self._configID = configID
            else:
                self._errors += "wrong config ID"
                self._configID = 0
                return
        self._configID = configID

    def checkErrors(self):
        if len(self._errors) == 0:
            return
        else:
            raise ConfigError(self._errors)


class ConfigError(Exception):
    pass
