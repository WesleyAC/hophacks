import json,main,datetime

d = json.loads(open("data_download.json").read())
rd = main.RawData(d)
ad = main.AvgData(rd, datetime.datetime(2017, 1, 31, 22, 58, 3), datetime.timedelta(7))
