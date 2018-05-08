class Clock(object):
    # Konstruktormethode (eine spezielle Objektmethode)
    def __init__(self, hour, minute, second): # just for testing if there is some kind of warning in case of not using all params
        self.hour = hour
        self.minute = minute
        self.second = second

    def nextSecond(self):
        self.second += 1
        if self.second > 59:
            self.second = 0
            self.minute += 1

        if self.minute > 59:
            self.minute = 0
            self.hour += 1

        if self.hour > 23:
            self.hour == 0

    # Magische Methode (spezielle Objektmethode)
    def __repr__(self):
        return "%02i.%02i.%02i" % (self.hour, self.minute, self.second)

clock = Clock(23,0,0)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for t in range(1000000):
    print(clock)
    clock.nextSecond()

