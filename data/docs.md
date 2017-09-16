http://support.tidepool.org/article/37-export-your-account-data

Event types:
{'basal', 'wizard', 'deviceEvent', 'cgmSettings', 'pumpSettings', 'cbg', 'smbg', 'bolus', 'upload'}

* Basal

{'clockDriftOffset': 0, 'conversionOffset': 0, 'deliveryType': 'scheduled', 'deviceId': 'Paradigm Revel - 523-=-54787576', 'deviceTime': '2016-06-06T07:00:00', 'duration': 43200000, 'guid': '4aba8cd7-5b82-4615-8383-38a89b368d07', 'id': 'q08a3rm4hom22secai3gu9dg4c82mvo7', 'payload': {'rawSeqNums': [89], 'rawUploadId': 54787576}, 'rate': 1, 'scheduleName': 'standard', 'source': 'carelink', 'time': '2016-06-06T14:00:00.000Z', 'timezoneOffset': -420, 'type': 'basal', 'uploadId': 'upid_09bf58f75f9f'}

* Wizard

This is only for medtronic pumps

{'bgInput': 8.159599546836935, 'bgTarget': {'high': 7.2159723883591935, 'low': 6.1058227901500866}, 'bolus': 'h74oveecen2ob6fst58gahlsq1maf2v0', 'carbInput': 62, 'clockDriftOffset': 0, 'conversionOffset': 0, 'deviceId': 'Paradigm Revel - 523-=-54787576', 'deviceTime': '2016-06-06T14:54:09', 'guid': '66855b31-cee9-4a03-bb8b-a167a6ee6393', 'id': 'nag2hprk0vpt3t6p5v3p5cuk8vu9llf4', 'insulinCarbRatio': 9, 'insulinOnBoard': 0.7, 'insulinSensitivity': 1.3876869977613833, 'payload': {'rawSeqNums': [84], 'rawUploadId': 54787576}, 'recommended': {'carb': 6.8, 'correction': 0.6, 'net': 6.8}, 'source': 'carelink', 'time': '2016-06-06T21:54:09.000Z', 'timezoneOffset': -420, 'type': 'wizard', 'units': 'mmol/L', 'uploadId': 'upid_09bf58f75f9f'}

* Device Event

Not sure what this is

* GGM settings

{'clockDriftOffset': 0, 'conversionOffset': 0, 'deviceId': 'DexG5MobRec_SM53102993', 'deviceTime': '2016-05-14T13:13:43', 'guid': '8ac361dd-b875-4c86-9fe0-d88a79c42174', 'highAlerts': {'enabled': False, 'level': 11.101495982091066, 'snooze': 0}, 'id': 'vdblm4sc6dckcmtrlqa7ncilm4ku5bpt', 'lowAlerts': {'enabled': True, 'level': 4.440598392836427, 'snooze': 0}, 'outOfRangeAlerts': {'enabled': True, 'snooze': 1200000}, 'payload': {'alarmProfile': 'Vibrate', 'internalTime': '2016-05-14T19:14:08', 'language': 'English', 'logIndices': [232485248]}, 'rateOfChangeAlerts': {'fallRate': {'enabled': False, 'rate': -0.16652243973136602}, 'riseRate': {'enabled': False, 'rate': 0.16652243973136602}}, 'time': '2016-05-14T20:13:43.000Z', 'timezoneOffset': -420, 'transmitterId': '404GE4', 'type': 'cgmSettings', 'units': 'mmol/L', 'uploadId': 'upid_0a01becd798a'}

* Pump settings

