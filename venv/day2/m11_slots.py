def ausgabe(**kwargs):
    print(kwargs)

# erzeugt ein Wörterbuch: {'vorname': 'Anna', 'alter': 42}
ausgabe(vorname="Anna", alter=42)

# Jetzt ohne etwas zu benennen alles als Parameter aufnehmen :)
class Sportwagen(object):
    __slots__ = ['marke', 'modell', 'ps'] # kann man auch als Tuple nutzen, also mit (..)
 #   def __init__(self, **kwargs): # keyword arguments
  #      pass
        #self.marke = marke
        #self.modell = modell
        #self.ps = ps

#s = Sportwagen("Lambo", "Gallardo", 400)
#s.verbrauch = 42
