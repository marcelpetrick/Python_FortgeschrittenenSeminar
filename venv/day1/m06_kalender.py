# wir bauen jetzt etwas nach, was fast schon so ähnlich in Date von datetime steckt ..
class Kalender(object):
    # Klasseneigenschaft
    # Tupel um die Anzahl der Tagezu definieren; gehört zu Klasse und nicht den Objekten selber
    # Februar bekommt in der ersten Version ersteinmal 28 ... wird später korrigiert
    tageProMonat = (-42, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) # first element as placeholder, so that all elements shift by one to the right
    # or replace -42 by None

    # Statische Methode:
    @staticmethod
    def istSchaltjahr(jahr):
        return (jahr % 400 == 0) or (jahr % 100 != 0 and jahr % 4 == 0)

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
        # ternärer Operator
        korrektur = 1 if self.monat == 2 and Kalender.istSchaltjahr(self.jahr) else 0 # nicht mit: frage ? true : false
        if self.tag > Kalender.tageProMonat[self.monat] + korrektur: # todo Februar /Schaltjahre
            self.tag = 1
            self.monat += 1
            if self.monat == 13:
                self.monat = 1
                self.jahr += 1

    # Magische Methode (spezielle Objektmethode)
    def __repr__(self):
        return "%02i.%02i.%04i" % (self.tag, self.monat, self.jahr)

if __name__ == "__main__":  # just run if the current module name is ours ... so that when imported this is not executed
    k = Kalender(31,12,2017)

    print(k)
    k.nextDay()
    print(k)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for t in range(10):
        print(k)
        k.nextDay()


    print("defined months:", len(Kalender.tageProMonat))
