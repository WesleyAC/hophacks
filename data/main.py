from datetime import datetime, time
from collections import OrderedDict

def mmol_to_mgdl(x):
    return x*18

class RawData:
    """
    Data including both CGM datapoints and boluses
    """
    def __init__(self, tidepool_data):
        """
        takes tidepool_data as a python object containing all tidepool data

        only does cgm data right now
        """
        self.tidepool = tidepool_data
        self.data = []
        cgm_data = list(filter(lambda x: x["type"] == "cbg", tidepool_data))
        cgm_data.sort(key = lambda x: datetime.strptime(x["deviceTime"], "%Y-%m-%dT%H:%M:%S"))

        for datapoint in cgm_data:
            timestamp = datetime.strptime(datapoint["deviceTime"], "%Y-%m-%dT%H:%M:%S")
            #TODO(Wesley) check for unit
            self.data.append((timestamp, mmol_to_mgdl(datapoint["value"])))

        self.data.sort()

        self.insulin = []

        insulin_data = list(filter(lambda x: x["type"] == "bolus", tidepool_data))
        insulin_data.sort(key = lambda x: datetime.strptime(x["deviceTime"], "%Y-%m-%dT%H:%M:%S"))
        for datapoint in insulin_data:
            timestamp = datetime.strptime(datapoint["deviceTime"], "%Y-%m-%dT%H:%M:%S")
            self.insulin.append((timestamp, datapoint["normal"]))

class AvgData:
    """
    Data about an "average" 24-hour period, including standard deviations
    """
    def __init__(self, raw_data, end_time, time_period, moving_avg=50):
        """
        Takes a RawData object and averages it over dtime
        """
        self.raw = raw_data

        self.datamap = OrderedDict() # Maps time -> list(data point)
        data = filter(lambda x: x[0] > end_time - time_period, raw_data.data)
        for point in data:
            point_time = time(point[0].hour, point[0].minute)
            if point_time not in self.datamap:
                self.datamap[point_time] = []
            self.datamap[point_time].append(point[1])

        self.avgs_list = []
        for i, point in enumerate(self.datamap.values()):
            avg = 0
            for moving_idx in range(i-moving_avg, i+moving_avg+1):
                iv = list(self.datamap.values())[moving_idx % len(self.datamap)]
                avg_at_idx = sum(iv)/len(iv)
                avg += avg_at_idx
            avg /= moving_avg*2 + 1
            self.avgs_list.append(avg)

        self.avgs = {list(self.datamap.keys())[i]: v for (i, v) in enumerate(self.avgs_list)}

    def fudge(self, amount, skew=0):
        self.avgs_list = list(map(lambda x: x[1] + amount + x[0]*skew, enumerate(self.avgs_list)))
        self.avgs = {list(self.datamap.keys())[i]: v for (i, v) in enumerate(self.avgs_list)}


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
        self.basel = [{"start": i["start"]/(1000*60*60), "rate": i["rate"]} for i in tidepool_data["basalSchedules"][tidepool_data["activeSchedule"]]]
        self.bolus_carbs = [{"start": i["start"]/(1000*60*60), "amount": i["amount"]} for i in tidepool_data["carbRatio"]]
        self.bolus_correction = [{"start": i["start"]/(1000*60*60), "amount": i["amount"]} for i in tidepool_data["insulinSensitivity"]]

    def increment_basel_block(self, timeofday, amount):
        for block in self.basel:
            if timeofday == "morning":
                if block["start"] >= 7 and block["start"] < 11:
                    block["rate"] += amount
            elif timeofday == "afternoon":
                if block["start"] >= 11 and block["start"] < 18:
                    block["rate"] += amount
            elif timeofday == "evening":
                if block["start"] >= 18 and block["start"] < 20:
                    block["rate"] += amount
            elif timeofday == "night":
                if block["start"] >= 20 or block["start"] < 7:
                    block["rate"] += amount

    def increment_bolus_carbs_block(self, timeofday, amount):
        for block in self.bolus_carbs:
            if timeofday == "morning":
                if block["start"] >= 7 and block["start"] < 11:
                    block["amount"] += amount
            elif timeofday == "afternoon":
                if block["start"] >= 11 and block["start"] < 18:
                    block["amount"] += amount
            elif timeofday == "evening":
                if block["start"] >= 18 and block["start"] < 20:
                    block["amount"] += amount
            elif timeofday == "night":
                if block["start"] >= 20 or block["start"] < 7:
                    block["amount"] += amount

    def increment_bolus_correction_block(self, timeofday, amount):
        for block in self.bolus_correction:
            if timeofday == "morning":
                if block["start"] >= 7 and block["start"] < 11:
                    block["amount"] += amount
            elif timeofday == "afternoon":
                if block["start"] >= 11 and block["start"] < 18:
                    block["amount"] += amount
            elif timeofday == "evening":
                if block["start"] >= 18 and block["start"] < 20:
                    block["amount"] += amount
            elif timeofday == "night":
                if block["start"] >= 20 or block["start"] < 7:
                    block["amount"] += amount

    @classmethod
    def from_all_data(cls, data):
        """
        Takes all tidepool data as a python object and returns a PumpSettings
        object that represents the most recent active profile.
        """
        settings = list(filter(lambda x: x["type"] == "pumpSettings", data))
        settings.sort(key = lambda x: datetime.strptime(x["deviceTime"], "%Y-%m-%dT%H:%M:%S"))

        return cls(settings[0])
