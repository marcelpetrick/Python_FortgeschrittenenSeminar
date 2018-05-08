# Vererbung: Wiedernutzung von Klassen; Hierarchien bilden
# Multi-Inheritance in Python möglich

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

# ---------------- main block ----------------

# cc for calender-clock
cc = Kalenderuhr(31, 12, 1999, 23, 59, 59)
for t in range(1000):
    print(cc)
    cc.nextSecond()
