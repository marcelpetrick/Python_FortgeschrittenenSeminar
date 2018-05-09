def fib():
    a, b = 1, 1
    while (True): # muss wiederholt werden
        a, b = b, a + b
        yield a # neues Schlüsselwort: wartet hier immer auf Abruf des Ergebnisses

# Start des Generators: als Instanziierung
f = fib()
# einfach immer das nächste Ergebnis abfragen
print(next(f))
print(next(f))
print(next(f))
print(next(f))