# Data notes

## Useful links

http://support.tidepool.org/article/37-export-your-account-data

## Event types:

{'basal', 'wizard', 'deviceEvent', 'cgmSettings', 'pumpSettings', 'cbg', 'smbg', 'bolus', 'upload'}

Events we care about:

* cbg
* pumpSettings
* wizard/bolus

### `pumpSettings` event

```json
{'activeSchedule': 'Profile',
 'basalSchedules': {'Profile': [{'rate': 0.9, 'start': 0},
                                {'rate': 1, 'start': 10800000},
                                {'rate': 1, 'start': 21600000},
                                {'rate': 1, 'start': 36000000},
                                {'rate': 1, 'start': 54000000},
                                {'rate': 1.1, 'start': 68400000},
                                {'rate': 1.1, 'start': 75600000}]},
 'bgTargets': {'Profile': [{'start': 0, 'target': 6.66089758925464},
                           {'start': 10800000, 'target': 6.66089758925464},
                           {'start': 21600000, 'target': 6.66089758925464},
                           {'start': 36000000, 'target': 6.66089758925464},
                           {'start': 54000000, 'target': 6.66089758925464},
                           {'start': 68400000, 'target': 6.66089758925464},
                           {'start': 75600000, 'target': 6.66089758925464}]},
 'carbRatios': {'Profile': [{'amount': 9, 'start': 0},
                            {'amount': 9, 'start': 10800000},
                            {'amount': 7, 'start': 21600000},
                            {'amount': 9, 'start': 36000000},
                            {'amount': 7.8, 'start': 54000000},
                            {'amount': 7.8, 'start': 68400000},
                            {'amount': 8, 'start': 75600000}]},
 'conversionOffset': 0,
 'deviceId': 'tandem1000096526966',
 'deviceTime': '2017-05-30T21:14:07',
 'guid': '5a42d936-041e-449b-8585-314409d709f8',
 'id': 'ln4mjbfj5iigjm23drh0packk0bokbhb',
 'insulinSensitivities': {'Profile': [{'amount': 0.7771047187463747,
                                       'start': 0},
                                      {'amount': 0.7771047187463747,
                                       'start': 10800000},
                                      {'amount': 0.7771047187463747,
                                       'start': 21600000},
                                      {'amount': 0.7771047187463747,
                                       'start': 36000000},
                                      {'amount': 0.7771047187463747,
                                       'start': 54000000},
                                      {'amount': 0.7771047187463747,
                                       'start': 68400000},
                                      {'amount': 0.7771047187463747,
                                       'start': 75600000}]},
 'time': '2017-05-31T04:14:07.000Z',
 'timezoneOffset': -420,
 'type': 'pumpSettings',
 'units': {'bg': 'mg/dL', 'carb': 'grams'},
 'uploadId': 'upid_1ff199879a24'}
```

### `cbg` event

```json
{'clockDriftOffset': 0,
 'conversionOffset': 0,
 'deviceId': 'DexG5MobRec_SM53102993',
 'deviceTime': '2016-05-27T19:51:26',
 'guid': '6d20e6ec-0461-41e4-8fbf-5bf8877c3733',
 'id': '8i0vq5uvnq15ilghn9lvnpskvieh4a06',
 'payload': {'internalTime': '2016-05-28T01:51:51',
             'logIndices': [233632311],
             'noiseMode': 'Clean',
             'transmitterTimeSeconds': 7152383,
             'trend': 'Flat'},
 'time': '2016-05-28T02:51:26.000Z',
 'timezoneOffset': -420,
 'type': 'cbg',
 'units': 'mmol/L',
 'uploadId': 'upid_0a01becd798a',
 'value': 9.214241665135585}
```

### `wizard` event 

```json
{'bgInput': 0,
 'bgTarget': {'target': 6.66089758925464},
 'bolus': 'hro3hfk99c6a8uafarbunfo1n7ci71i9',
 'carbInput': 30,
 'clockDriftOffset': 0,
 'conversionOffset': 0,
 'deviceId': 'tandem1000096526966',
 'deviceTime': '2017-05-30T19:59:49',
 'guid': '8038b4db-09f8-4e7f-a304-1c38f4fb0f3e',
 'id': 'dd1vqgpe1b3muoio5s72e45puji3l2dd',
 'insulinCarbRatio': 7.8,
 'insulinOnBoard': 3.65,
 'insulinSensitivity': 0.7771047187463747,
 'payload': {'logIndices': [18882]},
 'recommended': {'carb': 3.85, 'correction': 0, 'net': 3.85},
 'time': '2017-05-31T02:59:49.000Z',
 'timezoneOffset': -420,
 'type': 'wizard',
 'units': 'mmol/L',
 'uploadId': 'upid_1ff199879a24'}
```

### `bolus` event

```json
{'clockDriftOffset': 0,
 'conversionOffset': 0,
 'deviceId': 'tandem1000096526966',
 'deviceTime': '2017-05-30T19:59:49',
 'guid': '6f230593-b03a-48ec-8222-1c3157a4d4a4',
 'id': 'hro3hfk99c6a8uafarbunfo1n7ci71i9',
 'normal': 3.85,
 'payload': {'logIndices': [18882]},
 'subType': 'normal',
 'time': '2017-05-31T02:59:49.000Z',
 'timezoneOffset': -420,
 'type': 'bolus',
 'uploadId': 'upid_1ff199879a24'}
```
