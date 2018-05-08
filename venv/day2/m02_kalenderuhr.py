# Inheritance: reuse classes; create hierarchies
# Multi-Inheritance is possible in Python

# from day2.m01_uhr import Clock
import day2.m01_uhr as uhr  # works and assigns as "uhr"
from day1.m06_kalender import Kalender

class Kalenderuhr(Kalender, uhr.Clock):
    def __init__(self, tag, monat, jahr, hour, minute, second):
        Kalender.__init__(self, tag, monat, jahr)
        uhr.Clock.__init__(self, hour, minute, second)

    def __repr__(self):
        #return "%02i.%02i.%04i - %02i:%02i:%02i" % (self.jahr, self.monat, self.tag, self.hour, self.minute, self.second)
        return Kalender.__repr__(self) + " - " + uhr.Clock.__repr__(self)

    # override method from the clock
    def nextSecond(self):
        super().nextSecond() # call from the method "above"; if there are several super-classes with same method, then take from the first fitting
        #super(Kalenderuhr, self).nextSecond() # also possible: determine the super-class of Kalenderuhr
        # overflow if next day is reached :)
        if (0,0,0) == (self.hour, self.minute, self.second):
            super().nextDay()

# ---------------- main block ----------------

# cc for calender-clock
cc = Kalenderuhr(31, 12, 1999, 23, 59, 59)
for t in range(10000000):
    print(cc)
    cc.nextSecond() # calls our method
