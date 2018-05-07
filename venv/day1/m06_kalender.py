# wir bauen jetzt etwas nach, was fast schon so ähnlich in Date von datetime steckt ..
class Kalender(object):
    # Klasseneigenschaft
    # tuple um die anzahl der tage zu definieren; gehört zu klasse und nicht den objekten selber
    # Februar bekommt in der ersten Version ersteinmal 28 ... wird später korrigiert
    tageProMonat = (-42, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) # first element as placeholder, so that all elements shift by one to the right
    # or replace -42 by None

    # Konstruktormethode (eine spezielle Objektmethode)
    def __init__(self, tag, monat, jahr):
        # @todo Gültigkeitsprüfungen
        # @todo vergleichen mit datetime.date
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    # Objektmethode
    # go to the next day; Aufforderung als Nachricht
    def nextDay(self):
        # todo später schaltjahre berücksichtigen
        self.tag += 1
        if self.tag > Kalender.tageProMonat[self.monat]: # todo Monate haben unterschiedliche Anzahl ..
            self.tag = 1
            self.monat += 1
            if self.monat == 13:
                self.monat = 1
                self.jahr += 1

    # Magische MEthode (spezielle Objektmethode)
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


print("defined months:", len(Kalender.tageProMonat))