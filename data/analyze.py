from datetime import time, datetime, timedelta
import json
from data.main import RawData, AvgData, PumpSettings

demodata = json.loads(open("data/data_download.json").read())
rawdata = RawData(demodata)

demo_data_a = AvgData(rawdata, datetime(2017, 1, 31, 22, 58, 3), timedelta(7))
# demo_data_b = AvgData(rawdata, datetime(2017, 1, 23, 22, 58, 3), timedelta(30))
# demo_data_c = AvgData(rawdata, datetime(2016, 1, 18, 10, 47, 6), timedelta(7))

def problem_to_text(problem):
    """
    Takes in a problem tuple and returns a tuple of the problem and solution
    that should be shown to the user.
    """
    if problem[0] == "HighBg":
        #TODO(Wesley) stop giving bad advice
        return ("Your blood sugar is often high in the {}.".format(problem[1]),
                "Try increasing your {} basel insulin.".format(problem[1]))
    elif problem[0] == "LowBg":
        #TODO(Wesley) stop giving bad advice
        return ("Your blood sugar is often low in the {}.".format(problem[1]),
                "Try decreasing your {} basel insulin.".format(problem[1]))
    elif problem[0] == "BedtimeBg":
        return ("Your blood sugar is often high before bedtime.",
                "Try setting a reminder to give a correction bolus before you go to bed.")
    elif problem[0] == "MorningBg":
        return ("Your blood sugar is often high in the morning.",
                "Try increasing your nightime basel insulin.")

def get_problems(avg_data):
    problems = []
    high = time_high(avg_data)
    low = time_low(avg_data)
    bedtime = bedtime_bg(avg_data)
    morning = morning_bg(avg_data)
    if high is not None:
        problems.append(("HighBg", time_to_fuzzy(high)))
    if low is not None:
        problems.append(("LowBg", time_to_fuzzy(low)))
    if bedtime:
        problems.append(("BedtimeBg",))
    elif morning:
        problems.append(("MorningBg",))
    return problems

def get_schedule(data):
    return PumpSettings.from_all_data(data.raw.tidepool)

def get_new_schedule(data):
    old_schedule = get_schedule(data)
    for problem in get_problems(data):
        if problem[0] == "HighBg":
            old_schedule.increment_basel_block(problem[1], 0.25)
        if problem[0] == "LowBg":
            old_schedule.increment_basel_block(problem[1], -0.25)
        if problem[0] == "MorningBg":
            old_schedule.increment_basel_block("night", 0.25)
    return old_schedule # Not what it sounds like...

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
        return high_point[0]
    else:
        return None

def time_low(avg_data):
    """
    Finds the most common time of day that the user has a low bg
    """
    low_point = min(slice_to_daytime(avg_data.avgs).items(), key=lambda x: x[1])
    if low_point[1] < 70:
        return low_point[0]
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
