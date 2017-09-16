from datetime import datetime, time

def mmol_to_mgdl(x):
    return x*18

class RawData:
    """
    Data including both CGM datapoings and boluses
    """
    def __init__(self, tidepool_data):
        """
        takes tidepool_data as a python object containing all tidepool data

        only does cgm data right now
        """
        self.data = []
        cgm_data = list(filter(lambda x: x["type"] == "cbg", tidepool_data))
        cgm_data.sort(key = lambda x: datetime.strptime(x["deviceTime"], "%Y-%m-%jT%H:%M:%S"))

        for datapoint in cgm_data:
            timestamp = datetime.strptime(datapoint["deviceTime"], "%Y-%m-%jT%H:%M:%S")
            #TODO(Wesley) check for unit
            self.data.append((timestamp, mmol_to_mgdl(datapoint["value"])))

class AvgData:
    """
    Data about an "average" 24-hour period, including standard deviations
    """
    def __init__(self, raw_data, end_time, time_period):
        """
        Takes a RawData object and averages it over dtime
        """
        self.datamap = {} # Maps time -> list(data point)
        data = filter(lambda x: x[0] > end_time - time_period, raw_data.data)
        for point in data:
            point_time = time(point[0].hour, point[0].minute)
            if point_time not in self.datamap:
                self.datamap[point_time] = []
            self.datamap[point_time].append(point[1])

        self.avgs = {k: sum(v)/len(v) for (k,v) in self.datamap.items()}


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
        print(tidepool_data)
        self.basel = tidepool_data["basalSchedules"][tidepool_data["activeSchedule"]]
        self.bolus_carbs = tidepool_data["carbRatio"]
        self.bolus_correction = tidepool_data["insulinSensitivity"]

    @classmethod
    def from_all_data(cls, data):
        """
        Takes all tidepool data as a python object and returns a PumpSettings
        object that represents the most recent active profile.
        """
        settings = list(filter(lambda x: x["type"] == "pumpSettings", data))
        settings.sort(key = lambda x: datetime.strptime(x["deviceTime"], "%Y-%m-%jT%H:%M:%S"))
        return cls(settings[0])
