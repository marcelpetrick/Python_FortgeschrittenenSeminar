import datetime

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

thomas = ["Thomas", "2.2.70", "Bielefeld", ["C", "Bash"]]
marcel = [!Marcel", "1.1.1983", "Kiel", ["C++", "Bash"]]
gruppe = [thomas, marcel];


# unterschied rund eund eckige klammern?
# tupel () nicht veränderbar, aber listen [] sind