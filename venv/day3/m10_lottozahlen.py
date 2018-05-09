from random import randint

def urne(k = 6, n = 49): # Standardbelegung
    gezogene = set() # Menge um Dopplungen zu vermeiden
    i = 0 # Anzahl der bisher gezogenen Kugeln
    # Strategie für die Implementierung: nicht davon ausgehen, dass man einen Generator schreiben möchte, sondern einfach
    # naiv implementiert und dann mit 'yield' ausgibt
    for i in range(k):
        while (True):
            kugel = randint(1, n) # inklusives Ende der Range
            if kugel not in gezogene:
                gezogene.add(kugel)
                yield kugel
                break

# --------------------------------------
urne1 = urne()
for x in urne1:
    print(x)