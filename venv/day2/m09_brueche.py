# Homework: implement Vector

class Math:
    # wir brauchen etwas zum Kuerzen
    # 1  wenn b = 0 dann
    # 2    Ergebnis = a
    # 3  sonst
    # 4    Ergebnis = EUCLID(b, Divisionsrest(a durch b))    // siehe Modulo-Funktion
    # @staticmethod
    # def ggT(a, b):
    #     if b == 0:
    #         return a
    #     else:
    #         return Bruch.ggT(b, a % b)

    # or: math.gcd(a,b)

    # iterative Variante: siehe Wikipedia
    @staticmethod
    def ggT(a, b):
        while b != 0:
            h = a % b
            a, b = b, h
            # print (a,b)
        return a

    @staticmethod
    def kgV(a, b):
        return (a * b) // Math.ggT(a, b)

#-----------------------------------------------------------------------------------------

# Plan: Elemente der Datenstrukturen auch in natürlicher Weise nutzen können.
# Natürlich objekt-orientiert.
class Bruch(object):
    def __init__(self, z, n = 1): # zweiter Wert jetzt mit Default
        '''
        :param z: Zähler
        :param n: Nenner
        '''
        ggt = Math.ggT(z, n)
        self.z = z // ggt # um zu Verhindern, dass es Fließkommabehaftet wird
        self.n = n // ggt

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

#-----------------------------------------------------------------------------------------
    # ~~~ addition ~~~ soll funktionieren!
    def __add__(self, other):
        kgV = Math.kgV(self.n, other.n)
        #print(kgV)
        faktor1 = kgV // self.n
        faktor2 = kgV // other.n
        #print(faktor1, faktor2)
        #bruch1 = faktor1 * self
        #bruch2 = faktor2 * other
        return Bruch(self.z * faktor1 + other.z * faktor2, self.n * faktor1)
    # todo ... do the rest of the implementation
# -----------------------------------------------------------------------------------------
    # magic method
    def __repr__(self):
        return "%i / %i" % (self.z, self.n)
# -----------------------------------------------------------------------------------------

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

# test for a call without giving all parameters
x = Bruch(5)
# try to compute the greatest common divisor
print(Math.ggT(12, 4))

#infix operator
c *= a
print(c)

#-----------------------------------------------------------------------------------------
# Was ist pep? Anfragen zur Erweiterung des Standards
# PEP 0 -- Index of Python Enhancement Proposals (PEPs) ..

#-----------------------------------------------------------------------------------------
print("------------------------------------")
f = Bruch(3, 4)
g = Bruch(1, 8)
h = f + g
print(h)
print("good?")
# i = f + 3
# print(i)
# j = 3 + f
# print(j)
# print("unser zeug")
# print(Math.kgV(5,2))
