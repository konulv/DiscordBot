
class Config:
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
        return self._reminder

    @timeZone.setter
    def timeZone(self, timeZone):
        try:
            temp = int(timeZone)
        except ValueError:
            self._errors += "TimeZone not found," #fiugre out how to do this
            self._timeZone = 0
            return
        self._timeZone = timeZone


    @property
    def configID(self):
        return self._configID

    @configID.setter
    def configID(self, configID):
        try:
            if configID != None:
                temp = int(configID)
        except ValueError:
            self._errors += "wrong config ID" #wont work
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
