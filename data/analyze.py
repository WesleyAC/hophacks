from datetime import time, datetime, timedelta
import json
from data.main import RawData, AvgData

def get_demo_data():
    d = json.loads(open("data/data_download.json").read())
    return AvgData(RawData(d), datetime(2017, 1, 31, 22, 58, 3), timedelta(7))

def get_problems(avg_data):
    problems = []
    high = time_high(avg_data)
    low = time_low(avg_data)
    bedtime = bedtime_bg(avg_data)
    morning = morning_bg(avg_data)
    if high is not None:
        problems.append(("HighBg", high))
    if low is not None:
        problems.append(("LowBg", low))
    if bedtime:
        problems.append(("BedtimeBg",))
    elif morning:
        problems.append(("MorningBg",))
    return problems

def slice_to_daytime(data):
    """
    takes a dict of bg data and returns a dict that only has data from the daytime
    """
    return dict(filter(lambda x: x[0] > time(6) and x[0] < time(22), data.items()))

def time_to_fuzzy(t):
    """
    converts a time object to either "morning", "afternoon", "evening", or "night"
    """
    if t > time(0) and t < time(7):
        return "night"
    elif t > time(7) and t < time(11):
        return "morning"
    elif t > time(11) and t < time(18):
        return "afternoon"
    elif t > time(18) and t < time(23):
        return "evening"
    else:
        return "night"

def time_high(avg_data):
    """
    Finds the most common time of day that the user has a high bg
    """
    high_point = max(slice_to_daytime(avg_data.avgs).items(), key=lambda x: x[1])
    if high_point[1] > 200:
        return time_to_fuzzy(high_point[0])
    else:
        return None

def time_low(avg_data):
    """
    Finds the most common time of day that the user has a low bg
    """
    low_point = min(slice_to_daytime(avg_data.avgs).items(), key=lambda x: x[1])
    if low_point[1] < 70:
        return time_to_fuzzy(low_point[0])
    else:
        return None

def forgot_bolus(avg_data):
    pass

def bedtime_bg(avg_data):
    return avg_data.avgs[time(23, 59)] > 200 # That was easy

def morning_bg(avg_data):
    return not bedtime_bg(avg_data) and avg_data.avgs[time(7,1)] > 200

def forgot_correction(avg_data):
    pass
