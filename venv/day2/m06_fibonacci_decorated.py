# Der Parameter funk ist die zu dekorierende Funktion
# Nur die Definition wird genutzt. Es ist KEIN Aufruf!
def dekoriere(funk):
    d = {} # leeres Wörterbuch
    def dekorierte_funk(n):
        if n in d: # if found, then return the already computed thing
            return d[n]
        d[n] = funk(n) # else: decorate
        return d[n]

    return dekorierte_funk # neue Funktion wird auch zurükgegeben; Rückgabe ist die dekorierte Funktion

# the following line is a direct annotation for the decoration; could also be multiple decorations - separated by comma
@dekoriere
def fib(n):
    if n in (0,1):
        return 1
    return fib(n-2) + fib(n-1) #else vermieden: Einrückungstiefe gespart

# can be replaced by the decoration in line 13
#fib = dekoriere(fib)

print(fib(50)) # eventuell einmal mit pythontutor parsen

# closure als kontext des funktionsaufrufes