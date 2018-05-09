# see and read: https://www.python-kurs.eu/generatoren.php

# Iteratoren
l = [1, 2, 3]
# Ausgabe ... zB. mit einer Schleife
# l = "zeichenkette" # auch iterierbar :))
# alles was iterierbar ist: strings, listen, dateien (mit for-schleife)
# dazu braucht man eine nect() und ein get_current()
for x in l:
    print(x)

iterator = iter(l)
while (True):
    try:
        x = next(iterator) # give me the next element, if there is no more, then return a default object
        print(x)
    except StopIteration:
        break
