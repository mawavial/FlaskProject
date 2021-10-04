

class TripLog():
    """Represents a trip log """
    def __init__(self, location, temperature, humidity, timestamp, status):
        self.localtion = location
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = timestamp
        self.status = status

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init
