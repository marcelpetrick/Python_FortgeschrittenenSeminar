def ausgabe(**kwargs):
    print(kwargs)

# erzeugt ein Wörterbuch: {'vorname': 'Anna', 'alter': 42}
ausgabe(vorname="Anna", alter=42)

# Jetzt ohne etwas zu benennen alles als Parameter aufnehmen :)
class Sportwagen(object):
    __slots__ = ['__marke', '__modell', '__ps'] # kann man auch als Tuple nutzen, also mit (..)
    def __init__(self, **kwargs): # keyword arguments
        for key in kwargs:
            # wie kann man einem Objekt seine Eigenschaften zuweisen? Vielleicht über eine magische Methode?
            self.__setattr__(key, kwargs[key])
            # jetzt hätte man aber noch pobleme, wenn weniger als drei Argumente zum Beispiel übergeben werden
            # Dafür kann man aber auch einmal über __slots__ iterieren und diese dann mit Standardwerten belegen

    # property: kann man die nicht vereinfachen?
    ps = property(None, __setPs)
    #ps = property(Sportwagen.generate_getter("ps", self), self.__setPs)

    # new setter
    def __setPs(self, ps):
        if ps >= 0:
            self.__ps = ps
        else:
            raise ValueError

    def __getPs(self):
        return self.__ps # wie kann man das automatisieren, wenn man nur für eine Minderheit der Getter diese Ausgabe braucht?

    @staticmethod
    def generate_getter(name):
        # die neue Funktion wird wahrscheinlich privat sein
        def __get():
            return self.__getattr__(name)

#s = Sportwagen(marke="Lambo", modell="Gallardo", ps=400)
#s.verbrauch = 42 # wäre jetzt ein AttributeError

s = Sportwagen(ps = 400)

# falls man auf keyword-argument setzt, muss man auch properties definieren
# slots sind gut zur Absicherung der vorhandenen Attribute :)

# Morgen: Threads und Synchronisation; Iteratoren/Generatoren
