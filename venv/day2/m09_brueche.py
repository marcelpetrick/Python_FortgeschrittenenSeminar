# Homework: implement Vector

# Plan: Elemente der Datenstrukturen auch in natürlicher Weise nutzen können.
# Natürlich objekt-orientiert.

class Bruch(object):
    # wir brauchen etwas zum Kuerzen
    #1  wenn b = 0 dann
    #2    Ergebnis = a
    #3  sonst
    #4    Ergebnis = EUCLID(b, Divisionsrest(a durch b))    // siehe Modulo-Funktion
    @staticmethod
    def ggT(a, b):
        if b == 0:
            return a
        else:
            return Bruch.ggT(b, a % b)
    #or: math.gcd(a,b)

    def __init__(self, z, n = 1): # zweiter Wert jetzt mit Default
        '''
        :param z: Zähler
        :param n: Nenner
        '''
        self.z = z
        self.n = n

# Important: Wenn man Operatoren überlädt, dann immer paarig machen, damit man keine Richtung vergisst
    def __mul__(self, other):
        # aleways works when other is a Bruch
        print(type(other))
        if isinstance(other, int): # check for the type of some
            #print("fake it till you make it")
            #other = Bruch(other, 1)
            # or: return self * Bruch(other)
            return Bruch(self.z * other, self.n)
        return Bruch(self.z * other.z, self.n * other.n) # does currently not "Kürzen" todo

    # multiplikations-operation mit rechten operanden; gerade da, wo man die andere Klasse nicht ändern darf - da sonst Vertrag verletzt werden würde
    # einfach umwandeln
    def __rmul__(self, other):
        return self * other # oder: self.__mul__(other)

    def __add__(self, other):
        return Bruch(1,2) #todo

    def __repr__(self):
        return "%i / %i" % (self.z, self.n)

#~~~ some simple examples ~~~
a = Bruch(3, 4) # zum Anlegen muss man leider dann auch diese Notation benutzen; für die Initialisierung
b = Bruch(1, 8)
c = a * b # multiplikation jetzt als einfachste Funktion
c = a.__mul__(b) # identischer Aufruf; entspricht der vorhergehenden Zeile
print(c)

#~~~ ~~~
# entspricht dem Aufruf: d = a.__mul__(4)
d = a * 4 # geht (noch) nicht: AttributeError: 'int' object has no attribute 'z'
print(d)

# ~~~ umgekehrte Reihenfolge ~~~~
e = 4 * a
# entspricht dem Aufruf: int(4).__mul__()
# ==> TypeError, da int keine Multiplikation mit einem Bruch unterstützt
# es schließt sich folgender Aufruf an:
# e = a.__rmul__(4)
print(e)

x = Bruch(5)

print(Bruch.ggT(12, 4))
