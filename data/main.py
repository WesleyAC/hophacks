from datetime import datetime

class RawData:
    """
    Data including both CGM datapoings and boluses
    """
    def __init__(self):
        self.data = []

class AvgData:
    """
    Data about an "average" 24-hour period, including standard deviations
    """
    def __init__(self):
        self.data = []

class PumpSettings:
    """
    Data about pump settings:

    * Basel
    * Bolus
      * Correction
      * Carbs
    """

    def __init__(self, tidepool_data):
        """
        Takes tidepool_data as a python object representing a tidepool
        pumpSettings event.
        """
        assert tidepool_data["type"] == "pumpSettings"
        self.basel = tidepool_data["basalSchedules"][tidepool_data["activeSchedule"]]
        self.bolus_carbs = tidepool_data["basalSchedules"][tidepool_data["activeSchedule"]]
        self.bolus_correction = tidepool_data["insulinSensitivities"][tidepool_data["activeSchedule"]]

    @classmethod
    def from_all_data(cls, data):
        """
        Takes all tidepool data as a python object and returns a PumpSettings
        object that represents the most recent active profile.
        """
        settings = list(filter(lambda x: x["type"] == "pumpSettings", data))
        # 2017-05-30T21:14:07
        # %Y-%m-%jT%H:%M:%S
        settings.sort(key = lambda x: datetime.strptime(x["deviceTime"], "%Y-%m-%jT%H:%M:%S"))
        return settings[0]
