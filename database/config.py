
class Config:
    def __init__(self, channelID, reminder, timeZone, configID=None):
        self.errors = []
        self._channelID = channelID
        self._reminder = reminder
        self._timeZone = timeZone
        self._configID = configID

    @property
    def channelID(self):
        return self._channelID

    @channelID.setter
    def channelID(self, channelID):
        try:
            temp = int(channelID)
        except ValueError:
            self.errors.append(1)
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
            self.errors.append(2)
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
            self.errors.append(3)
            self._timeZone = 0
            return
        self._timeZone = timeZone


    @property
    def configID(self):
        return self._configID

    @configID.setter
    def configID(self, configID):
        try:
            temp = int(configID)
        except ValueError:
            self.errors.append(4)
            self._configID = 0
            return
        self._configID = configID

