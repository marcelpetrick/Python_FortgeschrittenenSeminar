# Slots?!?

class Sportwagen(object):
    # Hierüber gibt man die Schlüssel an, die für das Wörterbuch zulässig wären.
    # Also für dieses Klasse!
    __slots__ = ['marke', 'modell', 'ps'] # kann man auch als Tuple nutzen, also mit (..)
    def __init__(self, marke, modell, ps):
        self.marke = marke
        self.modell = modell
        self.ps = ps

s = Sportwagen("Lambo", "Gallardo", 400)
s.verbrauch = 42 # jetzt hätte man eine Eigenschaft verbrauch. Und das wollen wir verhindern! This fails now with AttributeError due to _slots__! :)
s.marke = "Klaus"