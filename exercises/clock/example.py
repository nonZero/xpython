class Clock:
    def __init__(self, hour, minutes):
        self.hour = (hour + minutes // 60) % 24
        self.minutes = minutes % 60

    def __str__(self):
        return "{:02}:{:02}".format(self.hour, self.minutes)

    def __eq__(self, other):
        return self.hour == other.hour and self.minutes == other.minutes

    def add(self, minutes):
        return Clock(self.hour, self.minutes + minutes)
