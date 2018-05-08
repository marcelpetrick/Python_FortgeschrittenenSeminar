# example dictionary
d = {"Tisch": "table",
     "Buch": "book",
     "Sonne": "sun", # verringert commit-log-changes & vereinfacht einfügen
     }
# Clou: Schlüssel kann über Wert abgerufen werden - auch "assoziatives Array"
# Schlüssel muss immer eineindeutig sein
print(d["Tisch"])
# question: how to reverse lookup?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# deshalb gleich neu: Memoisation - Caching! Merken von bereits bestimmten Ergebnissen

# Wie kann man sich Sachen merken? Dictionary
d = {} # Dictionary / Wörterbuch

def fib(n):
    if n in (0,1):
        return 1
    elif n in d: # wurde der Wert zuvor einmal berechnet?
        return d[n] # dann gib den zurueck
    d[n] = fib(n-2) + fib(n-1) # "cache das Ergebnis"
    return  d[n] #else vermieden: Einrückungstiefe gespart

# small helper for printing the call with some sugar
def printFib(n):
    print("Fibonacci of ", n, " = ", fib(n))

# do a call
printFib(1000)


