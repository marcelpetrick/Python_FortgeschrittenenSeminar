import datetime

#neue funktion definieren (europäische variante)
def alter(datum):
    heute = datetime.date.today()
    jahre = heute.year - datum.year #syntax highlighting
    # lange variante
    if(datum.month, datum.day) < (heute.month, heute.day): # lexikographischer vergleich
        jahre -= 1 #eins abziehen

    return jahre
## ende der funktion

# Thomas, 2.2.70, Bielefeld, C, Java
# Marcel, 1.1.83, Kiel, C++, Bash
# Henning, 16.1.60, Hildesheim, Assembler, RexX
# Martin, 3.3.87, Sindelfingen, Matlab
# Matthias, 18.8.89, Lichtenau, Matlab
# Daniel, 1.1.80, Bielefeld, Python, Java

# 1) Welche Teilnhemer sind am jüngsten?
# 2) Aus welchen Orten kommen die jüngsten Teilnehmer?

# (Geeignete Datenstruktur finden und modellieren, so dass die Abfragen am einfachsten wäre?)
# Liste von Objekten (Klasse), oder?
# class person(string name, datetime birthdate, string location, list(string) knownLanguages);
# but how to do this in python?

# liste (tupel) als datenstruktur, eventuell mit wörterbuch?
# oder liste von klassen?

thomas = ["Thomas", datetime.date(1970, 2, 2), "Bielefeld", ["C", "Bash"]]
marcel = ["Marcel", datetime.date(1983, 1, 1), "Kiel", ["C++", "Bash"]]
gruppe = [thomas, marcel] #semikolons sind nicht notwendig - leere anweisung

# ### Zwei Arten von Strukturen waren möglich ### als beispiel erstmal mit Listen
## jetzt: wie abfragen?

# 0: Alter ermitteln? Geburtsdatum von heutigen Datum abziehen?
heute = datetime.date.today() #python: googlen wie datum erzeugen
# doc.python.org - dann auf 3 umstellen
diff = heute - datetime.date(2017, 1,1)
print("age:" , diff)

#print(alter(datetime(1983, 1, 1)))
# über alle teilnehmer der liste iterieren, dann zweites feld nutzen und in alter reinschieben
# important: list comprehension (im grunde eine verkuerzte schleife)
altersliste = [alter(teilnehmer[1]) for teilnehmer in gruppe]
print(altersliste)
# oder eingebaute map-function benutzen

# 1) Welche Teilnhemer sind am jüngsten?
# Alter erhalten?
# jetzt müsste man die namen mitspeichern. oder ausnutzen, dass alterliste ja auch reihenfolge hat
# ODER: alter in gruppeneinträge einfügen
kleinstes = min(altersliste) #find the smallest entry
namensliste = [teilnehmer[0] for teilnehmer in gruppe
               if alter(teilnehmer[1]) == kleinstes]
print(namensliste)

# 2) Aus welchen Orten kommen die jüngsten Teilnehmer?


# unterschied rund eund eckige klammern?
# tupel () nicht veränderbar, aber listen [] sind