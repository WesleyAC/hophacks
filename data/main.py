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
    def __init__(self):
        self.basel = []
        self.bolus_carbs = []
        self.bolus_correction = []
