from data.main import RawData, AvgData
from datetime import time, datetime, timedelta
import requests

def tidepool_import(username, passwd):
    #TODO(Wesley) deal with wrong passwd/errors
    r = requests.post('https://api.tidepool.org/auth/login', auth=(username, passwd))
    user_id = r.json()["userid"]
    tidepool_session = r.headers["x-tidepool-session-token"]
    headers = {
        "x-tidepool-session-token": tidepool_session,
        "Content-Type": "application/json"
    }
    r = requests.get('https://api.tidepool.org/data/{}'.format(user_id), headers=headers)
    #TODO(Wesley) fix hardcoded date
    return AvgData(RawData(r.json()), datetime(2017, 5, 29, 0, 0, 0), timedelta(1))
