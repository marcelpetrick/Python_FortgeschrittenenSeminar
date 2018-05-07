def mittelwertFuerZwei(a, b):
    return (a + b) / 2.0 # else for python 2 it uses int instead of float; // as div operator for python 3

# pragmatisch mit eingebauter funktionalität von python
def mittelwertListe(liste):
    return sum(liste) / len(liste);

# dynamische liste
def mittelwert(*liste): #argumente in liste aufgesammelt
    return sum(liste) / len(liste);

print(mittelwertFuerZwei(3,4))

m = mittelwertListe([3,4,5])
print(m)

# schicker wäre aber
m = mittelwert(3,4,5) # erlaube beliebig viele argumente; aber eben anderer funktionsaufruf
print(m)

m = mittelwert(*[3,4,5]) #hier eine automatisch aufgesammelte Liste
print(m)