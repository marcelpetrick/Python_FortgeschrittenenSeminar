# Homework: implement Vector

# Plan: Elemente der Datenstrukturen auch in natürlicher Weise nutzen können.
# Natürlich objekt-orientiert.

class Bruch(object):
    def __init__(self, z, n):
        '''
        :param z: Zähler
        :param n: Nenner
        '''
        self.z = z
        self.n = n

    def __mul__(self, other):
        return 42

a = Bruch(3, 4) # zum Anlegen muss man leider dann auch diese Notation benutzen; für die Initialisierung
b = Bruch(1, 8)
c = a * b # multiplikation jetzt als einfachste Funktion
print(c)