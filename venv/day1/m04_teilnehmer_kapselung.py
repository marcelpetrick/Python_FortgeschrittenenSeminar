import datetime
class Teilnehmer(object):
    def __init__(self, vorname, geburtsdatum, ort, sprachen): #magische Methode notwendig; Initialisieren des neuen Objektes; Konstruktormehtode
        '''
        Konstruktormethode - ganz spezielle Methode
        self: bedeutet die instanz, die mitgegeben wird
        Dokumentationskommentar
        '''
# Doxygen ... zum Beispiel um Zeugs zu kommentieren
        self.vorname = vorname
        self.__geburtsdatum = geburtsdatum
        self.ort = ort
        self.sprachen = sprachen

    # new magic method: representation
    def __repr__(self): # string angeben was ausgegeben werden soll, was derzeit das objekt ist; meist nie selber aufgerufen
        return "%s %s %s %s" % (self.vorname, self.__geburtsdatum, self.ort, self.sprachen)

    def getGeburtsdatum(self):
        return self.__geburtsdatum

    # setter
    def setGeburtsdatum(selfself, geburtsdatum):
        # not in the future
        if geburtsdatum <= datetime.date.today():
            self.__geburtsdatum = geburtsdatum
        else: # dann wie es in der OOP üblich ist: exception raushauen, die auch wieder eine klasse ist
            raise ValueError("ungültiges Geburtsdatum")

    # age of the current object
    def alter(self): #signatur of the method
        heute = datetime.date.today()
        datum = self.geburtsdatum
        jahre = heute.year - datum.year  # syntax highlighting
        if (datum.month, datum.day) < (heute.month, heute.day):  # lexikographischer vergleich
            jahre -= 1  # remove one if no party in the current year :'(

        return jahre
    ## ende der funktion

# variablen name = Instanziierung eines Objektes; ANlegen einer neuen Instanz
thomas = Teilnehmer("Thomas", datetime.date(1970,2,2), "Bielefeld", ["C", "Bash"])
marcel = Teilnehmer("Marcel", datetime.date(1983,1,1), "Kiel", ["C++", "Bash"])
henning = Teilnehmer("Henning", datetime.date(1960,1,16), "Hildesheim", ["Assembler", "RexX"])
martin = Teilnehmer(" Martin", datetime.date(1987,3,3), "Sindelfingen", ["Matlab"])
matthias = Teilnehmer("Matthias", datetime.date(1989,8,18), "Lichtenau", ["Matlab"])
daniel = Teilnehmer("Daniel", datetime.date(1980,1,1), "Bielefeld", ["Python", "Java"])

gruppe = [thomas, marcel, henning, martin, matthias, daniel]
print(gruppe) # einzeilige Ausgabe

# derzit wäre änderung zulässig; ebenfalls wäre so etwas wie 2019, 1,1 möglich
# oder: thomas.geburtsdatum = "Foo" # funktioniert, weil nur Eitketten - kein Typ
thomas.geburtsdatum = datetime.date(1994,1,1) # nicht mehr schick

# Idee der Kapselung: Zugriff auf die Eigenschaften der Objekte um Eigenschaften zu härten; Prüfung ob Änderung zulässig ist
# direkter Zugriff auf die Eigenschaft nicht mehr möglich, nur noch via Methode - die prüft, ob neues gültiges Geburtstdatum
# Bernd Klein - Python; schöne Webseite
# https://www.python-kurs.eu/python3_properties.php
# properties, klassenattribute, ..

# Eigenschaften mit _ sind als privat gekennzeichnet - ist aber nur reine Konvention
# nur in Kombination mit Methoden
# wirkt nur, wenn der Entwickler selber das Bewusstsein hat, dass diese Konvention gilt

# __ als Präfix scheint tatsächlich zu verbergen

# jetzt hätte man leider eine neue methode hinzugefügt zu dem objekt: als _Teilnehmer__vorname
# verhindert, dass man versehentlich etwas ändert - aber trotzdem ärgerlich, weil man nicht geändret hat
#thomas.__vorname = "Peter"

#thomas._Teilnehmer__vorname = "Peter" #is the same
# resultat: verhindert effektiv, dass man etwas überschreibt, aber man verhindert es nicht


# doppelter unterstrich: "privat"
# einfacher unterstrich: interne variablen, die nicht während initialisierung belegt werden

