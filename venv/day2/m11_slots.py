def ausgabe(**kwargs):
    print(kwargs)

# erzeugt ein Wörterbuch: {'vorname': 'Anna', 'alter': 42}
ausgabe(vorname="Anna", alter=42)

# Jetzt ohne etwas zu benennen alles als Parameter aufnehmen :)
class Sportwagen(object):
    __slots__ = ['marke', 'modell', 'ps'] # kann man auch als Tuple nutzen, also mit (..)
    def __init__(self, **kwargs): # keyword arguments
        for key in kwargs:
            # wie kann man einem Objekt seine Eigenschaften zuweisen? Vielleicht über eine magische Methode?
            self.__setattr__(key, kwargs[key])
            # jetzt hätte man aber noch pobleme, wenn weniger als drei Argumente zum Beispiel übergeben werden
            # Dafür kann man aber auch einmal über __slots__ iterieren und diese dann mit Standardwerten belegen

s = Sportwagen(marke="Lambo", modell="Gallardo", ps=400)
#s.verbrauch = 42 # wäre jetzt ein AttributeError