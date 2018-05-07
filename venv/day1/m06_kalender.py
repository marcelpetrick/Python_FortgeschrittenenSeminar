# wir bauen jetzt etwas nach, was fast schon so ähnlich in Date von datetime steckt ..
class Kalender(object):
    def __init__(self, tag, monat, jahr):
        # @todo Gültigkeitsprüfungen
        # @todo vergleichen mit datetime.date
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    # go to the next day; Aufforderung als Nachricht
    def nextDay(self):
        # todo später schaltjahre berücksichtigen
        self.tag += 1
        if self.tag == 32: # todo Monate haben unterschiedliche Anzahl ..
            self.tag = 1
            self.monat += 1
            if self.monat == 13:
                self.monat = 1
                self.jahr += 1

    def __repr__(self):
        return "%02i.%02i.%04i" % (self.tag, self.monat, self.jahr)

k = Kalender(31,12,2017)

print(k)
k.nextDay()
print(k)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for t in range(10):
    print(k)
    k.nextDay()
