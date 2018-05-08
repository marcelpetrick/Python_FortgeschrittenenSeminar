# Der Parameter funk ist die zu dekorierende Funktion
def dekoriere(funk):
    d = {} # leeres Wörterbuch
    def dekorierte_funk(n):
        if n in d: # if found, then return the already computed thing
            return d[n]
        d[n] = funk(n) # else: decorate
        return d[n]

    return dekorierte_funk # neue Funktion wird auch zurükgegeben; Rückgabe ist die dekorierte Funktion

def fib(n):
    if n in (0,1):
        return 1
    return fib(n-2) + fib(n-1) #else vermieden: Einrückungstiefe gespart

fib = dekoriere(fib)

print(fib(50))