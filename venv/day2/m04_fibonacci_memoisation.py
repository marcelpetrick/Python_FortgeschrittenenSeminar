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
    return fib(n-2) + fib(n-1) #else vermieden: Einrückungstiefe gespart

fib = fib(30) # aber hat exponentielle Laufzeit
print(fib)



