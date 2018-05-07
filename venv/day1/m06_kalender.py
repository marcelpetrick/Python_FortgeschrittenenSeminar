# wir bauen jetzt etwas nach, was fast schon so ähnlich in Date von datetime steckt ..
class Kalender(object):
    def __init__(self, tag, monat, jahr):
        # @todo Gültigkeitsprüfungen
        # @todo vergleichen mit datetime.date
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

k = Kalender(31,12,2017)