{'activeSchedule': 'standard', 'basalSchedules': {'pattern a': [], 'pattern b': [], 'standard': [{'rate': 0.9, 'start': 0}, {'rate': 1, 'start': 10800000}, {'rate': 1, 'start': 25200000}, {'rate': 1.1, 'start': 68400000}]}, 'bgTarget': [{'high': 8.3261219865683, 'low': 6.1058227901500866, 'start': 0}, {'high': 7.2159723883591935, 'low': 6.1058227901500866, 'start': 25200000}, {'high': 8.3261219865683, 'low': 6.1058227901500866, 'start': 77400000}], 'carbRatio': [{'amount': 9, 'start': 0}, {'amount': 7, 'start': 21600000}, {'amount': 9, 'start': 36000000}, {'amount': 7.8, 'start': 54000000}, {'amount': 8, 'start': 75600000}], 'clockDriftOffset': 0, 'conversionOffset': 0, 'deviceId': 'Paradigm Revel - 523-=-54787576', 'deviceTime': '2016-06-06T16:14:13', 'guid': 'f3a6b0d4-e485-4de1-b34e-7605ad67ea2b', 'id': '9068c3rrdkbsc4qd8eqgc6ctcplb4j4i', 'insulinSensitivity': [{'amount': 1.3876869977613833, 'start': 0}], 'payload': {'logIndices': [1663]}, 'source': 'carelink', 'time': '2016-06-06T23:14:13.000Z', 'timezoneOffset': -420, 'type': 'pumpSettings', 'units': {'bg': 'mg/dL', 'carb': 'grams'}, 'uploadId': 'upid_f410e7d46800'}

* CBG

{'clockDriftOffset': 0, 'conversionOffset': 0, 'deviceId': 'DexG5MobRec_SM55104900', 'deviceTime': '2016-09-05T20:56:37', 'guid': '62646899-2bfc-444d-a795-dfa06e1a74d7', 'id': 'lkuqjj2kc9s491s2bl1oqt2sqphnu1av', 'payload': {'internalTime': '2016-09-06T04:57:48', 'logIndices': [242369868], 'noiseMode': 'Clean', 'transmitterTimeSeconds': 6588461, 'trend': 'Flat'}, 'time': '2016-09-06T03:56:37.000Z', 'timezoneOffset': -420, 'type': 'cbg', 'units': 'mmol/L', 'uploadId': 'upid_e0959bba007c', 'value': 4.607120832567793}

* SMBG

{'clockDriftOffset': 0, 'conversionOffset': 0, 'deviceId': 'Paradigm Revel - 523-=-54862477', 'deviceTime': '2016-06-07T13:31:35', 'guid': '06a05d35-715c-4c5f-b83e-caf8a87937c1', 'id': 'evluoromfc62iap2h7p99ff6oj3mbu19', 'payload': {'action-requestor': 'paradigm link or b key', 'rawSeqNums': [545], 'rawUploadId': 54862477}, 'source': 'carelink', 'subType': 'linked', 'time': '2016-06-07T20:31:35.000Z', 'timezoneOffset': -420, 'type': 'smbg', 'units': 'mmol/L', 'uploadId': 'upid_f410e7d46800', 'value': 8.437136946389211}

* Bolus

{'clockDriftOffset': 0, 'conversionOffset': 0, 'deviceId': 'Paradigm Revel - 523-=-54787576', 'deviceTime': '2016-06-06T14:54:09', 'guid': '8f82db12-87bb-4ef1-b50a-eafc92c8c415', 'id': 'h74oveecen2ob6fst58gahlsq1maf2v0', 'normal': 6.8, 'payload': {'rawSeqNums': [83], 'rawUploadId': 54787576}, 'source': 'carelink', 'subType': 'normal', 'time': '2016-06-06T21:54:09.000Z', 'timezoneOffset': -420, 'type': 'bolus', 'uploadId': 'upid_09bf58f75f9f'}

* Upload

{'byUser': '33dbe336c6', 'computerTime': '2016-06-06T16:37:45', 'conversionOffset': 0, 'deviceId': 'multiple', 'deviceManufacturers': ['Medtronic'], 'deviceModel': 'Paradigm Revel 523', 'deviceSerialNumber': '710846', 'deviceTags': ['insulin-pump'], 'guid': '1a912122-29d1-461f-aaa4-dc35742a3956', 'id': 'iqntrd002bquq81ee90l2i9ptbalajld', 'payload': {'skippedUploads': []}, 'time': '2016-06-06T23:37:45.000Z', 'timeProcessing': 'utc-bootstrapping', 'timezone': 'US/Pacific', 'timezoneOffset': -420, 'type': 'upload', 'uploadId': 'upid_09bf58f75f9f', 'version': '0.264.0'}
