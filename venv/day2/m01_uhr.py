class Clock(object):
    # ctor
    def __init__(self, hour, minute, second): # just for testing: unused params will not be reported as warning (already fixed)
        # todo: add checks for the ranges
        self.hour = hour
        self.minute = minute
        self.second = second

    # regular methods
    def nextSecond(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1

        if self.minute >= 60:
            self.minute = 0
            self.hour += 1

        if self.hour >= 24:
            self.hour = 0

    # representation
    def __repr__(self):
        return "%02i.%02i.%02i" % (self.hour, self.minute, self.second)

clock = Clock(23,59,58)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for t in range(100):
    print(clock)
    clock.nextSecond()
